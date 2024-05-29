#!/usr/bin/env python
# coding: utf-8

# # Data visualization in Pandas

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\Admin\OneDrive\Tableau Files\Ice Cream Ratings.csv")
df


# In[6]:


df.set_index('Date', inplace = True)


# In[7]:


df.plot()


# In[8]:


df.plot(kind = 'line')


# In[9]:


df.plot(kind = 'line', subplots = True)


# In[27]:


print(plt.style.available)

#it displays all the styles available for a line chart.


# In[44]:


plt.style.use('Solarize_Light2')


# In[46]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Rating', ylabel = 'Scores', figsize = (10,5))


# In[13]:


df.plot(kind = 'bar')


# In[14]:


df.plot(kind = 'bar', stacked = True)


# In[15]:


df['Flavor Rating'].plot(kind = 'bar')


# In[16]:


df.plot.barh(stacked = True)

#barh stands for horizontal bar


# In[19]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 550, c= 'Green')
# scatterplot graph
# s = size
# c = color


# In[20]:


df.plot.hist()


# In[21]:


df.plot.hist(bins = 15)


# In[22]:


df.boxplot()


# In[23]:


df.plot.area()


# In[24]:


df.plot.area(figsize = (10,5))


# In[26]:


df.plot.pie(y = 'Texture Rating', figsize = (10,6))


# In[ ]:




