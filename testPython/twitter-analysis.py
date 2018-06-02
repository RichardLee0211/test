######################################
#
# Author: Guanhua Yan
#
######################################

import os, sys, json, math
from pprint import pprint

# nltk
import nltk
from nltk.corpus import cmudict
from nltk.corpus import stopwords
#from nltk.stem.wordnet import WordNetLemmatizer
#lmtzr = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stopwords_set = set(stopwords.words('english'))

# got from http://www.clips.ua.ac.be/pages/stop-words
martin_porter_stopwords_set = set([
"a","aboard","about","above","across","after","again","against","all","almost","alone","along","alongside","already","also","although","always","am","amid","amidst","among","amongst","an","and","another","anti","any","anybody","anyone","anything","anywhere","are","area","areas","aren't","around","as","ask","asked","asking","asks","astride","at","aught","away","back","backed","backing","backs","bar","barring","be","became","because","become","becomes","been","before","began","behind","being","beings","below","beneath","beside","besides","best","better","between","beyond","big","both","but","by","came","can","can't","cannot","case","cases","certain","certainly","circa","clear","clearly","come","concerning","considering","could","couldn't","daren't","despite","did","didn't","differ","different","differently","do","does","doesn't","doing","don't","done","down","down","downed","downing","downs","during","each","early","either","end","ended","ending","ends","enough","even","evenly","ever","every","everybody","everyone","everything","everywhere","except","excepting","excluding","face","faces","fact","facts","far","felt","few","fewer","find","finds","first","five","following","for","four","from","full","fully","further","furthered","furthering","furthers","gave","general","generally","get","gets","give","given","gives","go","goes","going","good","goods","got","great","greater","greatest","group","grouped","grouping","groups","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","high","high","high","higher","highest","him","himself","his","hisself","how","how's","however","i","i'd","i'll","i'm","i've","idem","if","ilk","important","in","including","inside","interest","interested","interesting","interests","into","is","isn't","it","it's","its","itself","just","keep","keeps","kind","knew","know","known","knows","large","largely","last","later","latest","least","less","let","let's","lets","like","likely","long","longer","longest","made","make","making","man","many","may","me","member","members","men","might","mightn't","mine","minus","more","most","mostly","mr","mrs","much","must","mustn't","my","myself","naught","near","necessary","need","needed","needing","needn't","needs","neither","never","new","new","newer","newest","next","no","nobody","non","none","noone","nor","not","nothing","notwithstanding","now","nowhere","number","numbers","of","off","often","old","older","oldest","on","once","one","oneself","only","onto","open","opened","opening","opens","opposite","or","order","ordered","ordering","orders","other","others","otherwise","ought","oughtn't","our","ours","ourself","ourselves","out","outside","over","own","part","parted","parting","parts","past","pending","per","perhaps","place","places","plus","point","pointed","pointing","points","possible","present","presented","presenting","presents","problem","problems","put","puts","quite","rather","really","regarding","right","right","room","rooms","round","said","same","save","saw","say","says","second","seconds","see","seem","seemed","seeming","seems","seen","sees","self","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","show","showed","showing","shows","side","sides","since","small","smaller","smallest","so","some","somebody","someone","something","somewhat","somewhere","state","states","still","still","such","suchlike","sundry","sure","take","taken","than","that","that's","the","thee","their","theirs","them","themselves","then","there","there's","therefore","these","they","they'd","they'll","they're","they've","thine","thing","things","think","thinks","this","those","thou","though","thought","thoughts","three","through","throughout","thus","thyself","till","to","today","together","too","took","tother","toward","towards","turn","turned","turning","turns","twain","two","under","underneath","unless","unlike","until","up","upon","us","use","used","uses","various","versus","very","via","vis-a-vis","want","wanted","wanting","wants","was","wasn't","way","ways","we","we'd","we'll","we're","we've","well","wells","went","were","weren't","what","what's","whatall","whatever","whatsoever","when","when's","where","where's","whereas","wherewith","wherewithal","whether","which","whichever","whichsoever","while","who","who's","whoever","whole","whom","whomever","whomso","whomsoever","whose","whosoever","why","why's","will","with","within","without","won't","work","worked","working","works","worth","would","wouldn't","ye","year","years","yet","yon","yonder","you","you'd","you'll","you're","you've","you-all","young","younger","youngest","your","yours","yourself","yourselves"
])
martin_porter_stopwords_set.add("http")


