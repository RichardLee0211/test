# %%
"""
Main reference: https://www.deeplearningwizard.com/deep_learning/practical_pytorch/pytorch_logistic_regression/
"""

# %%
"""
Library Requirements:
  - torch==1.9.0
  - numpy==1.19.5
  - torchvision==0.10.0
"""

# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.datasets as dsets

# %%
# download MNIST data and load into tensor format
# image matrix is in first element of tuple (one element in dataset)
# label is in second element of tuple (one element in dataset)
train_data = dsets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
test_data = dsets.MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=True)

# %%
epochs = 10
batch_size = 128
learning_rate = 0.001
input_dim = 28*28
output_dim = 10

# %%
train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_data, batch_size=batch_size, shuffle=False)

# %%
class LogisticRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        output = self.linear(x)
        return output

# %%
model = LogisticRegressionModel(input_dim, output_dim)

# %%
criterion = nn.CrossEntropyLoss()

# %%
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# %%
import pdb
iter = 0
for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.view(-1, 28*28).requires_grad_()
        labels = labels

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        iter += 1

        if iter % 1000 == 0:
            correct = 0
            total = 0
            for images, labels in test_loader:
                images = images.view(-1, 28*28)
                with torch.no_grad():
                    outputs = model(images)

                predicted = torch.argmax(outputs, dim = 1)

                total += labels.size(0)

                correct += (predicted == labels).sum()

            accuracy = 100 * correct / total

            print(f'Iteration: {iter}; Loss: {loss.item()}; Accuracy: {accuracy}')

# %%
correct = 0
total = 0
iter_test = 0
for images, labels in test_loader:
    iter_test += 1
    images = images.view(-1, 28*28)
    with torch.no_grad():
        outputs = model(images)
    predicted = torch.argmax(outputs, dim = 1)

    total += labels.size(0)

    correct += (predicted == labels).sum()

accuracy = 100 * (correct.item() / total)

print(f'Final accuracy: {accuracy}')

# %%
"""
TODOs for practice:
  - Modify this to work for binary classification
    - If the label is 0, keep it the same. If the label is not 0, convert it to 1.
    - This requires re-creating an MNIST dataset instance.
  - Modify this code to use a train-dev-test split
    - Dev set can be created using a part of the training data. Make sure there is no data overlap between the splits.
    - Currently, a dev set is not used to decide whether to stop model training.
    - After every epoch, calculate accuracy on dev set and stop training when accuracy starts decreasing.
"""
