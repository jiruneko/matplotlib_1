#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)
plt.show()


# In[2]:


import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


x1 = [1, 2, 3]
y1 = [2, 4, 6]
x2 = [1, 2, 3]
y2 = [-2, -4, -6]

fig, axes = plt.subplots(2)
axes[0].plot(x1, y1)
axes[1].plot(x2, y2)
plt.show()


# In[5]:


fig, ax = plt.subplots(2, 2)
plt.show()


# In[6]:


fig, ax = plt.subplots(ncols=2)
plt.show()


# In[7]:


import matplotlib.style


# In[8]:


matplotlib.style.available


# In[9]:


matplotlib.style.use('seaborn')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# In[10]:


x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, label='sample legend')
ax.legend()
plt.show()


# In[11]:


x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, label='sample legend')
ax.legend(loc='lower right')
plt.show()


# In[ ]:




