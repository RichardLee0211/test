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

ch03 Built-in data structure, Functions, and Files
--------------------------------------------------------------------------------
