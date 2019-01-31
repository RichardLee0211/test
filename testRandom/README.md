this question is always around, hack it

find this website: https://www.random.org/

what do I think
================================================================================
Do I commited to Data analysis??
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
way1: using ;\
way2: %edit

a little trick to use ipython:
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
- a hitogram
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
TODO: don't really understand the definationa and how it works

TODO: need to understand these test
TODO: need understand statics better

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
