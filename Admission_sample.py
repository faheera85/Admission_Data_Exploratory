#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[8]:


df = pd.read_csv("Admission_Predict_Ver1.1.csv")


# In[13]:


df.shape


# In[19]:


df.head()


# In[20]:


df.tail()


# In[27]:


#Normalizing data
df['GRE Score'] = df['GRE Score']/380
df['University Rating'] = df['University Rating']/5
df['SOP']=df['SOP']/5
df['LOR ']=df['LOR ']/5
df['CGPA']=df['CGPA']/10
df['TOEFL Score']=df['TOEFL Score']/120


# In[35]:


df.hist(bins=60, figsize=(30,20))
plt.show()


# In[ ]:




