#!/usr/bin/env python
# coding: utf-8

# ## Feature Engineering

# In[1]:


# get_ipython().system('pip install fuzzywuzzy')
# get_ipython().system('pip install python-Levenshtein')


# In[2]:


import pandas as pd
import numpy as np
import time
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[3]:


data = pd.read_csv('../../Data/Amazon/meta_Books.csv')


# In[4]:


data.head()


# In[5]:


data_kaggle = pd.read_csv('../../Data/Popular_Books.csv')


# In[6]:


data_kaggle.head()


# In[7]:


# data_kaggle = data_kaggle.iloc[:20,:]


# In[8]:


# final_ratio = {}
final_values = []
final_indices = []

start = time.time()
for book_kaggle in data_kaggle['Book-Title']:
    ratio = []
    search_space_indices = []
    i = 0
    while len(search_space_indices) == 0:
        try:
            first_word = str.split(book_kaggle)[i]
            first_word = re.sub('[^A-Za-z0-9]+', '', first_word)
#             print(first_word)
            if first_word in ['The', 'A']:
                first_word = str.split(book_kaggle)[i+1] # maybe not the best strategy
            search_space = data["title"].str.find(first_word) == 0
            search_space_indices = data['title'][search_space].reset_index().iloc[:,0]
#             if i > 0:
#                 print('Went to the next word............')
        except:
#             print(book_kaggle, '...............................................')
            search_space_indices = [1]
            break
        i = i+1
        
#     if len(search_space_indices) == 0 && search_space_indices[0] == 'empty':
        
#     print(len(search_space_indices))
    for book_amazon in data['title'][search_space_indices]:
        value = fuzz.token_sort_ratio(book_kaggle, book_amazon)
        ratio.append(value)
#     print(ratio)
    final_indices.append(search_space_indices[np.argmax(ratio)])
    final_values.append(ratio[np.argmax(ratio)])
    
end = time.time()
print("The time of execution of above program is :",
      (end-start), "s")


# In[9]:


data_amazon_sel = data.iloc[final_indices, [1,3,5,6,10,11,15,16]]
data_amazon_sel['match_value'] = final_values
data_amazon_sel.head()


# In[27]:


data_amazon_sel


# In[50]:


a = data_kaggle.reset_index()
b = data_amazon_sel.reset_index(drop=True).reset_index()
a.head()


# In[51]:


b.head()


# In[54]:


df_merged = pd.merge(a, b, on='index', how='inner')
df_merged.head()


# In[64]:


df_merged.iloc[:,[1,2,3,4,5]+list(np.arange(9,df_merged.shape[1], 1))]


# In[65]:


df_merged.to_csv('merged_dataset.csv')


# In[ ]:




