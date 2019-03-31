Python for data analysis.pdf
================================================================================

I have been this repository before, I stared it somehow.
https://github.com/wesm/pydata-book/

this a 2-nd edit release in 2017

ch01 preliminaries
--------------------------------------------------------------------------------
- numpy
- pandas
- matplotlib
- Ipython and Jupyter(perfer Ipython)
- Scipy
- scikit-learn
- statsmodels

python conference:
- PyCon and EuroPython
...

we also have C++ conference
refer back DragonBoat data project, back to time, I must be the worstest performance man in the team
this is actually not a bad experience to view .ipynb file in github, thanks, github
the "pic" in .ipynb is actually HTML5 code, crazy one, nice touch
and some pic are stored in Base64 code
Base64: A~Z, a~z, 0~9, +, /

install ipython and jupyter seems to be easier in MacOS
just do
```shell
    pip3 install --upgrade pip
    pip3 install ipython
    pip3 install jupyter
```
to run
```shell
    ipython # or
    jupyter notebook
```
considering EDA have many virtualization, notebook could be a good tool
.ipynb file is compatiable with git
thus,
when do EDA, use jupyter notebook
otherwise, use python .py file for programming

when don't need vistualization, Jupyter seems to be extra tool that I don't need
Ipython could also open pictures in EDA, but may not be organized in order. Could put pictures in a fold
and Jupyter could be slow in my MBP when open a "notebook", that's a performance problem when you try to do IDE staff
the benefit of jupyter is that it's a good reading tool

I will need to work with picture or other GUI, but with command line taking my commands


ch02 Python lanuage basics, Ipython and Jupyter Notebooks
--------------------------------------------------------------------------------
Python would not be type-safe
what if a is user-define class and + is undefined
this is argument of control and convinient, for me, control is more important
```python
def add_numbers(a, b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a+b
```

this is like ??
```c++
    template<class T>
    auto add(T a, T b){
        return a+b;
    }
```

I will need to replace defensive code into assert() function, and remove them by #define DEBUG in the final production

everytime get into a new tech, get to review the basic. My time...55555

some useful short cut for Unix bash shell and Ipython shell:
C-a, C-e, C-c, C-r(history search), C-l(clear screen)

table 2-2 some frequently used Ipython magic commands, page.29

%run script.py
%matplotlib

### 2.3 Python Language Basic

#### Language semantics
have something I don't know about python

python is strong typed, object have data type but variable names don't have type. All variable names are reference

isinstance function
getattr, hasattr, setattr function

!! Duck typing: Often you may not care about the type of an object but rather only whether it has certain methods or behavior.

is keyword to check if two reference refer to the same object
```python
    a is b
    a is not b
    a / b  # could lead to float type
    a // b # C-style int divide
```

#### Scalar Types
strong format(aka. output format)
- Dates and times, page.44

#### control flow
...

ch03 Built-in data structure, Functions, and Files
--------------------------------------------------------------------------------
rush a little, need to do visualization in today
### 3.1 Data Structures and Sequences
- Tuple ()
- List []
- Built-in Sequence Functions
- dict {... : ... , }
- set {..., ...}
- List, set and Dict comprehensions

feel like C++ is a well-oiled machine with elegent interface, old but durable
python is like higher abstraction, but hide way to much internal working principle. Maybe I don't know python enough
TODO: I need more practise in python and get back here

### 3.2 Functions
many concept and useful tricks in programming python
#### ...
clean_strings function in page.72 is so cool. Higher abstraction.
#### Generator

### 3.3 Files and the Operating System


ch04 Numpy Basics: Arrays and Vectorized Computation
--------------------------------------------------------------------------------
whole Numpy is about array-oritation computation
### 4.1 The NumPy ndarray: A multidimensional Array Object
this is dynamic of python
```python
    In [22]: randomInt = np.random.randn(2,3,2)

    In [23]: randomInt
    Out[23]:
    array([[[-1.70778637,  0.27578785],
            [ 0.47381311,  0.48711643],
            [-0.72034409,  1.23316204]],

            [[ 0.56443843,  0.25742822],
            [-1.45896353,  0.27529172],
            [-1.11407563, -0.6823211 ]]])

    In [24]: randomInt[1]
    Out[24]:
    array([[ 0.56443843,  0.25742822],
            [-1.45896353,  0.27529172],
            [-1.11407563, -0.6823211 ]])

        In [25]: randomInt[1] = 1

        In [26]: randomInt[1]
        Out[26]:
    array([[1., 1.],
            [1., 1.],
            [1., 1.]])
```
RandomInt[1] is 3X2 array, and RandomInt[1] = 1 is assigning every element in the array to 1
RandomInt is 2X3X2 array, and RandomInt = 1 will assign RandomInt to a reference of a int

