#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Name : ")


# In[ ]:


#import the libraries
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dataframe_bmi = pd.read_csv('bmi.csv')
dataframe_bmi
#Task 1
#Read the bmi.csv


# In[2]:


#Task 2
#Data is sorted in descending order in accordance with BMI value
#Find the top 5 age group where the BMI value is the highest, and plot a bar graph out of it
top_5 = dataframe_bmi.head(5)
label = top_5['Age']
value = top_5['BMI']
plt.xlabel("Age")
plt.ylabel("BMI")
plt.xticks(rotation='vertical')

print(label)
print(value)

plt.bar(label,value,width=0.4, color=('red','black'))


# In[ ]:


#Task 3
#Read blood_pressure.csv


# In[ ]:


#Task 4
#Data is sorted in ascending order in accordance with Blood Pressure
#Find the top 5 age group where the BloodPressure value is the highest, and plot a bar graph out of it


# In[ ]:


#Task 5
#Read the insulin.csv


# In[ ]:


#Task 6
#Data is sorted in descending order in accordance with Insulin value
#Find out what will be the Glucose and BMI value when the Insulin is highest


# In[ ]:





# In[ ]:




