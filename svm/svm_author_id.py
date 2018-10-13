#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess() 
clf = SVC(C = 10000,kernel="rbf")
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
count =0
for i in range(len(pred)):
    if (pred[i]==1):
        count+=1
print (count)


#########################################################
### your code goes here ###

#########################################################


