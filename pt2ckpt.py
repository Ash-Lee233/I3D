
"""
Convert torch weight file to ckpt file
"""

import argparse

import torch
from mindspore import Tensor, save_checkpoint

mindspore_parameter_name = [
    'Conv3d_1a_7x7.weight',
    'Conv3d_1a_7x7_bn.bn2d.moving_mean',
    'Conv3d_1a_7x7_bn.bn2d.moving_variance',
    'Conv3d_1a_7x7_bn.bn2d.gamma',
    'Conv3d_1a_7x7_bn.bn2d.beta',
    'Conv3d_2b_1x1.weight',
    'Conv3d_2b_1x1_bn.bn2d.moving_mean',
    'Conv3d_2b_1x1_bn.bn2d.moving_variance',
    'Conv3d_2b_1x1_bn.bn2d.gamma',
    'Conv3d_2b_1x1_bn.bn2d.beta',
    'Conv3d_2c_3x3.weight',
    'Conv3d_2c_3x3_bn.bn2d.moving_mean',
    'Conv3d_2c_3x3_bn.bn2d.moving_variance',
    'Conv3d_2c_3x3_bn.bn2d.gamma',
    'Conv3d_2c_3x3_bn.bn2d.beta',
    'Mixed_3b_b0.conv3d.weight',
    'Mixed_3b_b0.bn.bn2d.moving_mean',
    'Mixed_3b_b0.bn.bn2d.moving_variance',
    'Mixed_3b_b0.bn.bn2d.gamma',
    'Mixed_3b_b0.bn.bn2d.beta',
    'Mixed_3b_b1a.conv3d.weight',
    'Mixed_3b_b1a.bn.bn2d.moving_mean',
    'Mixed_3b_b1a.bn.bn2d.moving_variance',
    'Mixed_3b_b1a.bn.bn2d.gamma',
    'Mixed_3b_b1a.bn.bn2d.beta',
    'Mixed_3b_b1b.conv3d.weight',
    'Mixed_3b_b1b.bn.bn2d.moving_mean',
    'Mixed_3b_b1b.bn.bn2d.moving_variance',
    'Mixed_3b_b1b.bn.bn2d.gamma',
    'Mixed_3b_b1b.bn.bn2d.beta',
    'Mixed_3b_b2a.conv3d.weight',
    'Mixed_3b_b2a.bn.bn2d.moving_mean',
    'Mixed_3b_b2a.bn.bn2d.moving_variance',
    'Mixed_3b_b2a.bn.bn2d.gamma',
    'Mixed_3b_b2a.bn.bn2d.beta',
    'Mixed_3b_b2b.conv3d.weight',
    'Mixed_3b_b2b.bn.bn2d.moving_mean',
    'Mixed_3b_b2b.bn.bn2d.moving_variance',
    'Mixed_3b_b2b.bn.bn2d.gamma',
    'Mixed_3b_b2b.bn.bn2d.beta',
    'Mixed_3b_b3b.conv3d.weight',
    'Mixed_3b_b3b.bn.bn2d.moving_mean',
    'Mixed_3b_b3b.bn.bn2d.moving_variance',
    'Mixed_3b_b3b.bn.bn2d.gamma',
    'Mixed_3b_b3b.bn.bn2d.beta',
    'Mixed_3c_b0.conv3d.weight',
    'Mixed_3c_b0.bn.bn2d.moving_mean',
    'Mixed_3c_b0.bn.bn2d.moving_variance',
    'Mixed_3c_b0.bn.bn2d.gamma',
    'Mixed_3c_b0.bn.bn2d.beta',
    'Mixed_3c_b1a.conv3d.weight',
    'Mixed_3c_b1a.bn.bn2d.moving_mean',
    'Mixed_3c_b1a.bn.bn2d.moving_variance',
    'Mixed_3c_b1a.bn.bn2d.gamma',
    'Mixed_3c_b1a.bn.bn2d.beta',
    'Mixed_3c_b1b.conv3d.weight',
    'Mixed_3c_b1b.bn.bn2d.moving_mean',
    'Mixed_3c_b1b.bn.bn2d.moving_variance',
    'Mixed_3c_b1b.bn.bn2d.gamma',
    'Mixed_3c_b1b.bn.bn2d.beta',
    'Mixed_3c_b2a.conv3d.weight',
    'Mixed_3c_b2a.bn.bn2d.moving_mean',
    'Mixed_3c_b2a.bn.bn2d.moving_variance',
    'Mixed_3c_b2a.bn.bn2d.gamma',
    'Mixed_3c_b2a.bn.bn2d.beta',
    'Mixed_3c_b2b.conv3d.weight',
    'Mixed_3c_b2b.bn.bn2d.moving_mean',
    'Mixed_3c_b2b.bn.bn2d.moving_variance',
    'Mixed_3c_b2b.bn.bn2d.gamma',
    'Mixed_3c_b2b.bn.bn2d.beta',
    'Mixed_3c_b3b.conv3d.weight',
    'Mixed_3c_b3b.bn.bn2d.moving_mean',
    'Mixed_3c_b3b.bn.bn2d.moving_variance',
    'Mixed_3c_b3b.bn.bn2d.gamma',
    'Mixed_3c_b3b.bn.bn2d.beta',
    'Mixed_4b_b0.conv3d.weight',
    'Mixed_4b_b0.bn.bn2d.moving_mean',
    'Mixed_4b_b0.bn.bn2d.moving_variance',
    'Mixed_4b_b0.bn.bn2d.gamma',
    'Mixed_4b_b0.bn.bn2d.beta',
    'Mixed_4b_b1a.conv3d.weight',
    'Mixed_4b_b1a.bn.bn2d.moving_mean',
    'Mixed_4b_b1a.bn.bn2d.moving_variance',
    'Mixed_4b_b1a.bn.bn2d.gamma',
    'Mixed_4b_b1a.bn.bn2d.beta',
    'Mixed_4b_b1b.conv3d.weight',
    'Mixed_4b_b1b.bn.bn2d.moving_mean',
    'Mixed_4b_b1b.bn.bn2d.moving_variance',
    'Mixed_4b_b1b.bn.bn2d.gamma',
    'Mixed_4b_b1b.bn.bn2d.beta',
    'Mixed_4b_b2a.conv3d.weight',
    'Mixed_4b_b2a.bn.bn2d.moving_mean',
    'Mixed_4b_b2a.bn.bn2d.moving_variance',
    'Mixed_4b_b2a.bn.bn2d.gamma',
    'Mixed_4b_b2a.bn.bn2d.beta',
    'Mixed_4b_b2b.conv3d.weight',
    'Mixed_4b_b2b.bn.bn2d.moving_mean',
    'Mixed_4b_b2b.bn.bn2d.moving_variance',
    'Mixed_4b_b2b.bn.bn2d.gamma',
    'Mixed_4b_b2b.bn.bn2d.beta',
    'Mixed_4b_b3b.conv3d.weight',
    'Mixed_4b_b3b.bn.bn2d.moving_mean',
    'Mixed_4b_b3b.bn.bn2d.moving_variance',
    'Mixed_4b_b3b.bn.bn2d.gamma',
    'Mixed_4b_b3b.bn.bn2d.beta',
    'Mixed_4c_b0.conv3d.weight',
    'Mixed_4c_b0.bn.bn2d.moving_mean',
    'Mixed_4c_b0.bn.bn2d.moving_variance',
    'Mixed_4c_b0.bn.bn2d.gamma',
    'Mixed_4c_b0.bn.bn2d.beta',
    'Mixed_4c_b1a.conv3d.weight',
    'Mixed_4c_b1a.bn.bn2d.moving_mean',
    'Mixed_4c_b1a.bn.bn2d.moving_variance',
    'Mixed_4c_b1a.bn.bn2d.gamma',
    'Mixed_4c_b1a.bn.bn2d.beta',
    'Mixed_4c_b1b.conv3d.weight',
    'Mixed_4c_b1b.bn.bn2d.moving_mean',
    'Mixed_4c_b1b.bn.bn2d.moving_variance',
    'Mixed_4c_b1b.bn.bn2d.gamma',
    'Mixed_4c_b1b.bn.bn2d.beta',
    'Mixed_4c_b2a.conv3d.weight',
    'Mixed_4c_b2a.bn.bn2d.moving_mean',
    'Mixed_4c_b2a.bn.bn2d.moving_variance',
    'Mixed_4c_b2a.bn.bn2d.gamma',
    'Mixed_4c_b2a.bn.bn2d.beta',
    'Mixed_4c_b2b.conv3d.weight',
    'Mixed_4c_b2b.bn.bn2d.moving_mean',
    'Mixed_4c_b2b.bn.bn2d.moving_variance',
    'Mixed_4c_b2b.bn.bn2d.gamma',
    'Mixed_4c_b2b.bn.bn2d.beta',
    'Mixed_4c_b3b.conv3d.weight',
    'Mixed_4c_b3b.bn.bn2d.moving_mean',
    'Mixed_4c_b3b.bn.bn2d.moving_variance',
    'Mixed_4c_b3b.bn.bn2d.gamma',
    'Mixed_4c_b3b.bn.bn2d.beta',
    'Mixed_4d_b0.conv3d.weight',
    'Mixed_4d_b0.bn.bn2d.moving_mean',
    'Mixed_4d_b0.bn.bn2d.moving_variance',
    'Mixed_4d_b0.bn.bn2d.gamma',
    'Mixed_4d_b0.bn.bn2d.beta',
    'Mixed_4d_b1a.conv3d.weight',
    'Mixed_4d_b1a.bn.bn2d.moving_mean',
    'Mixed_4d_b1a.bn.bn2d.moving_variance',
    'Mixed_4d_b1a.bn.bn2d.gamma',
    'Mixed_4d_b1a.bn.bn2d.beta',
    'Mixed_4d_b1b.conv3d.weight',
    'Mixed_4d_b1b.bn.bn2d.moving_mean',
    'Mixed_4d_b1b.bn.bn2d.moving_variance',
    'Mixed_4d_b1b.bn.bn2d.gamma',
    'Mixed_4d_b1b.bn.bn2d.beta',
    'Mixed_4d_b2a.conv3d.weight',
    'Mixed_4d_b2a.bn.bn2d.moving_mean',
    'Mixed_4d_b2a.bn.bn2d.moving_variance',
    'Mixed_4d_b2a.bn.bn2d.gamma',
    'Mixed_4d_b2a.bn.bn2d.beta',
    'Mixed_4d_b2b.conv3d.weight',
    'Mixed_4d_b2b.bn.bn2d.moving_mean',
    'Mixed_4d_b2b.bn.bn2d.moving_variance',
    'Mixed_4d_b2b.bn.bn2d.gamma',
    'Mixed_4d_b2b.bn.bn2d.beta',
    'Mixed_4d_b3b.conv3d.weight',
    'Mixed_4d_b3b.bn.bn2d.moving_mean',
    'Mixed_4d_b3b.bn.bn2d.moving_variance',
    'Mixed_4d_b3b.bn.bn2d.gamma',
    'Mixed_4d_b3b.bn.bn2d.beta',
    'Mixed_4e_b0.conv3d.weight',
    'Mixed_4e_b0.bn.bn2d.moving_mean',
    'Mixed_4e_b0.bn.bn2d.moving_variance',
    'Mixed_4e_b0.bn.bn2d.gamma',
    'Mixed_4e_b0.bn.bn2d.beta',
    'Mixed_4e_b1a.conv3d.weight',
    'Mixed_4e_b1a.bn.bn2d.moving_mean',
    'Mixed_4e_b1a.bn.bn2d.moving_variance',
    'Mixed_4e_b1a.bn.bn2d.gamma',
    'Mixed_4e_b1a.bn.bn2d.beta',
    'Mixed_4e_b1b.conv3d.weight',
    'Mixed_4e_b1b.bn.bn2d.moving_mean',
    'Mixed_4e_b1b.bn.bn2d.moving_variance',
    'Mixed_4e_b1b.bn.bn2d.gamma',
    'Mixed_4e_b1b.bn.bn2d.beta',
    'Mixed_4e_b2a.conv3d.weight',
    'Mixed_4e_b2a.bn.bn2d.moving_mean',
    'Mixed_4e_b2a.bn.bn2d.moving_variance',
    'Mixed_4e_b2a.bn.bn2d.gamma',
    'Mixed_4e_b2a.bn.bn2d.beta',
    'Mixed_4e_b2b.conv3d.weight',
    'Mixed_4e_b2b.bn.bn2d.moving_mean',
    'Mixed_4e_b2b.bn.bn2d.moving_variance',
    'Mixed_4e_b2b.bn.bn2d.gamma',
    'Mixed_4e_b2b.bn.bn2d.beta',
    'Mixed_4e_b3b.conv3d.weight',
    'Mixed_4e_b3b.bn.bn2d.moving_mean',
    'Mixed_4e_b3b.bn.bn2d.moving_variance',
    'Mixed_4e_b3b.bn.bn2d.gamma',
    'Mixed_4e_b3b.bn.bn2d.beta',
    'Mixed_4f_b0.conv3d.weight',
    'Mixed_4f_b0.bn.bn2d.moving_mean',
    'Mixed_4f_b0.bn.bn2d.moving_variance',
    'Mixed_4f_b0.bn.bn2d.gamma',
    'Mixed_4f_b0.bn.bn2d.beta',
    'Mixed_4f_b1a.conv3d.weight',
    'Mixed_4f_b1a.bn.bn2d.moving_mean',
    'Mixed_4f_b1a.bn.bn2d.moving_variance',
    'Mixed_4f_b1a.bn.bn2d.gamma',
    'Mixed_4f_b1a.bn.bn2d.beta',
    'Mixed_4f_b1b.conv3d.weight',
    'Mixed_4f_b1b.bn.bn2d.moving_mean',
    'Mixed_4f_b1b.bn.bn2d.moving_variance',
    'Mixed_4f_b1b.bn.bn2d.gamma',
    'Mixed_4f_b1b.bn.bn2d.beta',
    'Mixed_4f_b2a.conv3d.weight',
    'Mixed_4f_b2a.bn.bn2d.moving_mean',
    'Mixed_4f_b2a.bn.bn2d.moving_variance',
    'Mixed_4f_b2a.bn.bn2d.gamma',
    'Mixed_4f_b2a.bn.bn2d.beta',
    'Mixed_4f_b2b.conv3d.weight',
    'Mixed_4f_b2b.bn.bn2d.moving_mean',
    'Mixed_4f_b2b.bn.bn2d.moving_variance',
    'Mixed_4f_b2b.bn.bn2d.gamma',
    'Mixed_4f_b2b.bn.bn2d.beta',
    'Mixed_4f_b3b.conv3d.weight',
    'Mixed_4f_b3b.bn.bn2d.moving_mean',
    'Mixed_4f_b3b.bn.bn2d.moving_variance',
    'Mixed_4f_b3b.bn.bn2d.gamma',
    'Mixed_4f_b3b.bn.bn2d.beta',
    'Mixed_5b_b0.conv3d.weight',
    'Mixed_5b_b0.bn.bn2d.moving_mean',
    'Mixed_5b_b0.bn.bn2d.moving_variance',
    'Mixed_5b_b0.bn.bn2d.gamma',
    'Mixed_5b_b0.bn.bn2d.beta',
    'Mixed_5b_b1a.conv3d.weight',
    'Mixed_5b_b1a.bn.bn2d.moving_mean',
    'Mixed_5b_b1a.bn.bn2d.moving_variance',
    'Mixed_5b_b1a.bn.bn2d.gamma',
    'Mixed_5b_b1a.bn.bn2d.beta',
    'Mixed_5b_b1b.conv3d.weight',
    'Mixed_5b_b1b.bn.bn2d.moving_mean',
    'Mixed_5b_b1b.bn.bn2d.moving_variance',
    'Mixed_5b_b1b.bn.bn2d.gamma',
    'Mixed_5b_b1b.bn.bn2d.beta',
    'Mixed_5b_b2a.conv3d.weight',
    'Mixed_5b_b2a.bn.bn2d.moving_mean',
    'Mixed_5b_b2a.bn.bn2d.moving_variance',
    'Mixed_5b_b2a.bn.bn2d.gamma',
    'Mixed_5b_b2a.bn.bn2d.beta',
    'Mixed_5b_b2b.conv3d.weight',
    'Mixed_5b_b2b.bn.bn2d.moving_mean',
    'Mixed_5b_b2b.bn.bn2d.moving_variance',
    'Mixed_5b_b2b.bn.bn2d.gamma',
    'Mixed_5b_b2b.bn.bn2d.beta',
    'Mixed_5b_b3b.conv3d.weight',
    'Mixed_5b_b3b.bn.bn2d.moving_mean',
    'Mixed_5b_b3b.bn.bn2d.moving_variance',
    'Mixed_5b_b3b.bn.bn2d.gamma',
    'Mixed_5b_b3b.bn.bn2d.beta',
    'Mixed_5c_b0.conv3d.weight',
    'Mixed_5c_b0.bn.bn2d.moving_mean',
    'Mixed_5c_b0.bn.bn2d.moving_variance',
    'Mixed_5c_b0.bn.bn2d.gamma',
    'Mixed_5c_b0.bn.bn2d.beta',
    'Mixed_5c_b1a.conv3d.weight',
    'Mixed_5c_b1a.bn.bn2d.moving_mean',
    'Mixed_5c_b1a.bn.bn2d.moving_variance',
    'Mixed_5c_b1a.bn.bn2d.gamma',
    'Mixed_5c_b1a.bn.bn2d.beta',
    'Mixed_5c_b1b.conv3d.weight',
    'Mixed_5c_b1b.bn.bn2d.moving_mean',
    'Mixed_5c_b1b.bn.bn2d.moving_variance',
    'Mixed_5c_b1b.bn.bn2d.gamma',
    'Mixed_5c_b1b.bn.bn2d.beta',
    'Mixed_5c_b2a.conv3d.weight',
    'Mixed_5c_b2a.bn.bn2d.moving_mean',
    'Mixed_5c_b2a.bn.bn2d.moving_variance',
    'Mixed_5c_b2a.bn.bn2d.gamma',
    'Mixed_5c_b2a.bn.bn2d.beta',
    'Mixed_5c_b2b.conv3d.weight',
    'Mixed_5c_b2b.bn.bn2d.moving_mean',
    'Mixed_5c_b2b.bn.bn2d.moving_variance',
    'Mixed_5c_b2b.bn.bn2d.gamma',
    'Mixed_5c_b2b.bn.bn2d.beta',
    'Mixed_5c_b3b.conv3d.weight',
    'Mixed_5c_b3b.bn.bn2d.moving_mean',
    'Mixed_5c_b3b.bn.bn2d.moving_variance',
    'Mixed_5c_b3b.bn.bn2d.gamma',
    'Mixed_5c_b3b.bn.bn2d.beta',
    'logits_conv3d.weight',
    'logits_conv3d.bias',
]

