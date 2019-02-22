Practical Statistics for data Scientists, 50 essential concept
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
### Random Sampling and Sample Bias
- sample
- pipulation
- N(n)
- Random sampling
- stratified sampling
- Simple random sample
- sample bias

random-ful sample is better than large sample with bias

### Selection Bias
- dias
- data snooping
- Vast search effect
TODO: read [this](http://systemtradersuccess.com/fooled-by-randomness-through-selection-bias/)

### samping distribution of a statistic
- Sample Statistic
- Data distribution
- Sampling distribution
- Central limit theorem
- Standard error

TODO: figure 2-6, how do U mean a sample of 5 values??
TODO: further reading

### the bootstrap
- bootstrap sample
- resampling

I like it that wikipedia provide "download as PDF" option, much cooler typeset
TODO: need to a concrete example of how to bootstrap
TODO: check resample() scikit-learn function

### confidence intervals
- confidence level
- interval endpoints

when draw a random resample of size n with replacement from the sample of size n,
it means draw one data by random and place it back

### normal distribution
- error
- standardize
- z-score
- standard normal
- QQ-plot

TODO: standard Normal and QQ-plot in python
TODO: standard distribution formula

### long-tailed distribution
- tail
- skew

TODO: black swan theory

### Student's t-Distribution
- n
- Degrees of freedom

TODO: distribution of sample means, normal distribution or t-Distribution ??
TODO: [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)

### Binomial Distribution
- trial
- Success
- Binomial
- Binomial trial
- Binomial distribution

### poisson and related distributions
- lambda
- Poisson ditribution
- Exponential distribution
- weibull distribution

there are a lot other useful distributions, I don't where they come from, why do they have magic e in their formula

TODO: I still don't know how to do bootstrap in python


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

ch05 classification
--------------------------------------------------------------------------------

### Naive Bayes

ch06 Statistical Machine Learning
--------------------------------------------------------------------------------

### K-Nearest Neighbors

I got a KNN assignment in HPC

right now, I am so excited to see the number, enum(state of a abbtirbution), location, time etc

great, a small sample

ch07 Unsuparvised Learning
--------------------------------------------------------------------------------
