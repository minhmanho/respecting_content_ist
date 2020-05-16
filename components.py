import torch
import torch.nn as nn

def get_subsampler(_name, nchannels):
    return {
        "down_max": nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
        "down_avg": nn.AvgPool2d(kernel_size=3, stride=2, padding=1),
        "down_conv": nn.Conv2d(nchannels, nchannels, kernel_size=3, stride=2, padding=1, bias=True),
        "up_bilinear": nn.Upsample(scale_factor=2, mode='bilinear'),
        "up_nearest": nn.Upsample(scale_factor=2, mode='nearest'),
        "up_conv": nn.ConvTranspose2d(nchannels, nchannels, kernel_size=3, stride=2, padding=1, output_padding=1, bias=True),
    }[_name]

class baseLayer(nn.Module):
    def __init__(self, nInputs, nOutputs, kernel_size=3, stride=1, padding=1, pooling=None):
        super(baseLayer, self).__init__()
        self.conv1 = nn.Conv2d(nInputs, nOutputs, kernel_size, stride, padding, bias=True)
        self.conv2 = nn.Conv2d(nOutputs, nOutputs, kernel_size, stride, padding, bias=True)
        self.ins1 = nn.InstanceNorm2d(nOutputs, affine=True)
        self.ins2 = nn.InstanceNorm2d(nOutputs, affine=True)
        self.relu = nn.LeakyReLU(0.1,True)
    
    def forward(self):
        pass

class eLayer(baseLayer):
    def __init__(self, nInputs, nOutputs, kernel_size=3, stride=1, padding=1, pooling=None):
        super().__init__(nInputs, nOutputs, kernel_size, stride, padding, pooling)
        self.pool = get_subsampler("down_" + pooling, nInputs) if pooling is not None else None

    def forward(self, _input):
        X = _input
        if self.pool is not None:
            X = self.pool(X)
        X = self.relu(self.ins1(self.conv1(X)))
        X = self.relu(self.ins2(self.conv2(X)))
        return X

class dLayer(baseLayer):
    def __init__(self, nInputs, nOutputs, kernel_size=3, stride=1, padding=1, pooling=None):
        super().__init__(nInputs, nOutputs, kernel_size, stride, padding, pooling)
        self.upsample = get_subsampler("up_" + pooling, nInputs) if pooling is not None else None

    def forward(self, _input, skip_feat, connect_weight=1.0):
        X = _input
        if self.upsample is not None:
            X = self.upsample(X)
        X = self.relu(self.ins1(self.conv1(X)))
        X = X + connect_weight*skip_feat
        X = self.relu(self.ins2(self.conv2(X)))
        return X