import cld
import gzip 
import pyspark
from pyspark import SparkContext
from operator import add

from time import gmtime, strftime

#conditional_set = set([])
#conditional_set.add(porter.stem('flu'))
#conditional_set.add(porter.stem('cough'))

def read_config(filename):
    input_filename = ''
    mode = ''
    cutoff_words = 0.01
    task = ''
    target = ''
    output_filename = ''

    fn = open(filename, 'r')
    for line in fn:
        if len(line) == 0 or line[0] == '#':
            continue
        fields = line.strip('\n').split('=')
        if len(fields) != 2:
            print "Input file has wrong format!"
            sys.exit()
        if fields[0].strip(' ').lower() == 'inputfile':
            input_filename = fields[1].strip(' ')
        elif fields[0].strip(' ').lower() == 'mode':
            mode = fields[1].strip(' ')
        elif fields[0].strip(' ').lower() == 'cutoff':
            cutoff_words = float(fields[1].strip(' '))
        elif fields[0].strip(' ').lower() == 'task':
            task = fields[1].strip(' ').lower()
        elif fields[0].strip(' ').lower() == 'target':
            target = fields[1].strip(' ').lower().split(',')
        elif fields[0].strip(' ').lower() == 'outputfile':
            output_filename = fields[1].strip(' ').lower()

    fn.close()
    return (input_filename, mode, cutoff_words, task, target, output_filename)

# 
# target is a list. convert it to a map
#
def index_target(target):
    indexed_target = {}
    for i in range(len(target)):
        indexed_target[ target[i] ] = i
    return indexed_target


#
# Obtain a list of words from a file
#
def get_words_by_file(filename):
    print "Start processing filename", filename, "at time", strftime("%Y-%m-%d %H:%M:%S", gmtime())
    expanded_filename = expand_filename(filename)

    tweet_list = []
    try:
        jsongz_fn = gzip.open(expanded_filename, 'r')
        for line in jsongz_fn:
            #print line
            x = get_words_by_line(line)
            if len(x) > 0:
                # the list is not empty
                tweet_list.append(x)
        jsongz_fn.close()
        """
        with gzip.GzipFile(expanded_filename, 'r') as jsongz_fn:
            for line in jsongz_fn:
                #print line
                x = get_words_by_line(line)
                if len(x) > 0:
                    # the list is not empty
                    tweet_list.append(x)
        """
    except Exception as e:
        print "Exception", e, "when processing gzipped file", expanded_filename

    print "Finished processing filename", filename, "at time", strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return tweet_list

#
# Get counts
#
def extract_selected_words(words_list, selected_words_set, target):
    # words_list corresponds to a tweet comprised of a list of words
    #print "words_list =", words_list
    #return len(words_list)
    words_set = set(words_list)
    index_list = []
    for x in target:
        if x in words_set:
            index_list.append('1')
        else:
            index_list.append('0')
    index_key = ''.join(index_list)

    target_set = set(target)
    selected_set = set([])
    for x in words_list:
        if x in selected_words_set and not (x in target_set):
            selected_set.add(x)
    print index_key, selected_set
    return (index_key, selected_set)


#
# aggregate the word counts
#
def aggregate_word_counts(x, y):
    # y is a list of lists of words
    count_map = {}
    for z in y:
        for w in z:
            if w in count_map.keys():
                count_map[w] = count_map[w] + 1
            else:
                count_map[w] = 1
    count_list = []
    for w in count_map.keys():
        count_list.append( (w, (x, count_map[w])) )

    return count_list

