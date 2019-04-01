this question is always around, hack it

find this website: https://www.random.org/

what do I think
================================================================================

TODO:
- [ ] figure out the principal of random number generator
- [ ] figure out the principal of prediction algorithm
- [ ] figure out the statistical test for RNGs
- [ ]

Do I commited to Data analysis?: Yes, for this semester, I have 2 weeks to go for stage 1

feel like can't distinguish real and pseudo random generator with statistic attributes
- RNN
- simple pseudo random generator algorithms

statistics is way more complex than I thought, need to use it well
math real needs a certain mindset to dig in
the base line is
- I need to understand and use ML methods include Random forest
- I need to understand randomness and write a report

take python first

lovely, time series analysis would need Fourier transform

feel like knowledge that I learned a long time ago are waiting for me to discover again

[kaggle](https://www.kaggle.com/competitions) is a good place to go, but for now, I am not lack data. I need to see more data analysis code

TODO: [bootstrap](https://www.uvm.edu/~dhowell/StatPages/Resampling/BootstMeans/bootstrapping_means.html)

to edit multiply lines in ipython:
- way1: using ;\
- way2: %edit

a little trick to use ipython:
```python
    %edit # to edit a new temperlary file
    %edit -p  # to edit the previous file
    %edit _NN # NN is the output number, to edit that file/section
    %edit <function name> # to edit the function

    %run <script_file_name>

    %debug

    %save hello.py NN  # NN the input section number
    %save -a hello.py _NN # _NN the output section number, -a append

    %recall
    %timeit
    %history
```

TODO_3: more about [ipython tips](http://pages.physics.cornell.edu/~myers/teaching/ComputationalMethods/python/ipython.html)

程序员的数学2 概率统计 by 平冈和幸
================================================================================
my pdf is in chinese...

ch07 pseudo number 伪随积数
--------------------------------------------------------------------------------
let finish this chapter
mersenne twister: one pseudo random generator
TODO: [MT](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html)

Monte Carlo method
TODO_2: using random number to estimate pi
this method is like brute force in algorithms

this chapter doesn't really touch the core of random number
it tells me that tell whether a certain series of time is random number is meaningless

ch08 概率学的各类应用
--------------------------------------------------------------------------------
TODO: didn't really do the exercise, it could be every important for further analysis
### 8.1 回归分析和多变量分析
TODO: 主成分分析，principla component analysis, PCA

### 8.2 随机过程
stochastic process

!! 练习题8.3 技巧型很强
!! 练习题8.4
!! 练习题8.5

#### 8.2.2 卡尔曼滤波器

#### 8.2.3 马尔可夫链

### 8.3 信息论
TODO_2: this is a mount to climb

analysis2001.pdf
================================================================================

don't have a good content table

## 2 conclutions and recommendations
uniformity: the histogram and the chi-squared tests
independence: the autocorreletion plot
summation and duplication: the summary statistics

### 3.2 summary statistics

### 3.3 data analysis plots:
TODO: how to do it in python
TODO: need to know more about statistics
- a run sequence plot
- a log plot
- a histogram
- an autocorrelation plot

## 4 the test criteria and the tests chosen

### 4.1 the test criteria
..., page.9

test chosen:
- a chi-squared test
- a test of runs above and below the median
- a reverse arrangement test
- an overlapping sums test
- a binary rank test for 32X32 matrices

E.3 L'Ecuyer's Generator with Bays-Durham shuffle
--------------------------------------------------------------------------------
!!, have a code of seudo random number generator

[correlogram](https://en.wikipedia.org/wiki/Correlogram):
check randomness in a data set
TODO: don't really understand the defination and how it works

TODO: need to understand these test
TODO: need understand statics better

Analysis2005.pdf
================================================================================

great, good paper reading is half of the project

cool, NIST test suit(15 test)

flip a coin, exact modeling could predict

random test is like security.
No one define obsolute randomness, and no one define obsolute security
but when they pass more test, the confidence of randomness/security increases

ENGLISH: pass the battery of tests

D. TYPES OF PRNGs
--------------------------------------------------------------------------------
!! this would be useful for my report

K. DESCRIPTION OF THE NIST TESTS
--------------------------------------------------------------------------------
!! this would be useful for my report

a little reading about p-value:
- null-hypothesis(H_0): the hypothesis of original status
- alternative-hypothesis(H_a): the hypothesis of new status(new method is better), where heavy proof goes
- P-value is smaller than threshold(\alpha, e.g. 0.05 or 0.01 or researcher decided value),
then we could reject H_0 and go H_a, and engineers are happy

e.g.
H_0: this sequence is random
H_a: this sequence is no-random
if P-value < \alpha then reject H_0, H_a is right

Ho, I love "GNU Scientific Library" and scipy when I gonna implement these tests


statics handbook
================================================================================
introduce the statics handbook from [here](https://www.itl.nist.gov/div898/handbook/)

it's a 2000 pages book,
the first part, Exploratory Data Analysis, has 600 pages.
every good document but maybe too many details for starters

Statistic for Technology
================================================================================
wanna read the "Statistics for Technology" book that analysis2001.pdf refered
maybe could get it from Binghamton library


log
================================================================================

following this [ML predict RNG discussion](https://ai.stackexchange.com/questions/3850/using-machine-deep-learning-for-guessing-pseudo-random-generator)

```shell
    pip install virtualenv
    pip install virtualenvwrapper
```

pip install tensorflow failed
```shell
    ➜  Code pip install tensorflow
    Collecting tensorflow
      Could not find a version that satisfies the requirement tensorflow (from versions: )
      No matching distribution found for tensorflow
```
because in my macOS, python 3.7, and tensorflow is only compatible with python 3.4 3.5 3.6
[here](https://github.com/tensorflow/tensorflow/issues/20444)

pip uninstall keras

calm down and learn virtualenv first
[here](https://virtualenv.pypa.io/en/latest/)

[Use different Python version with virtualenv](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)

python3.6 make test failed

this is really time consuming to comfront this problem, I just wanna to test a python script

try it on Ubuntu virtual mechine
Ubuntu refuse to apt-get install pip3

finally, I choose to give Anaconda a try. Don't wanna spend my whole night in installation

and Yes, Anaconda helped me to manager my package version issue. use it for now

I need to understand the ML modle the code uses.

Okay, look. I would put some serious pictures in github repository and use markdown file to organize them.
now I would need a command line picture view in Ubuntu if it is my daily working OS,
then it would make things easier

```shell
    # what I need to do when using command output as a string
    ls -al `which youtube-dl`

    # what you need to do when connect two stream
    which youtube-dl | ls -al

    # what you need to do to deal with file and command
    ./command > outputfile
    ./command < inputfile > outputfile
```

need to source ~/.bash_profile, which is appended with some code by anaconda.
because I use zsh.

what would I do if you only receive bad reflects? keep digging

following this [blog](https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/)
to do installation, library management could be better than pip

tensorflow is now not compatible with python3.7, pip return a error; while
anaconda manage to build a virtual enveronment(in ~/.bash_profile) and downgrade software version.
Just make everything work for now

TODO:
well, the RNG predistion proble in ML is a classification problem, then
what's the relationship that might exists between the prediction algorithm and
intellectual problems that I saw before?

I will need more coding

- LCG: https://en.wikipedia.org/wiki/Linear_congruential_generator
- Randomness tests: https://en.wikipedia.org/wiki/Randomness_tests
    great, reference to "Numerical Recipes" and GCC



```shell
    # LCG
    ➜  testRandom git:(master) ✗ ./test 1664525 1013904223 4294967296 2 10
    3CA1BF79
    75C0E284
    305F0C13
    BDED2256
    B78DF5BD
    1E02BBF8
    34AF4EF7
    78EB5FEA
    86740E41
    B25A92AC
    B444EE1B
    ➜  testRandom git:(master) ✗ ./test 8 2 1024 1 20
    A
    52
    292
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
    92
```

ENGLISH: It may well seem surprising that a group of just 23 individuals is
required to reach a probability of 50% that two individuals in the group have the same birthday

TODO: Real-world applications for the birthday paradox include a cryptographic
attack called the birthday attack, which uses this probabilistic model to reduce
the complexity of finding a collision for a hash function.

ENGLISH: In deference to

TODO: python3 calculate 364*363*362*...*(365-22), what's it called??

100% means it always happen, 0% means it never happened.
but always happening doesn't mean 100%, never happened doesn't 0%.
Because we don't know the future. We also only know a little about past.

Random meaning patternless

TODO: For example, the infamous RANDU fails many randomness tests dramatically, including the spectral test.
a = 65539 c=0 m=2^31

ENGLISH: The use of an ill-conceived random number generator can put the validity
of an experiment in doubt by violating statistical assumptions.

TODO:
- Yongge Wang. On the Design of LIL Tests for (Pseudo) Random Generators and Some Experimental Results, http://webpages.uncc.edu/yonwang/, 2014
- Yongge Wang; Tony Nicol (2014), "Statistical Properties of Pseudo Random Sequences and Experiments with PHP and Debian OpenSSL", Esorics 2014, Lncs 8712: 454–471

ENGLISH: String 1 admits a short linguistic description: "32 repetitions of '01'".

#### how to use conda
https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html
get cheat sheet here, using it as my python environment manager
```shell
    conda create --name test
    conda create --clone base --name test02 # copy base into test02
    conda env export --name ENVNAME > envname.yml
    conda env create --file envname.yml

    conda activate test
    conda env list
    conda install --yes PKGNAME1 PKGNAME2
    conda update PKGNAME
    conda remove PKGNAME
```

#### about shared fold in VMware Fusion 8
solve VMware share fold, follow intructions from VMware Fusion 8 Help manual,
need to mount device. Cool.
with VMware Fusion 8, the Shared fold need to install tools to Guest OS.

#### about if __name__ == "__main__":
from: https://stackoverflow.com/questions/419163/what-does-if-name-main-do

feel happy to see OpenMP, a term that I understand
```shell
    (test) ➜  testRandom git:(master) ✗ python3 test3.py
    Using TensorFlow backend.
    WARNING:tensorflow:From /Users/wenchen/anaconda3/envs/test/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Colocations handled automatically by placer.
    WARNING:tensorflow:From /Users/wenchen/anaconda3/envs/test/lib/python3.6/site-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use tf.cast instead.
    Epoch 1/1
    2019-03-29 12:23:51.265799: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
    2019-03-29 12:23:51.266984: I tensorflow/core/common_runtime/process_util.cc:71] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
    OMP: Error #15: Initializing libiomp5.dylib, but found libiomp5.dylib already initialized.
    OMP: Hint: This means that multiple copies of the OpenMP runtime have been linked into the program. That is dangerous, since it can degrade performance or cause incorrect results. The best thing to do is to ensure that only a single OpenMP runtime is linked into the process, e.g. by avoiding static linking of the OpenMP runtime in any library. As an unsafe, unsupported, undocumented workaround you can set the environment variable KMP_DUPLICATE_LIB_OK=TRUE to allow the program to continue to execute, but that may cause crashes or silently produce incorrect results. For more information, please see http://www.intel.com/software/products/support/.
    [1]    83442 abort      python3 test3.py
```

wait, ipython doesn't using conda environment

conda install ipython
conda install matplotlib
conda install keras

this is cons of python, environment management

TensorFlowPrediction.py works on base conda environment

ENGLISH: For the user, the most salient distinction is probably this

manage python package:
- pip + virtualenv
- conda

ENGLISH: An entire generation of scientific Python users spent countless hours
struggling with the installation hell created by this exercise of forcing a
square peg into a round hole – and those were just ones lucky enough to be using
Linux. If you were on Windows, forget about it.

a way to install conda:
- pip install conda
- or search_download_install anaconda

PyPI(python package index)

TODO: given a math function, calculate integrate to some precision

|-----------------------------------------------------------------------------|
|random eng | frequency | frequencyBlock |------------------------------------|
|-----------------------------------------------------------------------------|
|random_dev | 0.77564   |0.00398---------|------------------------------------|
|srand0     | 0.00000   |----------------|------------------------------------|
|srand2     | 0.00000   |----------------|------------------------------------|
|LCG01      | 0.53855   |----------------|------------------------------------|
|LCG02      | 0.65271   |----------------|------------------------------------|
|mt19937    | 0.14156   |----------------|------------------------------------|
|ranlux24   | 0.61356   |----------------|------------------------------------|
|homeLCG01  | 0.87682   |----------------|------------------------------------|
|homeLCG02  | 0.00000   |----------------|------------------------------------|
|-----------------------------------------------------------------------------|

#### test for longest run of ones in a Block
choose K=5, M=128
|-------|-----------------------|
| class | probabilities         |
|-------|-----------------------|
| v<=4  | pi_0 = 0.1174         |
| v=5   | pi_1 = 0.2430         |
| v=6   | pi_2 = 0.2493         |
| v=7   | pi_3 = 0.1752         |
| v=8   | pi_4 = 0.1027         |
| v>=9  | pi_5 = 0.1124         |
|-------|-----------------------|

maybe checkout:
1. NIST (National Institute of Standards and Technology), A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications. 2001  
2. Knuth, Donald E., The Art of Computer Programming - Seminumerical Algorithm. Vol 2 Chapter 3 Random Numbers pg1-184. 1997.  
3. Menezes, van Oorschot and Vanstone, Handbook of Applied Cryptography, CRC Press 1997.  
4. Lavarand http://lavarand.sgi.com  
5. Vattulainen et al., A Comparative Study of Some Pseudorandom Number Generators,  Department of Electrical Engineering, August 1993.  
6. Klimasauskas, C. Not Knowing Your Random Number Generator Could be Costly: Random  Generators – Why Are They Important. PCAI (PC Artificial Intelligence) Issue 16.3 pg 50-56  
7. Rutti, Mario, A Random Number Generator Test Suite for the C++ Standard (Diploma Thesis), Institute for Theoretical Physics, Zurich, 2004. http://www.comp- phys.org:16080/rngts/doc/main.pdf  
8. How We Learned to Cheat at Online Poker: A Study in Software Security By Brad Arkin  Frank Hill Scott Marks Matt Schmid and Thomas John Walls  http://www.developer.com/tech/article.php/616221  
9. The Evaluation of RPG100 by Using NIST and DIEHARD tests, FDK Corporation, Dec 2003.  http://www.fdk.co.jp/cyber-e/pdf/HM-RAE104.pdf  

###
errors in K.10 in 2005report, d calculation

### over_lapping template matching test
this is ... , bad reporter
pi_0 0.367879
pi_1 0.183940
pi_2 0.137955
pi_3 0.099634
pi_4 0.069935
pi_5 0.140657

I don't wanna reclaim the math process to calculate P_value, as doing so in
five-pages report would lose a lot of detail and explaination, which is necessary
to fully understand and implement them. An example has been made in 2005 report.

ε = “the first 1,000,000 binary digits in the expansion of e”

1. virtualization
2. test suit
3. conbine
