https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

didn't use anaconda for this time
install torch torchvision
```shell
    ➜  testPyTorch git:(master) ✗ pip3 install torch torchvision
    Collecting torch
    Downloading https://files.pythonhosted.org/packages/0f/27/36b5f7acd661b2a435c7c9283dd4ddeac9a4c7fc0e328efaddeae2ffaf68/torch-1.3.0-cp37-none-macosx_10_9_x86_64.whl (71.1MB)
    100% |████████████████████████████████| 71.1MB 472kB/s
    Collecting torchvision
    Downloading https://files.pythonhosted.org/packages/97/4d/75e430a8ce3e4707a2de566229c1f5295dab99040b72f5b83f29cc196297/torchvision-0.4.1-cp37-cp37m-macosx_10_9_x86_64.whl (631kB)
    100% |████████████████████████████████| 634kB 2.1MB/s
    Collecting numpy (from torch)
    Downloading https://files.pythonhosted.org/packages/b4/e8/5ececadd9cc220bb783b4ce6ffaa9266925d37ed41237bc23bc530ab4f3d/numpy-1.17.2-cp37-cp37m-macosx_10_6_intel.whl (15.0MB)
    100% |████████████████████████████████| 15.0MB 1.4MB/s
    Collecting pillow>=4.1.1 (from torchvision)
    Downloading https://files.pythonhosted.org/packages/a4/92/801710e21ede5f583c6bde61b25baa46ed16d9d77d74935e11b9a801cdd7/Pillow-6.2.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (3.9MB)
    100% |████████████████████████████████| 3.9MB 1.9MB/s
    Requirement already satisfied: six in /usr/local/lib/python3.7/site-packages (from torchvision) (1.12.0)
    Installing collected packages: numpy, torch, pillow, torchvision
    Successfully installed numpy-1.17.2 pillow-6.2.0 torch-1.3.0 torchvision-0.4.1
```

basic operations
```python
    from __future__ import print_function
    import torch
    x = torch.empty(5, 3)
    print(x)
    x = torch.rand(5, 3)
    print(x)
    x = torch.zeros(5, 3, dtype=torch.long)
    print(x)
    x = torch.tensor([5.5, 3])
    print(x)
    x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
    print(x)
    x = torch.randn_like(x, dtype=torch.float)    # override dtype!
    print(x)                                      # result has the same size
    print(x.size()) # torch.Size is a tuple
    y = torch.rand(5, 3)
    print(x + y)
    print(torch.add(x, y))
    result = torch.empty(5, 3)
    torch.add(x, y, out=result)
    print(result)
    # adds x to y
    y.add_(x)
    print(y)
    print(x[:, 1])
    x = torch.randn(4, 4)
    y = x.view(16)
    z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
    print(x.size(), y.size(), z.size())
    x = torch.randn(1)
    print(x)
    print(x.item())
```

NumPy Bridge
```python
    a = torch.ones(5)
    print(a)
    b = a.numpy()
    print(b)
    a.add_(1)
    print(a)
    print(b)    # a and b point to the same data structure

    import numpy as np
    a = np.ones(5)
    b = torch.from_numpy(a)
    np.add(a, 1, out=a)
    print(a)
    print(b)    # a and b point to the same data structure
```

CUDA Tensors
```python3
    # let us run this cell only if CUDA is available
    # We will use ``torch.device`` objects to move tensors in and out of GPU
    if torch.cuda.is_available():
        device = torch.device("cuda")          # a CUDA device object
        y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
        x = x.to(device)                       # or just use strings ``.to("cuda")``
        z = x + y
        print(z)
        print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!
```

Tensor
```python3
    import torch
    x = torch.ones(2, 2, requires_grad=True)
    print(x)
    y = x + 2
    print(y)
    print(y.grad_fn)
    z = y * y * 3       # this is not matrix multiply
    out = z.mean()
    print(z, out)

    a = torch.randn(2, 2)
    a = ((a * 3) / (a - 1))
    print(a.requires_grad) # False
    a.requires_grad_(True)
    print(a.requires_grad) # True
    b = (a * a).sum()
    print(b.grad_fn) # <SumBackward0 object at <addr>>
```

TODO: not completely understand this
from: https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
```python3
    x = torch.randn(3, requires_grad=True)

    y = x * 2
    while y.data.norm() < 1000:
        y = y * 2

    print(y)

    v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
    y.backward(v)

    print(x.grad)
```

