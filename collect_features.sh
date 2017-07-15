#! /bin/bash
feature_path=$1
# 1. collect features for RF and GBDT, which are in libsvm format
python _rf_gbdt_fea.py $feature_path
# 2. collect features for intermediate step of fm and vm, which is also in libsvm format.
python _vw_fm_fea.py $feature_path
# 3. copy features for fm and vm to the path where the features are generated during the execution of _0_run_me.sh. These features are not in libsvm format, but suitble for vw and ffm-train, ffm-predict tools. You may only choose one seed.
python _vw_fm_fea2.py $feature_path
