#!/usr/bin/env python
# coding: utf-8

# In[2]:
#Day 21 lambda pgm

add = lambda x, y: x + y
result = add(3, 5)
print(result)  


# In[3]:


square = lambda x: x**2
result = square(4)
print(result)  


# In[4]:


is_even = lambda x: x % 2 == 0
result = is_even(7)
print(result)  


# In[5]:


concatenate = lambda a, b: a + b
result = concatenate("Hello", " Shakti")
print(result)  


# In[6]:


max_of_three = lambda x, y, z: max(x, y, z)
result = max_of_three(10, 5, 8)
print(result)  


# In[ ]:




