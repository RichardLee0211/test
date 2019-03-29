#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("random2.clang++.csv", skiprows=[0], header=None)
# this plot don't help to tell ture generator from pseudo one
df.plot(style="ko")
