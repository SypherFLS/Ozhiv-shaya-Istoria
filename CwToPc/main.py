import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import DataLoader
from utils import *
import matplotlib.pyplot as plt
from random import randint


# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))

# def deriy_sigmoid(x):
#     fx = sigmoid(x)
#     return fx * (1 - fx)

# def mse_loss(y_true, y_pred):
#     return ((y_true - y_pred) ** 2).mean()

# class NeuralNetwork_1:

#     def __init__(self):
#         torch.manual_seed(12)


# # 1st
# N = 5
# b = 3

# x1 = torch.rand(N)
# x2 = x1 + torch.randint(1, 10, [N]) / 10 
# c1 = torch.vstack([x1, x2]).mT

# x1 = torch.rand(N)
# x2 = x1 - torch.randint(1, 10, [N]) / 10 
# c2 = torch.vstack([x1, x2]).mT

# f = [0,1]

# w = torch.FloatTensor([-0.5, 0.5])

# for i in range(N):
#     x = c1[:][i]
#     y = torch.dot(w, x)
#     if y >= 0:
#         print("c1")
#     else:
#         print("c2")

# plt.scatter(c1[:, 0], c1[:,1], s=10, c = 'green')
# plt.scatter(c2[:, 0], c2[:,1], s=10, c = 'red')
# plt.plot(f)
# plt.grid()
# plt.show()


# back propogation training

def act(z):
    return torch.tanh(z)

def df(z):
    s = act(z)
    return 1 - s * s

def go_forward(x_inp, w1, w2):
    z1 = torch.mv(w1[:, :3], x_inp)+w1[:, 3]
    s1 = act(z1)

    z2 = torch.dot(w2[:2], s1) + w2[2]
    y = act(z2)
    return y, z1, s1, z2

torch.manual_seed(1)

W1 = torch.rand(8).view(2, 4) - 0.5
W2 = torch.rand(3) - 0.5

x_train = torch.FloatTensor([(-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)])

y_train = torch.FloatTensor([-1, 1, -1, 1, -1, 1, -1])

lmd = 0.05
N = 1000
total = len(y_train)

for _ in range(N):
    k = randint(0, total-1)
    x = x_train[k]
    y, z1, s1, out = go_forward(x, W1, W2)
    e = y - y_train[k]
    delta = e*df(out)
    delta2 = W2[:2] * delta * df(z1)

    W2[:2] = W2[:2] - lmd * delta * s1
    W2[2] = W2[2] - lmd * delta

    W1[0, :3] = W1[0, :3] - lmd * delta2[0] * x
    W1[1, :3] = W1[1, :3] - lmd * delta2[1] * x

    W1[0, :3] = W1[0, :3] - lmd * delta2[0] 
    W1[1, :3] = W1[1, :3] - lmd * delta2[1] 

for x, d in zip(x_train, y_train):
    y, z1, s1, out = go_forward(x, W1, W2)
    print(f"Output = {y} => {d}")

print(W1)
print(W2)