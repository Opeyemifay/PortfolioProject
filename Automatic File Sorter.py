#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter

# In[1]:


#import os - import operating system
#shutil - is shell utilities
#r allows the code to be read as a raw string.
#shutil is called "shell utilities" because it allows you to perform various file-related tasks that are 
#similar to the commands that you might use in a Unix shell,such as copying, moving, renaming, 
#and deleting files and directories.



import os 
import shutil


# In[2]:


path = r'C://Users//Admin//Documents//python tutorials//'


# In[15]:


file_name = os.listdir(path)


# In[6]:


folder_name = ['csv files', 'image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        os.makedirs((path + folder_name[loop]))
        print(path + folder_name[loop])
      
    
for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)


# In[14]:



        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




