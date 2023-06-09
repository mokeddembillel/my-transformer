import torch 
import numpy as np 
import pandas as pd 
import pickle
import math
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, sentence_length=5, imbd_size=512, hidden_size=64, num_heads=8):
        
        super().__init__()


        self.imbd_size = imbd_size
        self.hidden_size = hidden_size
        self.sentence_length = sentence_length
        self.num_heads = num_heads

        self.W_q = torch.rand((self.num_heads, self.imbd_size, self.hidden_size))
        self.W_k = torch.rand((self.num_heads, self.imbd_size, self.hidden_size))
        self.W_v = torch.rand((self.num_heads, self.imbd_size, self.hidden_size))
        self.W_0 = torch.rand((self.imbd_size, self.hidden_size))


    
    def forward(self, X): # X-> (sentence_length, imbd_size)
        
        X = X.repeat(self.num_heads) # X-> (num_heads, sentence_length, imbd_size)

        q = torch.bmm(X, self.W_q) # (num_heads, sentence_length, hidden_size)
        k = torch.bmm(X, self.W_k) # (num_heads, sentence_length, hidden_size)
        v = torch.bmm(X, self.W_v) # (num_heads, sentence_length, hidden_size)

        r1 = torch.softmax(torch.bmm(q, k.transpose(1,2)) / math.sqrt(self.hidden_size), dim=2) # (num_heads, sentence_length, sentence_length)
        r2 = torch.bmm(r1, v) # (num_heads, sentence_length, hidden_size)

        Z = torch.matmul(r2.permute((1, 0, 2)).reshape(self.sentence_length, self.num_heads * self.hidden_size), self.W_0)  # (sentence_length, imbd_size)


        return Z


if __name__ == "__main__":
    pass