pytorch_layers_name = [
    'Conv3d_1a_7x7.conv3d.weight',
    'Conv3d_1a_7x7.bn.weight',
    'Conv3d_1a_7x7.bn.bias',
    'Conv3d_1a_7x7.bn.running_mean',
    'Conv3d_1a_7x7.bn.running_var',
    'Conv3d_2b_1x1.conv3d.weight',
    'Conv3d_2b_1x1.bn.weight',
    'Conv3d_2b_1x1.bn.bias',
    'Conv3d_2b_1x1.bn.running_mean',
    'Conv3d_2b_1x1.bn.running_var',
    'Conv3d_2c_3x3.conv3d.weight',
    'Conv3d_2c_3x3.bn.weight',
    'Conv3d_2c_3x3.bn.bias',
    'Conv3d_2c_3x3.bn.running_mean',
    'Conv3d_2c_3x3.bn.running_var',
    'Mixed_3b.b0.conv3d.weight',
    'Mixed_3b.b0.bn.weight',
    'Mixed_3b.b0.bn.bias',
    'Mixed_3b.b0.bn.running_mean',
    'Mixed_3b.b0.bn.running_var',
    'Mixed_3b.b1a.conv3d.weight',
    'Mixed_3b.b1a.bn.weight',
    'Mixed_3b.b1a.bn.bias',
    'Mixed_3b.b1a.bn.running_mean',
    'Mixed_3b.b1a.bn.running_var',
    'Mixed_3b.b1b.conv3d.weight',
    'Mixed_3b.b1b.bn.weight',
    'Mixed_3b.b1b.bn.bias',
    'Mixed_3b.b1b.bn.running_mean',
    'Mixed_3b.b1b.bn.running_var',
    'Mixed_3b.b2a.conv3d.weight',
    'Mixed_3b.b2a.bn.weight',
    'Mixed_3b.b2a.bn.bias',
    'Mixed_3b.b2a.bn.running_mean',
    'Mixed_3b.b2a.bn.running_var',
    'Mixed_3b.b2b.conv3d.weight',
    'Mixed_3b.b2b.bn.weight',
    'Mixed_3b.b2b.bn.bias',
    'Mixed_3b.b2b.bn.running_mean',
    'Mixed_3b.b2b.bn.running_var',
    'Mixed_3b.b3b.conv3d.weight',
    'Mixed_3b.b3b.bn.weight',
    'Mixed_3b.b3b.bn.bias',
    'Mixed_3b.b3b.bn.running_mean',
    'Mixed_3b.b3b.bn.running_var',
    'Mixed_3c.b0.conv3d.weight',
    'Mixed_3c.b0.bn.weight',
    'Mixed_3c.b0.bn.bias',
    'Mixed_3c.b0.bn.running_mean',
    'Mixed_3c.b0.bn.running_var',
    'Mixed_3c.b1a.conv3d.weight',
    'Mixed_3c.b1a.bn.weight',
    'Mixed_3c.b1a.bn.bias',
    'Mixed_3c.b1a.bn.running_mean',
    'Mixed_3c.b1a.bn.running_var',
    'Mixed_3c.b1b.conv3d.weight',
    'Mixed_3c.b1b.bn.weight',
    'Mixed_3c.b1b.bn.bias',
    'Mixed_3c.b1b.bn.running_mean',
    'Mixed_3c.b1b.bn.running_var',
    'Mixed_3c.b2a.conv3d.weight',
    'Mixed_3c.b2a.bn.weight',
    'Mixed_3c.b2a.bn.bias',
    'Mixed_3c.b2a.bn.running_mean',
    'Mixed_3c.b2a.bn.running_var',
    'Mixed_3c.b2b.conv3d.weight',
    'Mixed_3c.b2b.bn.weight',
    'Mixed_3c.b2b.bn.bias',
    'Mixed_3c.b2b.bn.running_mean',
    'Mixed_3c.b2b.bn.running_var',
    'Mixed_3c.b3b.conv3d.weight',
    'Mixed_3c.b3b.bn.weight',
    'Mixed_3c.b3b.bn.bias',
    'Mixed_3c.b3b.bn.running_mean',
    'Mixed_3c.b3b.bn.running_var',
    'Mixed_4b.b0.conv3d.weight',
    'Mixed_4b.b0.bn.weight',
    'Mixed_4b.b0.bn.bias',
    'Mixed_4b.b0.bn.running_mean',
    'Mixed_4b.b0.bn.running_var',
    'Mixed_4b.b1a.conv3d.weight',
    'Mixed_4b.b1a.bn.weight',
    'Mixed_4b.b1a.bn.bias',
    'Mixed_4b.b1a.bn.running_mean',
    'Mixed_4b.b1a.bn.running_var',
    'Mixed_4b.b1b.conv3d.weight',
    'Mixed_4b.b1b.bn.weight',
    'Mixed_4b.b1b.bn.bias',
    'Mixed_4b.b1b.bn.running_mean',
    'Mixed_4b.b1b.bn.running_var',
    'Mixed_4b.b2a.conv3d.weight',
    'Mixed_4b.b2a.bn.weight',
    'Mixed_4b.b2a.bn.bias',
    'Mixed_4b.b2a.bn.running_mean',
    'Mixed_4b.b2a.bn.running_var',
    'Mixed_4b.b2b.conv3d.weight',
    'Mixed_4b.b2b.bn.weight',
    'Mixed_4b.b2b.bn.bias',
    'Mixed_4b.b2b.bn.running_mean',
    'Mixed_4b.b2b.bn.running_var',
    'Mixed_4b.b3b.conv3d.weight',
    'Mixed_4b.b3b.bn.weight',
    'Mixed_4b.b3b.bn.bias',
    'Mixed_4b.b3b.bn.running_mean',
    'Mixed_4b.b3b.bn.running_var',
    'Mixed_4c.b0.conv3d.weight',
    'Mixed_4c.b0.bn.weight',
    'Mixed_4c.b0.bn.bias',
    'Mixed_4c.b0.bn.running_mean',
    'Mixed_4c.b0.bn.running_var',
    'Mixed_4c.b1a.conv3d.weight',
    'Mixed_4c.b1a.bn.weight',
    'Mixed_4c.b1a.bn.bias',
    'Mixed_4c.b1a.bn.running_mean',
    'Mixed_4c.b1a.bn.running_var',
    'Mixed_4c.b1b.conv3d.weight',
    'Mixed_4c.b1b.bn.weight',
    'Mixed_4c.b1b.bn.bias',
    'Mixed_4c.b1b.bn.running_mean',
    'Mixed_4c.b1b.bn.running_var',
    'Mixed_4c.b2a.conv3d.weight',
    'Mixed_4c.b2a.bn.weight',
    'Mixed_4c.b2a.bn.bias',
    'Mixed_4c.b2a.bn.running_mean',
    'Mixed_4c.b2a.bn.running_var',
    'Mixed_4c.b2b.conv3d.weight',
    'Mixed_4c.b2b.bn.weight',
    'Mixed_4c.b2b.bn.bias',
    'Mixed_4c.b2b.bn.running_mean',
    'Mixed_4c.b2b.bn.running_var',
    'Mixed_4c.b3b.conv3d.weight',
    'Mixed_4c.b3b.bn.weight',
    'Mixed_4c.b3b.bn.bias',
    'Mixed_4c.b3b.bn.running_mean',
    'Mixed_4c.b3b.bn.running_var',
    'Mixed_4d.b0.conv3d.weight',
    'Mixed_4d.b0.bn.weight',
    'Mixed_4d.b0.bn.bias',
    'Mixed_4d.b0.bn.running_mean',
    'Mixed_4d.b0.bn.running_var',
    'Mixed_4d.b1a.conv3d.weight',
    'Mixed_4d.b1a.bn.weight',
    'Mixed_4d.b1a.bn.bias',
    'Mixed_4d.b1a.bn.running_mean',
    'Mixed_4d.b1a.bn.running_var',
    'Mixed_4d.b1b.conv3d.weight',
    'Mixed_4d.b1b.bn.weight',
    'Mixed_4d.b1b.bn.bias',
    'Mixed_4d.b1b.bn.running_mean',
    'Mixed_4d.b1b.bn.running_var',
    'Mixed_4d.b2a.conv3d.weight',
    'Mixed_4d.b2a.bn.weight',
    'Mixed_4d.b2a.bn.bias',
    'Mixed_4d.b2a.bn.running_mean',
    'Mixed_4d.b2a.bn.running_var',
    'Mixed_4d.b2b.conv3d.weight',
    'Mixed_4d.b2b.bn.weight',
    'Mixed_4d.b2b.bn.bias',
    'Mixed_4d.b2b.bn.running_mean',
    'Mixed_4d.b2b.bn.running_var',
    'Mixed_4d.b3b.conv3d.weight',
    'Mixed_4d.b3b.bn.weight',
    'Mixed_4d.b3b.bn.bias',
    'Mixed_4d.b3b.bn.running_mean',
    'Mixed_4d.b3b.bn.running_var',
    'Mixed_4e.b0.conv3d.weight',
    'Mixed_4e.b0.bn.weight',
    'Mixed_4e.b0.bn.bias',
    'Mixed_4e.b0.bn.running_mean',
    'Mixed_4e.b0.bn.running_var',
    'Mixed_4e.b1a.conv3d.weight',
    'Mixed_4e.b1a.bn.weight',
    'Mixed_4e.b1a.bn.bias',
    'Mixed_4e.b1a.bn.running_mean',
    'Mixed_4e.b1a.bn.running_var',
    'Mixed_4e.b1b.conv3d.weight',
    'Mixed_4e.b1b.bn.weight',
    'Mixed_4e.b1b.bn.bias',
    'Mixed_4e.b1b.bn.running_mean',
    'Mixed_4e.b1b.bn.running_var',
    'Mixed_4e.b2a.conv3d.weight',
    'Mixed_4e.b2a.bn.weight',
    'Mixed_4e.b2a.bn.bias',
    'Mixed_4e.b2a.bn.running_mean',
    'Mixed_4e.b2a.bn.running_var',
    'Mixed_4e.b2b.conv3d.weight',
    'Mixed_4e.b2b.bn.weight',
    'Mixed_4e.b2b.bn.bias',
    'Mixed_4e.b2b.bn.running_mean',
    'Mixed_4e.b2b.bn.running_var',
    'Mixed_4e.b3b.conv3d.weight',
    'Mixed_4e.b3b.bn.weight',
    'Mixed_4e.b3b.bn.bias',
    'Mixed_4e.b3b.bn.running_mean',
    'Mixed_4e.b3b.bn.running_var',
    'Mixed_4f.b0.conv3d.weight',
    'Mixed_4f.b0.bn.weight',
    'Mixed_4f.b0.bn.bias',
    'Mixed_4f.b0.bn.running_mean',
    'Mixed_4f.b0.bn.running_var',
    'Mixed_4f.b1a.conv3d.weight',
    'Mixed_4f.b1a.bn.weight',
    'Mixed_4f.b1a.bn.bias',
    'Mixed_4f.b1a.bn.running_mean',
    'Mixed_4f.b1a.bn.running_var',
    'Mixed_4f.b1b.conv3d.weight',
    'Mixed_4f.b1b.bn.weight',
    'Mixed_4f.b1b.bn.bias',
    'Mixed_4f.b1b.bn.running_mean',
    'Mixed_4f.b1b.bn.running_var',
    'Mixed_4f.b2a.conv3d.weight',
    'Mixed_4f.b2a.bn.weight',
    'Mixed_4f.b2a.bn.bias',
    'Mixed_4f.b2a.bn.running_mean',
    'Mixed_4f.b2a.bn.running_var',
    'Mixed_4f.b2b.conv3d.weight',
    'Mixed_4f.b2b.bn.weight',
    'Mixed_4f.b2b.bn.bias',
    'Mixed_4f.b2b.bn.running_mean',
    'Mixed_4f.b2b.bn.running_var',
    'Mixed_4f.b3b.conv3d.weight',
    'Mixed_4f.b3b.bn.weight',
    'Mixed_4f.b3b.bn.bias',
    'Mixed_4f.b3b.bn.running_mean',
    'Mixed_4f.b3b.bn.running_var',
    'Mixed_5b.b0.conv3d.weight',
    'Mixed_5b.b0.bn.weight',
    'Mixed_5b.b0.bn.bias',
    'Mixed_5b.b0.bn.running_mean',
    'Mixed_5b.b0.bn.running_var',
    'Mixed_5b.b1a.conv3d.weight',
    'Mixed_5b.b1a.bn.weight',
    'Mixed_5b.b1a.bn.bias',
    'Mixed_5b.b1a.bn.running_mean',
    'Mixed_5b.b1a.bn.running_var',
    'Mixed_5b.b1b.conv3d.weight',
    'Mixed_5b.b1b.bn.weight',
    'Mixed_5b.b1b.bn.bias',
    'Mixed_5b.b1b.bn.running_mean',
    'Mixed_5b.b1b.bn.running_var',
    'Mixed_5b.b2a.conv3d.weight',
    'Mixed_5b.b2a.bn.weight',
    'Mixed_5b.b2a.bn.bias',
    'Mixed_5b.b2a.bn.running_mean',
    'Mixed_5b.b2a.bn.running_var',
    'Mixed_5b.b2b.conv3d.weight',
    'Mixed_5b.b2b.bn.weight',
    'Mixed_5b.b2b.bn.bias',
    'Mixed_5b.b2b.bn.running_mean',
    'Mixed_5b.b2b.bn.running_var',
    'Mixed_5b.b3b.conv3d.weight',
    'Mixed_5b.b3b.bn.weight',
    'Mixed_5b.b3b.bn.bias',
    'Mixed_5b.b3b.bn.running_mean',
    'Mixed_5b.b3b.bn.running_var',
    'Mixed_5c.b0.conv3d.weight',
    'Mixed_5c.b0.bn.weight',
    'Mixed_5c.b0.bn.bias',
    'Mixed_5c.b0.bn.running_mean',
    'Mixed_5c.b0.bn.running_var',
    'Mixed_5c.b1a.conv3d.weight',
    'Mixed_5c.b1a.bn.weight',
    'Mixed_5c.b1a.bn.bias',
    'Mixed_5c.b1a.bn.running_mean',
    'Mixed_5c.b1a.bn.running_var',
    'Mixed_5c.b1b.conv3d.weight',
    'Mixed_5c.b1b.bn.weight',
    'Mixed_5c.b1b.bn.bias',
    'Mixed_5c.b1b.bn.running_mean',
    'Mixed_5c.b1b.bn.running_var',
    'Mixed_5c.b2a.conv3d.weight',
    'Mixed_5c.b2a.bn.weight',
    'Mixed_5c.b2a.bn.bias',
    'Mixed_5c.b2a.bn.running_mean',
    'Mixed_5c.b2a.bn.running_var',
    'Mixed_5c.b2b.conv3d.weight',
    'Mixed_5c.b2b.bn.weight',
    'Mixed_5c.b2b.bn.bias',
    'Mixed_5c.b2b.bn.running_mean',
    'Mixed_5c.b2b.bn.running_var',
    'Mixed_5c.b3b.conv3d.weight',
    'Mixed_5c.b3b.bn.weight',
    'Mixed_5c.b3b.bn.bias',
    'Mixed_5c.b3b.bn.running_mean',
    'Mixed_5c.b3b.bn.running_var',
    'logits.conv3d.weight',
    'logits.conv3d.bias',
]


