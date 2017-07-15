import pandas as pd
import numpy as np
import scipy as sc
import scipy.sparse as sp
from sklearn.utils import check_random_state 
import pylab 
import sys
import time
import utils
from utils import *
import os
from sklearn.datasets import dump_svmlight_file

from joblib import dump, load

t0tv_mx_save = load(utils.tmp_data_path + 't0tv_mx3.joblib_dat')
t0tv_mx3 = t0tv_mx_save['t0tv_mx']
click_values = t0tv_mx_save['click']
day_values = t0tv_mx_save['day']

print "t0tv_mx3 loaded with shape", t0tv_mx3.shape
dump_svmlight_file(t0tv_mx3,click_values, sys.argv[1]+'/rf_gbdt.dat',zero_based=True,multilabel=False)
exit(1)