#
# calculate mutual information
#
def calc_mutual_information(pattern_count_list, pattern_map):
	# an item in pattern_count_list is like: [ pattern, count ]
	    total_w_count = 0
	    for (pa, cnt) in pattern_count_list:
	    total_w_count = total_w_count + cnt

	    total_count = 0
	    for x in pattern_map.keys():
		    total_count = total_count + pattern_map[x]

		    mi = 0.0
		    for (pa, cnt) in pattern_count_list:
# pattern, count with this word
		    pr_pa_w = cnt    
# pattern, count without this word
		    pr_pa_no_w = pattern_map[pa] - cnt
# count with this pattern
		    pr_pa = pattern_map[pa]
# count without this word
		    pr_no_w = total_count - total_w_count

		    print "pa =", pa, "cnt =", cnt, "pr_pa_w =", pr_pa_w, "pr_pa_no_w =", pr_pa_no_w, "pr_pa =", pr_pa, "pr_no_w =", pr_no_w, "total_w_count =", total_w_count, "total_count =", total_count

mi = mi + 1.0 * pr_pa_w / total_count * math.log(1.0 * pr_pa_w / pr_pa / total_w_count * total_count)
	if pr_pa_no_w > 0:
mi = mi + 1.0 * pr_pa_no_w / total_count * math.log (1.0 * pr_pa_no_w / pr_pa / pr_no_w * total_count)

	return mi

#
# Expand a filename if it contains an environment variable
#
def expand_filename(filename):
    if '$' in filename:
        fields = filename.split('/')
        print fields
        output = []
        for x in fields:
            if '$' in x:
                if '$' != x[0]:
                    print "This is wrong. $ must be at the beginning!"
                    os.exit()
                items = x.split('$')
                if len(items) != 2:
                    print "This is wrong. There can only be one $!"
                    os.exit()
                output.append( os.environ[ items[-1] ] )
            else:
                output.append( x )
        return '/'.join(output)
    else:
        return filename

#
# Obtain a list of words from a line
#
def get_words_by_line(line):
    detection_result = ""
    wordlist = []
    if line:
        try:
            items = json.loads(line)
        except Exception as e:
            print "Exception", e, "when calling json.loads", line
            return []
        #pprint(items)
        if u'text' in items.keys():
            #print "text", items[u'text'] 
            txt = items[u'text']
            fields = txt.split(' ')
            if len(fields) >= 2 and fields[0] == 'RT' and len(fields[1]) > 0 and fields[1][0] == '@': # and fields[1][-1] == ':':
                # deal with retweets
                fields.pop(0)
                while len(fields) > 0:
                    if len(fields[0]) == 0 or fields[0][0] == '@':
                        fields.pop(0)
                    else:
                        break
                newtxt = ' '.join(fields)
                #detection_result = cld.detect(newtxt.encode('utf-8'))
            elif len(fields) > 0 and len(fields[0]) > 0 and fields[0][0] == '@':
                while len(fields) > 0:
                    if len(fields[0]) == 0 or fields[0][0] == '@':
                        fields.pop(0)
                    else:
                        break
                newtxt = ' '.join(fields)
                #detection_result = cld.detect(newtxt.encode('utf-8')) 
            else:
                newtxt = txt

            #print "newtxt =", newtxt
            encodedtxt = newtxt.encode('utf-8')
            try:
                detection_result = cld.detect(encodedtxt)
            except Exception as e:
                print "Exception in cld.detect:", e
                return []

        if len(detection_result) > 0 and detection_result[0].lower() == 'english':
            tokens = nltk.word_tokenize(encodedtxt)
            stemwords = []
            for t in tokens:
                # ignore strings starting with "//"
                if len(t) >= 2 and t[0] == '/' and t[1] == '/':
                    continue
                processed_t = t.strip(",|.;\/\\*\'\"").lower()
                # check whether processed_t contains special characters
                # we don't consider numbers, stopwords, and single characters
                if len(processed_t) >= 2 and processed_t.isalnum() and not processed_t.isdigit() and not (processed_t in martin_porter_stopwords_set): # and cld.detect(processed_t)[0].lower() == 'english':
                    #stemwords.append(lmtzr.lemmatize(t))
                    stemmed_w = porter.stem(processed_t)
                    #if not (stemmed_w in stopwords_set):
                    wordlist.append(stemmed_w)

    return wordlist

