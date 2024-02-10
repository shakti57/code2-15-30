#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Day20
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a scatter plot using Seaborn
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Show the plot
plt.show()


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a histogram with KDE using Seaborn
sns.histplot(tips['total_bill'], kde=True)

# Show the plot
plt.show()


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a box plot with categorical data using Seaborn
sns.boxplot(x="day", y="total_bill", data=tips)

# Show the plot
plt.show()


# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
iris = sns.load_dataset("iris")

# Create a pair plot for multivariate analysis using Seaborn
sns.pairplot(iris, hue="species")

# Show the plot
plt.show()


# In[ ]:




