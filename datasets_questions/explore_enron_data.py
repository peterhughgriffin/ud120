#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
import numpy as np
from time import time
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat
from feature_format import targetFeatureSplit

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

#%%
print(len(enron_data))

#%%
POICount=0

for person in enron_data:
    if enron_data[person]["poi"]==1:
        POICount += 1

#%%
print(enron_data["PRENTICE JAMES"]['total_stock_value'])

#%%
print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

#%%
print(enron_data["SKILLING JEFFREY K"])

#%%
Bosses=[]
BossNames = ["LAY", "SKILLING", "FASTOW"]

for person in enron_data:
    for Boss in BossNames:
        if Boss in person:
            Bosses.append(enron_data[person])
            print(person + " obtained this much money: " + str(enron_data[person]["total_payments"]))

#%%
salaried=0
for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        salaried += 1
        print(person)

#%%
emailer=0
for person in enron_data:
    if enron_data[person]['email_address'] != 'NaN':
        emailer += 1
        print(person)

#%%

data=featureFormat(enron_data,['poi','salary'])
target, features = targetFeatureSplit(data)

#%%
TotalPay=0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        TotalPay += 1
        print(person)
        
print(TotalPay/len(enron_data)*100)
      
#%%
TotalPay_poi=0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN' and enron_data[person]['poi'] == 1:
        TotalPay_poi += 1
        print(person)
        
print(TotalPay_poi/len(enron_data)*100)













