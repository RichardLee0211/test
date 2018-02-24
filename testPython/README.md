trying to download pip with get-pip.py provided by
https://pip.readthedocs.io/en/stable/installing/
but get errors
and then try
```bash
sudo python get-pip.py # success
```
```bash
sudo pip install "ipython[notebook]" --upgrade --ignore-installed six
OSError: [Errno 1] Operation not permitted:
'/System/Library/Frameworks/Python.framework/Versions/2.7/share'
```
solution may be here:
https://stackoverflow.com/questions/33004708/osx-el-capitan-sudo-pip-install-oserror-errno-1-operation-not-permitted

MacOS seems to refuse to install ipython[notebook] using
```bash
sudo pip install "ipython[notebook]" --upgrade --ignore-installed six
```

and this does successful
```bash
sudo pip3 install "ipython[notebook]" --upgrade --ignore-installed six
```

set up a vitual environment for python using tutorial in:
https://packaging.python.org/tutorials/installing-packages/

I think I start to love ipython, with great auto-completion feature
and from http://docs.python-guide.org/en/latest/dev/virtualenvs/, python 2 will
retire in 2 years.

install virtualenv and create python2 env, using ipython2 for coding

to exit virtual env of python, type deactivate

## note of python data science essential
```python2
import pandas as pd

iris_filename = 'datasets-uci-iris.csv'

iris = pd.read_csv(iris_filename, sep=',', header=None, \
        names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width',\
        'target'])
iris.head()
iris.tail()
iris.columns
Y = iris['target']; Y
X = iris['sepal_length', 'sepal_width']; X
```

```python2
import pandas as pd
fake_dataset = pd.read_csv('a_loading_example_1.csv', sep=',')
fake_dataset
fake_dateset = pd.read_csv('a_loading_exmaple_1.csv', parse_dates = [0])
fake_dateset
fake_dateset.filena(50)
```

load large dataset
```python2
import pandas as pd
iris_chunks = pd.read_csv(iris_filename, header=None, \
                    name=['C1', 'C2', 'C3', 'C4', 'C5'], chunksize=10)
for chunk in iris_chunks:
    print chunk.shape
    print chunk
```
way2:
```python2
iris_chunks = pd.read_csv(iris_filename, header=None, \
                    name=['C1', 'C2', 'C3', 'C4', 'C5'], iteratior=True)
print iris_iterator.get_chunk(10)
print iris_iterator.get_chunk(20)
piece = itis_iterator.get_chunk(2)
```

```python2
with open(iris_filename, 'rb') as data_stream:
    for n, row in enumerate(csv.DictReader(data_stream, \
        filenames = ['sepal_length', 'sepal_width', 'petal_length', \
        'petal_width', 'target'], dialect='excel')):
        if n == 0:
            print n, row
        else:
            break

```

```python2
with open(iris_filename, 'rb') as data_stream:
    for n, row in enumerate(csv.reader(data_stream, dialect='excel')):
        if n==0:
            print row
        else:
            break
```

```python2

def batch_read(filename, batch=5):
    # open the data stream
    with open(filename, 'rb') as data_stream:
        # reset the batch
        batch_output = list()
        # iterate over the file
        for n, row in enumerate(csv.reader(data_stream, dialect='excel')):
            # if the batch is of the right size
            if n > 0 and n % batch == 0:
                # yield back the batch as an ndarray
                yield(np.array(batch_output))
                # reset the batch and restart
                batch_output = list()
            # otherwise add the row to the batch
            batch_output.append(row)
        # when the loop is over, yield what's left
        yield(np.array(batch_output))
```

mask
```python2
mask_target = iris['target'] == 'Iris-virginica'
iris.loc[mask_target, 'target'] = 'New label'
iris['target'].unique()
```

group
```python2
grouped_targets_mean = iris.groupby(['target']).mean()
grouped_targets_var = iris.groupby(['target']).var()
iris.sort_index(by='sepal_length').head()
```

```python2
dataset = pd.read_csv('a_selection_example_1.csv')
dataset = pd.read_csv('a_selection_example_1.csv', index_col=0)
```

TODO:
- [x] master ipython and load python2 into it # using ipython2
- [ ] how to using ipyhton as ipyhon notebook, to code blocks and exam each step
- [ ] find some analysis ways
