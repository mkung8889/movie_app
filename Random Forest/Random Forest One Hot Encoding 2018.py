#!/usr/bin/env python
# coding: utf-8

# * grouplens MovieLens 2018 20M data: https://grouplens.org/datasets/movielens/20m/
# * feature engineered genres by performing one hot encoding
# * utilized random forest to confirm that this model would be a poor predictor when compared to recommender models

# In[1]:


# import dependencies
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# import movies
df = pd.read_csv("../data/ml-20m/201820M.csv")
df.head()


# In[3]:


# set rating to what we are trying to predict
target = df["rating"].astype(int)


# In[4]:


# removing ratings to create our x values
data = df
data.drop(["rating"],axis=1, inplace=True)


# In[5]:


# data = data
feature_names = data.columns
data.head()


# In[6]:


X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)


# In[ ]:


rf = RandomForestClassifier(n_estimators=50)
rf = rf.fit(X_train, y_train)
rf.score(X_test, y_test)


# In[ ]:


importances = rf.feature_importances_
importances


# In[ ]:


sorted(zip(rf.feature_importances_, feature_names), reverse=True)


# In[ ]:


sns.set(rc={'figure.figsize':(6,10)})


# In[ ]:


sns.barplot(x=importances, y=feature_names)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Features by Importance")
plt.legend()
plt.savefig("images/RF2018OHE.png")
plt.show()


# In[ ]:


predicted_y = rf.predict(X_test)


# In[ ]:


actual_y = y_test.to_numpy()


# In[ ]:


mean_squared_error(actual_y, predicted_y)


# In[ ]:




