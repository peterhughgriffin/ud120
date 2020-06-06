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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#%% ########################################################
### your code goes here ###

from sklearn.svm import SVC

clf = SVC(C=10000.0,kernel="rbf")

Reduce=1

features_train_red = features_train[:int(len(features_train)/Reduce)]
labels_train_red = labels_train[:int(len(labels_train)/Reduce)]

t0 = time()
clf.fit(features_train_red, labels_train_red)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print ("prediction time:", round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score

Accuracy = accuracy_score(labels_test, pred)

print(Accuracy)
#%% 

# print(clf.predict([features_test[50]]))
Count0=0
Count1=0
for item in pred:
    if item == 0:
        Count0=Count0+1
    else:
        Count1=Count1+1

print(Count1)



#########################################################