#### ...
#### boolean Indexing
quite smart, but python actually requires more type knowledge to keep a clear programming mind
things like data[names=="Bob"]
and don't have #define function, will have a lot data liberature. Could be avoid by assgining config variable
python creates more opportunities for programer to make mistakens, but it may be convient for prototype
python do things most of time as expected, but when it doesn't, I need to know how to fix it.

provide many easy functions, need to practise and really master them
it actually benefit C/C++ programming, many choice have been build to build basic layer of scientific applicaiton

programming in C/C++ and python is not about programer time and CPU time.
when low-latency is a requirement, programming in lower language becomes a requirement.
and programer time is not marjorly effected by language, it's effected by programer's program effecience, experience in code design.
one there is a good code design and enough experience with language, development should be march ahead.
I have also seen people programing in high level language, but they are slow because know a little about language

It's good for beginner though that there are a lot of library to use, and they get to use library in smart way
python, language itself is dynamic and user-friendly(fake-frindly??), programmer need to take time to familiar their self with library

### 4.2 Universal Functions: Fast Element-wise Array Function

### 4.3 Array-Oriented Programming with Arrays
<C-l> is handy
TODO: dont' really understand np.meshgrid function, page.108
TODO: how to pic.show and continue interact with ipython shell??
TODO: how to remove all variable and restart namespace?: %reset -f command

TODO_3: page.114, dtype='<U4'

### 4.4 File Input and Output with Arrays

### 4.5 Linear Algebra

### 4.6 Pseudorandom Number Generation
distribution:
- binomial distribution
- normal(Gaussian) distribution
- beta distribution
- chi-square distribution
- gamma distribution
- uniform[0, 1) distribution

### 4.7 Example: Random Walks
import conventions
```python
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import statsmodels as sm
```
TODO: I need coding experience with Numpy
install seaborn and statsmodels with pip install

ch05 Getting Start with pandas
--------------------------------------------------------------------------------

import pandas as pd
from pandas import Series, DataFrame

### 5.1 Introduction to pandas Data Structures

### 5.2 Essential Functionlity

### 5.3 summarizing and computing descriptive statistics
reading code is more important than reading description

#### correlation and Covariance

#### Unique Values, Value Counts and Membership

### 5.4 conclusion
TODO: need more practise, so far, I haven't wroten a block useful python code

ch06 Data loading, storage and file formats
--------------------------------------------------------------------------------
### 6.1 Reading and Writing Data in Text format
I only need to write this chapter for now
install pandas in mac with
```shell
    pip install pandas
    pip install pytest
# test inside ipython with
    pd.test()
```

#### reading text files in pieces
#### writing data to text format
... skipped

ch07 Data cleaning and Preparation
--------------------------------------------------------------------------------
### 7.1 Handling Missing Data
pd.DataFrame is [colum][row]

### 7.2 Data Transformation
when you wanna get familiar with files in a fold, more is a good tool
using more *.csv, then use :n for next file, :f for filename, space for next page or next file
TODO: stock_px.csx wanna plot it
put code in .py file make it easier for me to doc and watch

!! add a new column to dataFrame, page.199
```python
    lowercased = data["food"].str.lower()
    data["animal"] = lowercased.map(meat_to_animal)
```

Interact computing do get its convenient, I start to feel it.

pd.DataFrame is different from np.ndarray
np.ndarray is like array, ndarray[1]
pd.DataFrame is like data table, DataFrame["Attri"] is a colum, it's a pd.Series
pd.Series is printed as colum, to work with DataFrame

pd.DataFrame.index is the row index
pd.DataFrame.colums is the colum index

