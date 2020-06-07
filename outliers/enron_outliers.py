#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit



### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]

# Remove the outlier "TOTAL"
data_dict.pop( "TOTAL", 0 )

data = featureFormat(data_dict, features)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

#%% This is how I (eventually) found the outlier

# for item in data_dict:
#     # print(data_dict[item]['salary'])
#     if data_dict[item]['salary']==26704229:
#         print(item)

#%%
for item in data_dict:
    # print(data_dict[item]['salary'])
    if data_dict[item]['salary']=='NaN' or data_dict[item]['bonus']=='NaN':
        pass
    elif data_dict[item]['salary']>1e6 and data_dict[item]['bonus']>5e6:
        print(item)