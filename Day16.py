#!/usr/bin/env python
# coding: utf-8

# In[1]:

#16 day 
import numpy as np

# Create an array
data = np.array([10, 15, 20, 25, 30])

# Calculate mean and median
mean_value = np.mean(data)
median_value = np.median(data)

print("Data:", data)
print("Mean:", mean_value)
print("Median:", median_value)


# In[2]:


import numpy as np

# Create an array
data = np.array([5, 10, 15, 20, 25])

# Calculate standard deviation
std_deviation = np.std(data)

print("Data:", data)
print("Standard Deviation:", std_deviation)


# In[3]:


import numpy as np

# Generate random data
random_data = np.random.randint(0, 100, size=10)

# Calculate mean, median, and standard deviation
mean_value = np.mean(random_data)
median_value = np.median(random_data)
std_deviation = np.std(random_data)

print("Random Data:", random_data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)


# In[4]:


import numpy as np

# Create two arrays
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]

print("Array x:", x)
print("Array y:", y)
print("Correlation Coefficient:", correlation_coefficient)


# In[5]:


import numpy as np

# Create an array
data = np.array([15, 20, 25, 30, 35, 40, 45, 50])

# Calculate 25th and 75th percentiles
percentile_25 = np.percentile(data, 25)
percentile_75 = np.percentile(data, 75)

print("Data:", data)
print("25th Percentile:", percentile_25)
print("75th Percentile:", percentile_75)


# In[ ]:




