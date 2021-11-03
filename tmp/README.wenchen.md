conda create -n transform_test python=3.6
# pip install ipython torch
conda install ipython
pip install  numpy matplotlib spacy torchtext seaborn


# this thing is weird
# http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl

Extended Neural GPU, ByteNet and ConvS2S

TODO: later, more paper reading
- encoder-decoder structure [(cite)](https://arxiv.org/abs/1409.0473).
- auto-regressive [(cite)](https://arxiv.org/abs/1308.0850),
- residual connection [(cite)](https://arxiv.org/abs/1512.03385)
- layer normalization [(cite)](https://arxiv.org/abs/1607.06450)
- dropout [(cite)](http://jmlr.org/papers/v15/srivastava14a.html)
- additive attention [(cite)](https://arxiv.org/abs/1409.0473),

torch.__version__


##### class Batch code breakdown
type(tmp) # torch.tensor
tmp.shape # (100, 10)
tmp.unsqueeze(-2) # add another dimansion of 1 at -2
tmp.shape # (100, 1, 10)

tmp2 = tensor != 0 # tmp2 is tensor as well

            self.trg = trg[:, :-1]  # remove tail
            self.trg_y = trg[:, 1:] # remove head



### yield
from: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
so many upvotes for this
```python
    ## iterables:
    mylist = [x*x for x in range(3)]
    for i in mylist:
       print(i)

    ## use only once, and only store one element in memory at one time
    mygenerator = (x*x for x in range(3))
    for i in mygenerator:
       print(i)

    ## build a generator
    def create_generator():
       mylist = range(3)
       for i in mylist:
           yield i*i

    mygenerator = create_generator() # create a generator
    print(mygenerator) # mygenerator is an generator object!
    for i in mygenerator:
        print(i)
```
