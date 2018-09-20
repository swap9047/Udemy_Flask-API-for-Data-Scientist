#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:53:39 2018

@author: swap9047
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

iris=load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=101,test_size=0.25)

clf=RandomForestClassifier(n_estimators=10)

clf.fit(x_train,y_train)

predicted=clf.predict(x_test)
print(accuracy_score(predicted,y_test))

import pickle
with open('/home/swap9047/Desktop/Udemy Flask/rf.pkl','wb') as model_pkl:
    pickle.dump(clf,model_pkl)