Network
```python3
    import torch
    import torch.nn as nn
    import torch.nn.functional as F


    class Net(nn.Module):

        def __init__(self):
            super(Net, self).__init__()
            # 1 input image channel, 6 output channels, 3x3 square convolution
            # kernel
            self.conv1 = nn.Conv2d(1, 6, 3)
            self.conv2 = nn.Conv2d(6, 16, 3)
            # an affine operation: y = Wx + b
            self.fc1 = nn.Linear(16 * 6 * 6, 120)  # 6*6 from image dimension
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            # Max pooling over a (2, 2) window
            x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
            # If the size is a square you can only specify a single number
            x = F.max_pool2d(F.relu(self.conv2(x)), 2)
            x = x.view(-1, self.num_flat_features(x))
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

        def num_flat_features(self, x):
            size = x.size()[1:]  # all dimensions except the batch dimension
            num_features = 1
            for s in size:
                num_features *= s
            return num_features


    net = Net()
    print(net)

    params = list(net.parameters())
    print(len(params))
    print(params[0].size())  # conv1's .weight

    input = torch.randn(1, 1, 32, 32)
    out = net(input)
    print(out)

    net.zero_grad()
    out.backward(torch.randn(1, 10))

    # Loss Function
    output = net(input)
    target = torch.randn(10)  # a dummy target, for example
    target = target.view(1, -1)  # make it the same shape as output
    criterion = nn.MSELoss()

    loss = criterion(output, target)
    print(loss)

    # Backprop
    net.zero_grad()     # zeroes the gradient buffers of all parameters

    print('conv1.bias.grad before backward')
    print(net.conv1.bias.grad)

    loss.backward()

    print('conv1.bias.grad after backward')
    print(net.conv1.bias.grad)

    # update the weights
    learning_rate = 0.01
    for f in net.parameters():
        f.data.sub_(f.grad.data * learning_rate)

    # update the weights
    import torch.optim as optim

    # create your optimizer
    optimizer = optim.SGD(net.parameters(), lr=0.01)

    # in your training loop:
    optimizer.zero_grad()   # zero the gradient buffers
    output = net(input)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()    # Does the update
```

training an image classifier
```python3
    import torch
    import torchvision
    import torchvision.transforms as transforms

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                              shuffle=True, num_workers=2)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                             shuffle=False, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    # define a CNN
    import torch.nn as nn
    import torch.nn.functional as F


    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x


    net = Net()

    # define a Loss function and optimizer
    import torch.optim as optim

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    # train the network
    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    # save the model
    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)
```

#### review it
```shell
  # ipython and conda env
  conda activate nlp-hw1
  ipython
  import sys; print(sys.version);
  ## since conda creat virtual env by prepending entries in $PATH, I need install
  ## ipython in the new envrionment
  conda install ipython
```

#### conda manage environments
from: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

```environment.yml
  name: stats2
  channels:
    - javascript
  dependencies:
    - python=3.6   # or 2.7
    - bokeh=0.9.2
    - numpy=1.9.*
    - nodejs=0.10.*
    - flask
    - pip:
      - Flask-Testing
```

```shell
  # it has a ~/.condarc file
  conda create --name myenv
  conda install -n myenv python=3.6 scipy=0.15.0
  conda env create -f environment.yml
  ## list
  conda env list
  conda info
  conda info --envs
  ## activate
  conda activate myenv
  ## update packages
  conda env update --prefix ./env --file environment.yml --prune
  ## clone
  conda create --name myclone --clone myenv
  conda info --envs
  ## export packages list
  conda list --explicit   # list all the packages installed in this env
  conda list --explicit > spec-file.txt
  conda create --name myenv --file spec-file.txt
  conda install --name myenv --file spec-file.txt
  ## deactivate
  conda deactivate
  ## export env
  conda env export > environment.yml
  ## remove env
  conda env remove --name myenv
  conda remove --name myenv --all
```

```shell
  conda install torch=1.9.0

  PackagesNotFoundError: The following packages are not available from current channels:

    - torch=1.9.0
  ...

  # using pip then
  conda install -n myenv pip
  conda activate myenv
  pip install -r requirement.txt
  conda install ipython
```

usint test20210916