def get_edges(words_list, nodes_set):
    edge_list = []
    for i in range(len(words_list)):
        for j in range(len(words_list)):
            if i >= j:
                continue
            if words_list[i] in nodes_set and words_list[j] in nodes_set:
                if words_list[i] <  words_list[j]:
                    #edge_list.append((words_list[i], words_list[j]))
                    edge_list.append(words_list[i] + '|' + words_list[j])
                elif words_list[i] > words_list[j]:
                    edge_list.append(words_list[j] + '|' + words_list[i])

    #print words_list, edge_list
    return edge_list

def test(x):
    return len(x)

# count the number of appearances for each pair of keywords
def count_single_appearances(words_list, selected_words_set):
    ret_list = []
    words_set = set([])
    for w in words_list:
        if w in selected_words_set:
            words_set.add(w)
    for w in words_set:
        ret_list.append(w)
    return ret_list

# count the number of appearances for each pair of keywords
def count_pairwise_appearances(words_list, selected_words_set):
    ret_list = []
    words_set = set([])
    for w in words_list:
        if w in selected_words_set:
            words_set.add(w)
    xlist = list(words_set)
    for i in range(len(xlist)):
        for j in range(len(xlist) - i - 1):
            if xlist[i] < xlist[i + j + 1]:
                ret_list.append( (xlist[i], xlist[i + j + 1]) )
            else:
                ret_list.append( (xlist[i + j + 1], xlist[i]) )
    return ret_list


