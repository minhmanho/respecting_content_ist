import torch
import torch.nn as nn
import math
import random
from components import eLayer, dLayer

class SegInNet(nn.Module):

    def __init__(self, nInputs, nOutputs):
        super(SegInNet, self).__init__()

        ## Encoder 
        self.enc1 = eLayer(nInputs,32,kernel_size=3,stride=1,padding=1,pooling=None)
        self.enc2 = eLayer(32,64,kernel_size=3,stride=1,padding=1,pooling='max')
        self.enc3 = eLayer(64,128,kernel_size=3,stride=1,padding=1,pooling='max')
        self.enc4 = eLayer(128,256,kernel_size=3,stride=1,padding=1,pooling='max')
        self.enc5 = eLayer(256,512,kernel_size=3,stride=1,padding=1,pooling='max')
        self.enc6 = eLayer(512,512,kernel_size=3,stride=1,padding=1,pooling='max')

        ## Decoder
        self.dec1 = dLayer(512,512,kernel_size=3,padding=1,pooling='nearest')
        self.dec2 = dLayer(512,256,kernel_size=3,padding=1,pooling='nearest')
        self.dec3 = dLayer(256,128,kernel_size=3,padding=1,pooling='nearest')
        self.dec4 = dLayer(128,64,kernel_size=3,padding=1,pooling='nearest')
        self.dec5 = dLayer(64,32,kernel_size=3,padding=1,pooling='nearest')

        self.final_conv = nn.Conv2d(32,nOutputs,3,1,1,bias=True)
        self.final_activation = nn.Tanh()

        # set connect weights
        self.connect_weights = [1.0, 1.0, 1.0, 1.0, 1.0]
        print('SegInNet')


    def forward(self, I, R):
        sources = []
        X = torch.cat([I, R], 1)

        for i in range(6):
            # I
            X = getattr(self, 'enc{:d}'.format(i + 1))(X)
            sources.append(X)


        ## Decoder
        X = sources.pop()

        for i in range(5):
            # print(X.size())
            X = getattr(self, 'dec{:d}'.format(i + 1))(X, sources[-i-1], connect_weight=self.connect_weights[i])

        X = self.final_conv(X)

        return self.final_activation(X)
