#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1

#X
    


# In[3]:


#Q2

import pandas as pd

cast = pd.read_csv(r'C:\Users\Joshua Student\Downloads\cast_dataset.csv')
cast.head()


# In[4]:


#1
hamlets = cast.title.value_counts()['Hamlet']
print("there are ", hamlets , "amounts of titles with Hamlet")


# In[6]:


#2
print(cast[cast.title == "Treasure Island"].sort_values(by='year'))


# In[8]:


#3
x = len(cast[(cast.title == "Hamlet") & (cast.year == 1921)])
print(x,"roles were credited in the silent 1921 version of Hamlet")


# In[29]:


#4

df = cast[(cast.title == "Hamlet")]
new_df = df.groupby(df.year// 10 * 10).size()
new_df.plot(kind = 'bar')


# In[31]:


#5
men = len(cast[
    (cast.year == 1950) &
    (cast.n == 1) & (cast.type == 'actor')
])
print(men ,"men")

women = len(cast[
    (cast.year == 1950) &
    (cast.n == 1) & (cast.type == 'actress')
])
print(women, "women")


# In[32]:


#6
print(cast[
    (cast.year >= 1990) &
    (cast.n == 1)
].sort_values(by='name').head(10))

df = cast[(cast.n == 1)].count_values


# In[41]:


#6
df = cast[(cast.n == 1) & (cast.year > 1990)].sort_values(by='name')
df.count()

lst =  []

for i in df:


# In[58]:


#7

df = cast[cast.name == 'Frank Oz']
new_df = df.groupby(['year','title']).size()
df = new_df[new_df > 1]
df.plot(kind='bar')
print(df)


# In[ ]:





# In[ ]:




