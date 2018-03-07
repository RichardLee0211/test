import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# url = "http://donnees.ville.montreal.qc.ca/storage/f/ \
        # 2014-01-20T20%3A48%3A50.296Z/2013.csv"
url = "../data/world-happiness-report/2015.csv"

df = pd.read_csv(url) # , index_col='Date', parse_dates=True, dayfirst=True)

df.head(2)
