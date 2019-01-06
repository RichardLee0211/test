this question is always around, hack it

find this website: https://www.random.org/

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

Practical Statistics for data Scientists
================================================================================
put it away as it demo concept with R language, a language I am not ready to get into
need to understand to basic statistics concepts, leaving R language part along, learn panda

ch01 Exploratory Data Analysis
--------------------------------------------------------------------------------
talked a little about data type

### rectangular data
- rectangular data
- time series data
- spatial data
- graph(or network) data

### Estimates of Location
- mean("x-bar")
- weighted mean
- Median
- weighted median
- Trimmed mean: can be thought of a compromise between the median and the mean
- robust
- outlier

### Estimates of Variability
- Deviations: difference from mean, errors
- Mean absolute deviation: I1-norm, Manhattan norm
- Variance: mean-squared-error, s**2
- Standard deviation: the square root of the variance, I2-norm, Euclidean norm, s
- Median absolute deviation from the median
- Range
- order statustics
- Percentile
- Interquartile range

### exploring the data distribution
- boxplot
- Frequency table
- Histogram
- Density plot

### exploring Binary and Categorical Data
- mode
- expected value
- bar charts
- pie charts

TODO: [a lesson on misleading graphs](http://passyworldofmathematics.com/misleading-graphs/)

### correlation
- Correlation coefficient
- Correlation matrix
- Scatterplot

### Exploring Two or More Variables
- contingency tables
- Hexagonal binning
- Coutour plots
- violin plots

univariate analysis
bivariate analysis

download some csv files, like the old time. But this time, I am not focus on big data tech.
I am on statistic method and data mining algorithms
using python3 and panda, see what I can do
R is supported by open source community, great. Although I don't using it for now

TODO_3: may be look into this [magic graph](https://en.wikipedia.org/wiki/Mandelbrot_set)
, after I get excellent drawing skills

TODO: need to learn to do EDA in python3, should be easy


ch02 Data and Sampling Distributions
--------------------------------------------------------------------------------
TODO: read later
### Random Sampling and Sample Bias


ch03 Statistical Experiments and Significance Testing
--------------------------------------------------------------------------------
is attractive for me

### A/B testing
- treatment
- treatment group
- control group
- Randomization
- subjects
- test statistic

### Hypothesis Tests
- Null hypothesis
- Alternative Hypothesis
- One-way test
- Two-way test

### Resampling
- Permutation test
- With or without replacement
this is could be very useful for fight against randomness
TODO: need to know how to do it in Python

#### Example: Web Stickiness
I am great that they have a example to explain permutation test

### Statistical Significance and P-values
- p-value
- Alpha
TODO: read in more detail with task
- Type 1 error
- Type 2 error

### t-Tests
- test statistic
- t-statistic
- t-distribution

TODO: to be continue, need build python3 statical skills

ch04 regression and prediction
--------------------------------------------------------------------------------

ch06 Statistical Machine Learning
--------------------------------------------------------------------------------

ch07 Unsuparvised Learning
--------------------------------------------------------------------------------