def pytorch2mindspore(pretrained_path, save_path):
    print('Start conversion.')
    par_dict = torch.load(pretrained_path, map_location=torch.device('cpu'))
    params_list = []
    params_list_final = []

    for name in par_dict:
        param_dict = {}
        parameter = par_dict[name]
        param_dict['name'] = name
        param_dict['data'] = Tensor(parameter.numpy())
        params_list.append(param_dict)

    for name in pytorch_layers_name:
        temp = name
        if 'Conv3d' in temp:
            temp = temp.replace('conv3d.', '')
            temp = temp.replace('.bn', '_bn')
        if 'Mix' in temp:
            temp = temp.replace('.', '_', 1)
        if 'bn.' in temp:
            temp = temp.replace('bn.', 'bn.bn2d.', 1)
            temp = temp.replace('weight', 'gamma', 1)
            temp = temp.replace('bias', 'beta', 1)
        if 'running_var' in temp:
            temp = temp.replace('running_var', 'moving_variance', 1)
        if 'running_mean' in temp:
            temp = temp.replace('running_mean', 'moving_mean', 1)
        if 'logits' in temp:
            temp = temp.replace('.', '_', 1)

        for pd in params_list:
            for ms_name in mindspore_parameter_name:
                if pd['name'] == name and temp == ms_name:
                    params_list_final.append({"name": temp, "data": pd['data']})

    save_checkpoint(params_list_final, save_path)
    print('Finish conversion.')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pretrained_path', type=str, default='./pretrained/flow_imagenet.pt',
                        help='Path to pretrained model')
    parser.add_argument('--save_path', type=str, default='./pretrained/flow_imagenet.ckpt',
                        help='Path to save the converted model')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    config = parse_args()
    pytorch2mindspore(config.pretrained_path, config.save_path)
