import os
import torch

class Config(object):
    def __init__(self, data_dir):
        assert os.path.exists(data_dir)
        self.train_file = os.path.join(data_dir, "train.txt")