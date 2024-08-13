#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests # requests is a liberary that contains packages .. and packeges contains modules which is .py file 
from bs4 import BeautifulSoup  # bs4 is a package that contains beautifulsoap module 
import pandas as pd


# In[2]:


url='https://en.wikipedia.org/wiki/Mohamed_Salah'

r = requests.get(url)

r.headers['content-type'] # to know what type that web page have text or json


# In[3]:


PageContent=r.text
print(PageContent)


# In[4]:


soup = BeautifulSoup(PageContent, 'html.parser')

#print(PageContent[0:500])
print(soup)


# In[20]:


# Find the first <p> tag
p_tag = soup.find('table')
p_tag.prettify()


# In[7]:


table =soup.find('table')
table


# In[8]:


tables = pd.read_html(url)
df=tables[0]


# In[9]:


df


# In[10]:


df=df.loc[2:33,"0":"1"]
df


# In[11]:


df.columns=['info','Stats']


# In[12]:


df


# In[ ]:




