import sys
from trainer import Trainer_ReconNet
from net import ReconNet
from data_loader import get_train_val_data_loaders

num_views = 1

class trainerArgs:
    # experiment name
    exp = 1
    # fails if else
    arch = 'ReconNet'
    # log frequency
    print_freq = 1
    # output model path
    output_path = ''
    # fails if else
    resume = 'best'
    # no idea
    num_views = num_views
    # fails if 0
    output_channel = 46
    # default
    init_gain = 0.02
    # default
    init_type = 'standard'
    # optimizer settings
    loss = 'l1'
    optim = 'adam'
    lr = 0.001
    weight_decay = 0

newTrainer = Trainer_ReconNet(trainerArgs())

class loaderArgs:
    # experiment name
    exp = 1
    num_views = num_views
    input_size = 128
    output_size = 128
    data_root = 'exp/data'
    data_list_dir = 'exp/result'
    batch_size = 1
    num_workers = 1

train_loader, val_loader = get_train_val_data_loaders(train_file='datalist.csv', val_file="", args=loaderArgs)

newTrainer.train_epoch(train_loader, 0)

# exp=1,
# arch='ReconNet',
# print_freq=1,
# output_path='',
# resume='best',
# num_views = 1,
# output_channel=0,
# init_gain=0.02,
# init_type='standard'

# python newmodel.py exp 1 arch 'ReconNet' print_freq 1 output_path '' resume 'best' num_views 1 output_channel 0 init_gain 0.02 init_type 'standard' 

# 'exp' 1, 
# 'seed' 1, 
# 'num-views' 1,
# 'input-size' 128,
# 'output-size' 128,
# 'output-channel' 0,
# 'start-slice' 0,
# 'test' 1,
# 'vis_plane' 0,