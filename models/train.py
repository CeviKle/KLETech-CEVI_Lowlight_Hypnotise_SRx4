# flake8: noqa
import os.path as osp

import archs
import data
import models
from basicsr.train import train_pipeline
import warnings


warnings.filterwarnings("ignore")




if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    print("hellllllllllllllllooooooooooooooooooooooo", root_path)
    train_pipeline(root_path)
