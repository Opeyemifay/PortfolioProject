#!/usr/bin/env python
# coding: utf-8

# # Reading in Files

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\countries of the world.csv")

df
# when you go in between the link and press shift + tab, it displays all the argument 
# df stands for dataframe.


# In[3]:


# index is what makes a dataframa a dataframe. you can filter on index and as well serach on index.
# (header = none) removes header from a table
# (name = ['']) inserts header to a table - (name = ['Countyry', 'Region'])


# In[4]:


pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\countries of the world.csv", header = None)


# In[5]:


pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\countries of the world.csv", names = ['Country', 'Region'])


# In[6]:


df = pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\countries of the world.txt")

df

# the file format is in .text, so to convert to a table its .


# In[7]:


df = pd.read_table(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\countries of the world.txt")

df

# pd.read_table can be used to convert many data types


# In[8]:


df = pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\countries of the world.txt", sep = '\t')

df

#this is also another format to convert .txt to a table using sep(seperator)


# In[9]:


df = pd.read_json(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\json_sample.json")

df

# to read json file


# In[10]:


df = pd.read_excel(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\world_population_excel_workbook.xlsx")

df


# In[11]:


df2 = pd.read_excel(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')

df2

# in an excel workbook there are many sheet, to specify the sheet to work it, use sheet_name = 's'


# In[24]:


# There are some options in panda that only allow the first 5, and last five of a table to be displayed. However they can be
# displayed with the use of some codes.

pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns',39)

# display.max.rows is used to display hidden rows.
# display.max.columnc is used to display hidden columns.


# In[13]:


df2.info()

# .info() - displays all the information about a dataframe.


# In[14]:


df2.shape

# .shape - displays the number of column and rows in a dataframe


# In[15]:


df2.head()

# .head() displays the first five row in a table, meanwhile the number of rows to displayed can be specified.shown below.


# In[16]:


df2.head(10)


# In[17]:


df2.tail()

# .tail() displays the last five rows in a datagframe. it can also be specified like the .head()


# In[18]:


df2.tail(10)


# In[19]:


df2['Rank']


# In[20]:


df2.loc[149]

# .loc - location
# .iloc - integer location


# In[21]:


df2.iloc[149]


# In[ ]:




