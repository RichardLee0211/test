trying to download pip with get-pip.py provided by
https://pip.readthedocs.io/en/stable/installing/
but get errors
and then try
```bash
sudo python get-pip.py # success
```
```bash
sudo pip install "ipython[notebook]" --upgrade --ignore-installed six
OSError: [Errno 1] Operation not permitted:
'/System/Library/Frameworks/Python.framework/Versions/2.7/share'
```
solution may be here:
https://stackoverflow.com/questions/33004708/osx-el-capitan-sudo-pip-install-oserror-errno-1-operation-not-permitted

MacOS seems to refuse to install ipython[notebook] using
```bash
sudo pip install "ipython[notebook]" --upgrade --ignore-installed six
```

and this does successful
```bash
sudo pip3 install "ipython[notebook]" --upgrade --ignore-installed six
```

set up a vitual environment for python using tutorial in:
https://packaging.python.org/tutorials/installing-packages/

I think I start to love ipython, with great auto-completion feature
and from http://docs.python-guide.org/en/latest/dev/virtualenvs/, python 2 will
retire in 2 years.
