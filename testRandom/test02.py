#! python3
# I doubt the use of shebang line, since I would run it in different system, FreeBSD or Linux distro
#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./RandomData/random_2.clang++.csv", skiprows=[0], header=None)
    print("something")
    # this plot don't help to tell ture generator from pseudo one
    # df.plot(style="ko")

    # %matplotlib inline in ipython fails
    # %matplotlib osx
    # weird, some times plt.show() shows the pic in ipython, sometimes it doesn't

    # df.plot.line()
    plt.plot(df)
    plt.show()
