
# coding: utf-8

# In[21]:


import numpy as np


#low medium high
# microsoft_apple = np.zeros((3,3)) 
# microsoft_amazon = np.zeros((3,3)) 
# apple_amazon = np.zeros((3,3)) 
# hanes_amazon = np.zeros((3,3)) 
# nike_hanes = np.zeros((3,3)) 

# 3^5 -> giant table (a,b,c)x(d,e) = (a,d),(a,e),...
#rigged parameters
microsoft_apple = np.array([[1,2,3],[0,100, 50],[34, 78, 1000]])
microsoft_amazon =np.array([[10,22,50],[2220,109, 50],[4, 8, 60]])
apple_amazon = np.array([[122,357,5],[17,99, 1001],[45, 7, 82]])


hanes_amazon =  np.array([[154,297,48],[80,73, 4699],[8004, 913, 468]])
nike_hanes =  np.array([[21,4,8995],[107,99, 974],[69000, 942, 62]])

apple_amazon.shape


# In[23]:


#itertools test
# https://stackoverflow.com/questions/14931769/
#how-to-get-all-combination-of-n-binary-value
import itertools
n= 3
lst = list(itertools.product([0, 1, 2], repeat=n))
# lst composed of (Microsoft, Apple, Amazon) respectively 

clique = np.arange(27).reshape((3,3,3))
#print(len(lst))
for tuple_ in lst:

    apple_amazon[0][0]
    micro_apple = microsoft_apple[tuple_[0], tuple_[1]]
    micro_amazon =  microsoft_amazon[tuple_[0], tuple_[2]]    
    app_amazon = apple_amazon[tuple_[1], tuple_[2]]
    
    clique[tuple_[0], tuple_[1], tuple_[2]] = micro_apple*micro_amazon*app_amazon


# In[24]:


#clique = np.arange(27).reshape((3,3,3))
clique  # highest dimension -> Microsoft 462


# In[ ]:


# message passing algorithm 
#nike -> hanes

#clique -> hanes

#hanes -> clique

#hanes -> nike 

