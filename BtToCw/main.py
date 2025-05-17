import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import DataLoader
from utils import *
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


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
        



# torch.manual_seed(12)
# t = torch.randn(1, 5, 5)
# t = torch.FloatTensor(2, 4).fill()
# t = torch.uniform(0, 1)
# t.normal_(0, 1)
# t = torch.Tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
# d = t.view(3, 3, 3)
# t = torch.arange(32).view(8, 2, 2)

a = torch.arange(12)

print(a)
