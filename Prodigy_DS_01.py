#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import matplotlib.pyplot as plt


# In[13]:


# Load the dataset from a CSV file
data = pd.read_csv('population_by_age.csv')


# In[14]:


# Display the first few rows of the dataset
print(data.head())


# In[15]:


# Create a bar chart for Population by Age Group
plt.figure(figsize=(12, 8))
plt.bar(data['Age Group'], data['Population'], color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Population')
plt.title('Population Distribution by Age Group')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




