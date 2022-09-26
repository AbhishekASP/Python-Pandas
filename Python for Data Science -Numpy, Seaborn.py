#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


tips = sns.load_dataset('tips') # tips is a data set present in seaborn.


# In[6]:


tips.head(10)


# In[7]:


tips.shape


# In[9]:


np.mean(tips['total_bill'])


# In[10]:


np.median(tips['total_bill'])


# In[16]:


np.var(tips['total_bill'])


# In[18]:


np.percentile(tips['total_bill'],50)


# In[19]:


np.percentile(tips['total_bill'],25)


# In[20]:


np.percentile(tips['total_bill'],75)


# In[21]:


sns.boxplot(tips['total_bill'])


# In[22]:


tips.columns


# In[23]:


sns.countplot(tips['sex'])


# In[31]:


pd.value_counts(tips['sex']=='Male')


# In[34]:


sns.scatterplot(tips['total_bill'],tips['tip'])


# In[35]:


sns.distplot(tips['total_bill'])


# In[ ]:




