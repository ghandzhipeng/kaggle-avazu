## Dataset:
- click through data from day 21, 00:00 am to day 30, 23:00 pm.
- 40 M samples * 24 attributes, labels \in {0, 1}

## The entire process:
Can be found in the pdf. Mainly generating the features, feed them to different models, ensemble the models.

## Dependencies
1. Python 2.7.x + numpy + pandas + scikit­learn. Note that below is a feasible configuration but not a necessary one.
	- numpy == 1.10, for ndarrays
	- pandas == 0.15, for dataframes
	- sklearn == 0.17, for learning.

2. Vowpal Wabbit:
	- https://github.com/JohnLangford/vowpal_wabbit/wiki
	- after compiling the code, the path can be found: ---/vowpal_wabbit/vowpalwabbit/vw
	- VW relies on boost library.
	- charas of VW:
		- input format: [Label] [Importance] [Base] [Tag]|Namespace Features |Namespace Features ... |Namespace Features. Google for details.
		- optimized for Sparse data, pretty fast.
		- Feature Pairing.
		- can run programs use command line, like ```vw -paras values```

3. 3 idiot’s FM: 
	- https://github.com/guestwalk/kaggle­2014­criteo
	- after compiling, two executable files can be found: ffm-train, ffm-predict. Both can have several paras, used like ```ffm-train -paras values``` (Not fm!)
	- can handle field-aware factorization machines.

4. xgboost: 
	- https://github.com/tqchen/xgboost
	- after compiling, add it to the PYTHONPATH and you can use it via python: PYTHONPATH=---/xgboost/python-package
	- can handle gbdt algs.

## Debugs:
- after setting up the environment, there may be some bugs like ...(I forgot it). Mostly caused by not familar with Dataframe, numpy. Also there maybe some misuse of tools like ffm-train, ffm-predict, some path errors...
- another hint, when using small data to debug, please do not only ```head -n, tail -n```, combine them or split the file and randomly choose some.

## Things got:
1. You should first restore the environment of when running an existing code, may takes some time.
2. When there is a bug, you cannot modify it until you understand what the API exactly means, what the code is doing... Or it will waste you a lot of time.
3. Data read by pandas are firstly treated as objects.. astype('string')
4. The parameter "header" of pandas.read_csv is confusing: True(1-st line), False(0-th line)
, None(no schema info). Also, Dataframe can access/ADD via columns, via attributes, df['name', df.name.values=="ddddd"].
	- s.iloc[] -- for integer position addressing;
	- s.loc[] -- for index label addressing; and
	- s.ix[] -- for a hybrid of integer position and label addressing.
	- s.shape[0] -- how many rows
5. numpy deals with arrays.
6. many other errors like len of values and index not match... google it.
7. ./configure --prefix=$HOME/myapps, make, make install(mostly not this)


OK. I was just played for one and a half days... There are preprocessed features for these data whose code got the first place in the competition. https://github.com/guestwalk/kaggle-avazu 
