import pandas as pd
import numpy as np
import scipy as sc
import scipy.sparse as sp
import pylab 
import sys
import time
import os
import utils
from utils import *
from joblib import dump, load, Parallel, delayed

sys.path.append(utils.xgb_path)
import xgboost as xgb
from sklearn.datasets import dump_svmlight_file
def build_data():
    t0tv_mx_save = load(utils.tmp_data_path + 't0tv_mx.joblib_dat')

    t0tv_mx = t0tv_mx_save['t0tv_mx']
    click_values = t0tv_mx_save['click']
    day_values = t0tv_mx_save['day']
    
    print "t0tv_mx loaded with shape ", t0tv_mx.shape
    dump_svmlight_file(t0tv_mx, click_values, sys.argv[1] +'/vw_fm1.dat',zero_based=True,multilabel=False)

build_data()
