#An Optimized Generative Adversarial Network Training Model for Generating Audio Encoded MP4 Video Files
import argparse
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.data import DataLoader
import torch.nn as nn
from torchvision.datasets import MNIST, FashionMNIST
from torch.autograd import Variable
import torchvision.transforms as transforms
import torchvision.models as models
import os
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.utils.data import DataLoader
import numpy as np
import time
import random
import torch.utils.data as data
import torchvision.utils as vutils
from torch.utils.data import DataLoader

import torchvision
import numpy as np
import cv2
import os
import random
import time
import torch
import numpy as np

# Define the model class
class Net(nn.Module):
    def __init__(self, n_in, n_out, n_g):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(n_in, n_out, 3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(n_out)
        self.conv2 = nn.Conv2d(n_out, n_out, 3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(n_out)
        self.conv3 = nn.Conv2d(n_out, n_g, 1, bias=True)
        self.bn3 = nn.BatchNorm2d(n_g)
        self.lrelu = nn.LeakyReLU(0.2, inplace=True)
        self.lrelu2 = nn.LeakyReLU(0.2, inplace=True)

        self.pool = nn.MaxPool2d(3, stride=2)

    def forward(self, x):
        x = self.bn1(self.conv1(x))
        x = self.bn2(self.conv2(x))
        x = self.bn3(self.conv3(x))

        x = F.relu(x)
        x = self.lrelu(x)

        x = self.pool(x)
        x = self.lrelu2(x)

        return x


# Define the discriminator class
class Discriminator(nn.Module):
    def __init__(self, n_out, n_g):
        super(Discriminator, self).__init__()

        self.conv1 = nn.Conv2d(3, n_out, 3, bias=False)
        self.bn1 = nn.BatchNorm2d(n_out)
        self.conv2 = nn.Conv2d(n_out, n_out, 3, bias=False)
        self.bn2 = nn.BatchNorm2d(n_out)
        self.conv3 = nn.Conv2d(n_out, n_g, 1, bias=True)
        self.bn3 = nn.BatchNorm2d(n_g)
        self.lrelu = nn.LeakyReLU(0.2, inplace=True)
        self.lrelu2 = nn.LeakyReLU(0.2, inplace=True)
        self.dropout = nn.Dropout2d()

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.conv3(x)
        x = self.bn3(x)
        x = F.relu(x)
        x = self.lrelu(x)

        x = self.dropout(x)

        x = self.avgpool(x)
        x = x.view(-1, x.size(-1))

        return x


# define the generator class
class Generator(nn.Module):
    def __init__(self, n_out, n_g):
        super(Generator, self).__init__()

        self.conv1 = nn.Conv2d(3, n_out, 3, bias=False)
        self.bn1 = nn.BatchNorm2d(n_out)
        self.conv2 = nn.Conv2d(n_out, n_out, 3, bias=False)
        self.bn2 = nn.BatchNorm2d(n_out)
        self.conv3 = nn.Conv2d(n_out, n_g, 1, bias=True)
        self.bn3 = nn.BatchNorm2d(n_g)
        self.lrelu = nn.LeakyReLU(0.2, inplace=True)
        self.lrelu2 = nn.LeakyReLU(0.2, inplace=True)
        self.dropout = nn.Dropout2d()

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.conv3(x)
        x = self.bn3(x)
        x = F.relu(x)
        x = self.lrelu(x)

        x = self.dropout(x)

        x = self.avgpool(x)
        x = x.view(-1, x.size(-1))

        return x


# Define the optimizer class
class Optimizer(nn.Module):
    def __init__(self, params):
        super(Optimizer, self).__init__()

        self.wd = params['wd']
        self.optimizer = torch.optim.Adam(params['vars'],
                                          lr=params['lr'], betas=(0.0, 0.9))

    def update(self, m):
        self.optimizer.zero_grad()
        loss = self.fn(m)
        loss.backward()
        self.optimizer.step()

    def fn(self, m):
        m.apply(self.wd)
        m.conv1.weight.data.clamp_(-0.05, 0.05)
        m.conv1.bias.clamp_(-0.05, 0.05)
        m.conv2.weight.data.clamp_(-0.05, 0.05)
        m.conv2.bias.clamp_(-0.05, 0.05)
        m.conv3.weight.data.clamp_(-0.05, 0.05)
        m.conv3.bias.clamp_(-0.05, 0.05)
        return F.cross_entropy(m.conv1, m.conv2)
