#!/usr/bin/env python
# coding: utf-8

# In[1]:
#18

import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Show the plot
plt.show()


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
fmri = sns.load_dataset("fmri")

# Line plot
sns.lineplot(x="timepoint", y="signal", data=fmri)

# Show the plot
plt.show()


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
iris = sns.load_dataset("iris")

# Histogram
sns.histplot(x="sepal_length", data=iris, bins=20)

# Show the plot
plt.show()


# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Box plot
sns.boxplot(x="day", y="total_bill", data=tips)

# Show the plot
plt.show()


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
flights = sns.load_dataset("flights")

# Pivot the data for heatmap
flights_pivot = flights.pivot_table(index='month', columns='year', values='passengers')

# Heatmap
sns.heatmap(flights_pivot, cmap="YlGnBu", annot=True, fmt="d", linewidths=.5)

# Show the plot
plt.show()


# In[ ]:




