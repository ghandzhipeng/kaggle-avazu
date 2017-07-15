import utils
from utils import *
import os
import sys

path1 = utils.tmp_data_path
dest = sys.argv[1]
os.system("cp " + path1 + "/vwV12__r*.txt.gz " + dest)
os.system("cp " + path1 + "/fm__r*.txt " + dest)