if __name__ == "__main__":
    configfile = sys.argv[1]
    (input_filename, mode, cutoff_words, task, target, output_filename) = read_config(configfile)
    print "target =", target, "cutoff_words =", cutoff_words
    #sys.exit()

    sparkcontext = SparkContext(mode, 'TwitterAnalysis')
    input_fn = open(input_filename, 'r')
    inputfiles = input_fn.readlines()
    input_fn.close()

    # sentences is a list of tweet, each represented as a list of words.
    rdd__sentences = sparkcontext.parallelize(xrange(0, len(inputfiles))) \
        .flatMap(lambda x: get_words_by_file(inputfiles[x].strip('\n'))) 
    rdd__sentences.cache()

    # sorted_words is a list of (count, word) pairs, which is sorted by the count.
    rdd__sorted_words = rdd__sentences.flatMap(lambda x: x) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add) \
        .map(lambda (x,y): (int(y), x)) \
        .sortByKey(False) 

    # we select only a fraction of words for consideration, which ignores those that are not important.
    # the fraction is given as input parameter cutoff_words
    total_number = rdd__sorted_words.count()
    num_selected_words = int(cutoff_words * total_number)
    print "num_selected_words =", num_selected_words
    cutoff = rdd__sorted_words.take(num_selected_words)[-1][0]
    print "cutoff =", cutoff

    # selected_words is a list of words that are selected
    rdd__selected_words = rdd__sorted_words.filter(lambda (x,y): x >= cutoff).map(lambda(x,y): y)
    rdd__selected_words.cache()

    selected_words_list = rdd__selected_words.collect()
    selected_words_set = set(selected_words_list)

    # for the 'create_graph' task, we want to create a graph comprised of words
    if task == 'create_graph':
        print "list of nodes..."
        for node in selected_words_list:
            print node

        # the following code shows construction of edges among selected nodes (an edge is created if two words 
        # belonging to the selected node set show in a tweet at the same time.
        print "list of edges..."
        rdd__edges = rdd__sentences.flatMap(lambda x: get_edges(x, selected_words_set)) \
            .map(lambda x: (x, 1)) \
            .reduceByKey(add) \
            .map(lambda (x,y): (int(y), x)) \
            .sortByKey(False)

        edges_list = rdd__edges.collect()
        for (cnt, edge) in edges_list:
            print tuple(edge.split('|')), cnt

    # for the 'mutual_information' task, we want to calculate the mutual information between the target set and 
    # any selected word
    elif task == 'mutual_information':
        # indexed_target = index_target(target)

        """
        # testing
        print "count of sentences", sentences.count()
        pattern_words = sentences.map(lambda x: extract_selected_words(x, selected_words_set, target))
        #pattern_words = sentences.map(lambda x: test(x))
        print "count of pattern_words", pattern_words.collect()
        print pattern_words
        sys.exit()
        """

        # for each pattern in terms of appearances of target words, we obtain a list of tweets comprised of a list of selected words
        rdd__pattern_words = rdd__sentences.map(lambda x: extract_selected_words(x, selected_words_set, target) ).groupByKey() 
        rdd__pattern_words.cache()

        rdd__pattern_count = rdd__pattern_words.map(lambda(x, y): (x, len(y)))
        pattern_list = rdd__pattern_count.collect()
        pattern_map = {}
        for x in pattern_list:
            pattern_map[x[0]] = x[1]

        # calculate mutual information
        rdd__mutual_information = rdd__pattern_words.flatMap(lambda(x, y):  aggregate_word_counts(x, y)) \
            .groupByKey() \
            .map(lambda(x, y): (calc_mutual_information(y, pattern_map), x) ) \
            .sortByKey(False)

        local_mi = rdd__mutual_information.collect()
        for (mi, w) in local_mi:
            print w, mi

    # calculate pairwise (positive) mutual information
    elif task == 'pairwise_mutual_information':
        rdd__single_counts = rdd__sentences.flatMap(lambda x: count_single_appearances(x, selected_words_set)) \
            .map(lambda x: (x, 1.0)) \
            .reduceByKey(add)

        single_counts_map = rdd__single_counts.collectAsMap()
        rdd__pairwise_counts = rdd__sentences.flatMap(lambda x: count_pairwise_appearances(x, selected_words_set)) \
            .map(lambda x: (x, 1.0)) \
            .reduceByKey(add) \
            .map(lambda ((x, y), c): ((x, y), c * math.log(c / single_counts_map[x] * single_counts_map[y], 2 ) )) \
            .filter(lambda ((x, y), c): c > 0)
        pairwise_counts_map = rdd__pairwise_counts.collectAsMap()

        print "#nodes =", len(selected_words_list), "#edges =", len(pairwise_counts_map) 
        #sys.exit()

        """
        for key in pairwise_counts_map.keys():
            print key, pairwise_counts_map[key]
        """

        # create an adjancy list to keep all the pairwise information.
        graph_list = {}
        # create feature map
        feature_map = {}
        for i in range(len(selected_words_list)):
            feature_map[ selected_words_list[i] ] = i

        #graph_list = [ [] ] * len(selected_words_list)
        graph_list = []

	output_nodes_filename = output_filename + '.nodes'
	output_nodes_fn = open(output_nodes_filename, 'w')
        for i in range(len(selected_words_list)):
            graph_list.append([])
	    print >> output_nodes_fn, i, selected_words_list[i]
	output_nodes_fn.close()

        #for i in range(len(graph_list)):
        #    #print "Thinking...", i, len(graph_list[i])

        for key in pairwise_counts_map.keys():
            #if feature_map[key[0]] == 0 or feature_map[key[1]] == 0:
            #    print "Before...", graph_list[0]

            #print "Inserting...", key, feature_map[key[0]], feature_map[key[1]], pairwise_counts_map[key]
            graph_list[ feature_map[key[0]] ].append( ( feature_map[key[1]], pairwise_counts_map[key] ) )
            graph_list[ feature_map[key[1]] ].append( ( feature_map[key[0]], pairwise_counts_map[key] ) )

            #if feature_map[key[0]] == 0 or feature_map[key[1]] == 0:
            #    print "Inserting...", key, feature_map[key[0]], feature_map[key[1]], pairwise_counts_map[key]
            #    print "After...", graph_list[0]
            #    sys.exit()

        print "Finished creating graph_list..."
        # print it to the output filename
        output_fn = open(output_filename, 'w')
        for i in range(len(graph_list)):
            for j in range(len(graph_list[i])):
                print >> output_fn, i, graph_list[i][j][0], graph_list[i][j][1]
        output_fn.close()