a nice way to get random DataFrame
```python
    data = pd.DateFrame(np.random.randn(1000, 4))
    data.describe()
    col = data[2]
    col[np.abs(col)>3] # get values that exceeds 3 in one colum
```

TODO: ?? I get a data: DataFrame and wanna change values
```python
    data = pd.DateFrame(np.random.randn(1000, 4))
    col_2 = data[2] # col_2 is a Serie
    col_2[3] = 4 # get a caveat
```

DataFrame is colum first
TODO: it confused me that dataFrame[] take colume index and row boolean index
```python
    data = pd.DataFrame(np.arange(10).reshape(5, 2))
    (data>3).any(1) # get row boolean index(Series)
    (data>3).any(0) # get colum boolean index(Series)
    data[0] # get 5 elements Series
    data[(data>3).any(1)] # get filtered DataFrame
```

data initialization could be useful when I manipulate on data with this auxiliary data
```python
    df = pd.DataFrame(np.arange(5*4).reshape(5, 4))
    sampler = np.random.permutation(5) # get something like array([3, 1, 4, 2, 0])
    choices = pd.Series([5, 7, -1, 6, 4])
```

#### Computing Indicator/Dummy Variables
TODO: don't really understand

like to use DataFrame.columnName

a fancy process, page.209
```python
    all_genres = []
    for x in movies.genres:
        all_genres.extend(x.split("|")) # x is str type, x.split("|") returns a list of str
    genres = pd.unique(all_genres)
```

DataFrame[:8] is row slide

something about my_list
```python
    my_list = ["apple", "banana", "grapes", "pear"]
    for c, value in enumerate(my_list):
        print(c, value)
```

```python
    for i, gen in enumerate(movies.genres):
        indices = dummies.columns.get_indexer(gen.split("|"))
        dummies.iloc[i, indices] = 1
```

### 7.3 String Manipulation

wait, """ is not comment, it's for multiline string literal


TODO: read later
TODO: I wanna to be able to do classfication base on some basic attributes
lets say some data about students
(assuming one exam records about a class is in one .csv file)
way1, based on one attributes
way2, based on some attributes combined
way3, based on one student's several exam results across several datasets


ch08 Data Wrangling: Join, Combine, and Reshape
--------------------------------------------------------------------------------
skip for now

ch09 Plotting and Visualization
--------------------------------------------------------------------------------
### A brief matplotlib API Primer
matplotlib.pyplot
plot details
I wanna plot some special funcitons
like y=sin(x)

feels like matplotlib is take np.ndarray a lot
but a lot of time, I read pd.DataFrame

### Plorring with pandas and seaborn
insteresting tips.csv
DONE: what if i wanna find tip instance that tips["tip"] more than 5 dollors
```python
    tips[tips["tip"]>5]
```

TODO: need to know more about distribution
DONE: after using sns.distplot, don't kbcnow how to show it in ipython: plt.show(). need to checkout seaborn doc
```python
    comp1 = np.random.normal(0, 1, size=200)
    comp2 = np.random.normal(10,2, size=200)
    values = pd.Series(np.concatenate([comp1, comp2]))
    sns.distplot(values, bins=100, color="k")
```

```python
    macro = pd.read_csv("examples/macrodata.csv")
    data = macro[["cpi", "m1", "tbilrate", "unemp"]] # this is like using list as index
    trans_data = np.log(data).diff().dropna() # TODO:??
    trans_data[-5:]
    sns.regplot("m1", "unemp", data=trans_data)
```


ch10 Data Aggregation and Group Operations
--------------------------------------------------------------------------------
TODO

ch11 Time series
--------------------------------------------------------------------------------
### 11.1 Date and time data types and tools

### 11.2 Time Series Basics

### 11.3 Date Ranges, Frequencies, and Shifting

### 11.4 Time zone Handling
skipped

### 11.5 periods and period Arithmetic
skipped

### 11.6 Resampling and Frequency conversion
skipped

### 11.7 Moving window Functions
DataFrame.describe()
TODO: how lower to 2 digit behind the dot

ch12 Advanced pandas
--------------------------------------------------------------------------------

ch13 Introduction to Modeling Libraries in Python
--------------------------------------------------------------------------------

ch14 Data Analysis Examples
--------------------------------------------------------------------------------
I am still too weak to excute a python analysis job
