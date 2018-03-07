import numpy as np

def mull(n):
    return np.array([[(i+1)*(j+1) for i in range(n)] for j in range(n)])

import os
mypid = os.getpid()

if __name__ == "__main__":
    # mull(3)
    # mypid = os.getpid()
    import urllib, zipfile
    url = 'http://ipython.rossant.net/'
    filename = 'cities.zip'
    downloaded = urllib.request(url + filename)
    with open(filename, 'wb') as f:
        f.write(downloaded.read())
    with zipfile.ZipFile(filename) as myzip:
        myzip.extractall('../data/')
