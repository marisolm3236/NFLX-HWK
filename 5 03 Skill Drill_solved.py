#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import plotly.express as px
import statsmodels.api as sm


# In[2]:


def to_float(s):
    tmp_s = s.split()
    try:
        return float(tmp_s[0])
    except ValueError:
        return float('0')


# In[3]:


bikecounts_file = os.path.join('./','bikecounts.csv')
bikecounts_df = pd.read_csv(bikecounts_file, index_col=0)
bikecounts_df['Precipitation'] = bikecounts_df['Precipitation'].apply(to_float)
bikecounts_df['Day'] = pd.to_datetime(bikecounts_df['Day'])
bikecounts_df['Weekday'] = bikecounts_df['Day'].apply(lambda x: x.weekday())
print(bikecounts_df.info())
bikecounts_df.head()


# In[4]:


px.imshow(bikecounts_df[['Weekday','Precipitation','High Temp (°F)','Low Temp (°F)','Brooklyn Bridge']].corr())


# In[5]:


X = bikecounts_df[['Weekday','Precipitation','High Temp (°F)','Low Temp (°F)']]
y = bikecounts_df['Brooklyn Bridge']
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
y_predict = model.predict(results.params)
results.params


# In[6]:


results.summary()


# In[7]:


pd.DataFrame({'Brooklyn Bridge':y, 'Predict':y_predict}).head()


# In[8]:


# OLS only use High Temp (°F) as input
X = bikecounts_df['High Temp (°F)']
y = bikecounts_df['Brooklyn Bridge']
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
results.summary()


# Number of bikes cross Brooklyn Bridge is affected by day of the week, precipitation and high temperature because R-squared is 0.729 and p-value of Weekday, Precipitation and High Temp are below 0.05
