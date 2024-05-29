#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning in Pandas

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"C:\Users\Admin\OneDrive\Documents\Pandas Tutorial\Customer Call List.xlsx")
df


# In[3]:


# to drop duplicates in a table, when a row has the same details in a table

df.drop_duplicates()


# In[4]:


# to save the newly updated table

df = df.drop_duplicates()
df


# In[5]:


# in a bid to clean this data, there's a need to remove some columns that has no or less information the dataframe

df = df.drop(columns = 'Not_Useful_Column')
df


# In[10]:


# to remove white spaces, /, _, ... from lastname column
# the df["Last_Name"] is to ensure its stored in Last_Name, and not over write the whole dataframe.

#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123./_")
df


# In[13]:


# cleaning and standardizing Phone_number

df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','', regex =True)

df


# In[22]:


#df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-'+ x[6:10])
df


# In[23]:


# To remove all nan--, Na--

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')

df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')

df


# In[26]:


# standardizing column values using replace

df[['Street_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',', n = 2, expand = True)
df


# In[30]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')

df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')

df


# In[31]:


df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')

df


# In[35]:


# to remove all Nan across all rows

df = df.replace('N/a', '')
df = df.fillna('')

df


# In[37]:


# filtering down rows of data

for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace = True)

df


# In[38]:


for x in df.index:
    if df.loc[x, 'Phone_Number'] == '':
        df.drop(x, inplace = True)

df

# Another way to drop null values
# df = df.dropna(subset = 'Phone_Number'), inplace = True


# In[39]:


df.reset_index()


# In[40]:


df.reset_index(drop = True)


# In[ ]:




