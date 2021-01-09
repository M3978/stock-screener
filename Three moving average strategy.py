#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr


# In[2]:


yf.pdr_override() 


# In[3]:


now = dt.datetime.now()


# In[4]:


stock = input('Enter stock symbol')


# In[5]:


startyear = 2019


# In[6]:


startmonth = 1


# In[7]:


startday = 1


# In[8]:


start=dt.datetime(startyear,startmonth,startday)


# In[9]:


df=pdr.get_data_yahoo(stock,start,now)


# In[10]:


df.head()


# In[11]:


plt.figure(figsize=(12.2,4.5))


# In[15]:


plt.plot(df['Adj Close'])
plt.show()


# Calculate Three moving average:

# In[26]:


df['ma5'] = df['Adj Close']= df.iloc[:,4].rolling(window=21).mean()
df['ma21'] = df['Adj Close']= df.iloc[:,4].rolling(window=21).mean()
df['ma60'] = df['Adj Close']= df.iloc[:,4].rolling(window=21).mean()


# In[ ]:





# In[27]:


df.head()


# Vizualizing closing price and moving averages:
#     

# In[29]:


plt.figure(figsize=(15,12))
plt.plot(df['Adj Close'])
plt.plot(df['ma5'])
plt.plot(df['ma21'])
plt.plot(df['ma60'])


# In[ ]:




