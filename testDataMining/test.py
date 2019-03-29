import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pd.__version__

# this command could have changed
# %matplotlib inline

sales = pd.read_csv("sample-salesv2.csv", parse_dates= ["date"])
# sales.head()

# to see the count, mean, std, min, 25%, 50%, 75%, max of each column
# sales.describe()

# describe numbers
# sales["unit price"].describe()

# describe Strings
# sales["category"].describe()
# sales["category"].unique()
