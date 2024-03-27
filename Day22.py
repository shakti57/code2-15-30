#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Day 22

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.rand(10, 12)
sns.heatmap(data, cmap="YlGnBu")
plt.show()


# In[7]:


import plotly.express as px
import numpy as np

# Generate random data
data = np.random.rand(10, 12)

# Create heatmap using Plotly Express
fig = px.imshow(data, color_continuous_scale="YlGnBu")
fig.show()


# In[ ]:




