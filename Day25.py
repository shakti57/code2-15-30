#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Day 25

import pandas as pd

# Creating a data frame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print(df)


# In[2]:


# Accessing and manipulating data in a data frame
print(df['Name'])  # Accessing a column
print(df.iloc[0])  # Accessing a row by index

# Adding a new column
df['Salary'] = [50000, 60000, 55000]

# Filtering data
filtered_df = df[df['Age'] > 25]
print(filtered_df)


# In[5]:


# Merging data frames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [60000, 55000, 70000]})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)


# In[6]:


# Merging data frames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [60000, 55000, 70000]})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)


# In[ ]:




