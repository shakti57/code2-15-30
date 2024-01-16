#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Creating a DataFrame from a dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 22],
        'City': ['New York', 'San Francisco', 'Chicago']}
df = pd.DataFrame(data)


# In[3]:


# Display the first few rows of the DataFrame
print(df.head())

# Display basic information about the DataFrame
print(df.info())

# Descriptive statistics of numerical columns
print(df.describe())


# In[4]:


# Selecting a column
print(df['Name'])

# Selecting multiple columns
print(df[['Name', 'Age']])

# Filtering rows based on a condition
print(df[df['Age'] > 25])


# In[5]:


# Adding a new column
df['IsAdult'] = df['Age'] > 18

# Updating values
df.loc[df['Name'] == 'John', 'City'] = 'Boston'

# Removing a column
df = df.drop('IsAdult', axis=1)


# In[6]:


df


# In[ ]:




