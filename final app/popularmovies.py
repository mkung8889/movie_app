#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ratings = pd.read_csv("../data/ml-100k/ratings.csv")
ratings.head()


# In[3]:


ratings = ratings[ratings.rating == 5.0]
ratings.head()


# In[4]:


movies = ratings.groupby(["movieId"]).count()
movies.head()


# In[5]:


movies = movies.sort_values(by=['rating'], ascending=False).head(20)


# In[6]:


movies


# In[7]:


items = pd.read_csv("../data/ml-100k/movies.csv")
items.head()


# In[8]:


links = pd.read_csv("../data/ml-100k/links.csv")
links.head()


# In[9]:


df = pd.merge(movies, items, on="movieId", how="left")
df


# In[10]:


df = pd.merge(df, links, on="movieId", how="left")
df


# In[11]:


df.drop(['userId', 'timestamp', 'genres', 'tmdbId'],axis=1, inplace=True)


# In[12]:


df


# In[ ]:




