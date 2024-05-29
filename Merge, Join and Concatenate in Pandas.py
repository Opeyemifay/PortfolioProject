#!/usr/bin/env python
# coding: utf-8

# # Merge, Join and Concatenate in Pandas

# In[ ]:


# Natural join => how = 'inner' => only data that are both in the two tables
# Full outer join => how = 'outer' => all the data that are in both tables
# Left outer join => how = 'left' => all data in the left table, and similar data from the right, and not 
#unique data in right table.
# Right outer join => how = 'right' => all data in the right table, and similar data from the left, and not 
#unique data in left table.


# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\Admin\OneDrive\Tableau Files\LOTR.csv")
df


# In[3]:


df2 = pd.read_csv(r"C:\Users\Admin\OneDrive\Tableau Files\LOTR 2.csv")
df2


# In[5]:


df.merge(df2, how ='inner')


# In[6]:


df.merge(df2, how ='inner', on = 'FellowshipID')


# In[7]:


df.merge(df2, how ='inner', on = ['FellowshipID', 'FirstName'])


# In[8]:


df.merge(df2, how ='outer')


# In[9]:


df.merge(df2, how ='left')


# In[10]:


df.merge(df2, how ='right')


# In[11]:


df.merge(df2, how ='cross')

#cross join takes each data in the left table and merge it with all the data in the left table.


# # Join

# In[14]:


df.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix = '_Right')


# In[17]:


# join is much better when working with indexes 

df4 = df.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix = '_Left', rsuffix = '_Right', how = 'outer' )

df4


# # Concatenate

# In[ ]:


#Concantenate puts a dataframe on top of the other, rather than putting one dataframe next to one another 
#like join and merge


# In[18]:


pd.concat([df, df2])

#it literally placed the first table on the second table


# In[19]:


pd.concat([df, df2], join = 'inner')

#it returns column that are the same in the 2 tables


# In[20]:


pd.concat([df, df2], join = 'outer')


# In[21]:


pd.concat([df, df2], join = 'outer', axis = 1)

# the axis=1, joined the datframe to each other like a MERGE would.


# # Append

# In[ ]:


#the append () function is used to append rows from one dataframe to the end of another data frame


# In[22]:


df.append(df2)


# In[ ]:


# Actually append is scraped, its replica is concat. it does the same as append.


# In[ ]:




