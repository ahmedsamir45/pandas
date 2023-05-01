#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd


# In[54]:


car_model = pd.Series(['bmw','wonda','toyota'])


# In[55]:


car_model


# In[56]:


car_color = pd.Series(["white","black","red"])


# In[57]:


car_color


# In[58]:


car_data = pd.DataFrame({'car model':car_model,'car colour':car_color})


# In[59]:


car_data

        


# In[60]:


car_sales = pd.read_csv('E:\data sceince csv\car-sales.csv')


# In[61]:


car_sales


# In[62]:


car_sales.dtypes


# In[63]:


car_sales.columns


# In[64]:


car_sales.index


# In[65]:


car_sales.describe()


# In[66]:


car_sales.info


# In[67]:


car_sales["Odometer (KM)"].mean()


# In[68]:


car_sales.sum()


# In[69]:


len(car_sales)


# In[70]:


car_sales.head()


# In[71]:


car_sales.head(7)


# In[72]:


car_sales.tail()



# In[73]:


car_sales.tail(4)


# In[74]:


car_sales.loc[3]


# In[75]:


car_sales.shape


# In[76]:


car_sales.shape


# In[77]:


car_data.to_csv("exported car data")


# In[78]:


car_sales["Doors"]


# In[79]:


car_sales["Doors"].sum()


# In[80]:


len(car_sales)


# In[81]:


car_sales.sum()


# In[82]:


animals = pd.Series(["cat","dog","bird","lion","pandas"],index=[0,9,3,4,2])


# In[83]:


animals


# In[84]:


animals.iloc[3]


# In[85]:


animals.loc[3]


# In[86]:


animals.iloc[:3]


# In[90]:


car_sales


# In[91]:


car_sales["Price"].str.replace("[\$\,\.]",'').astype(int)


# In[92]:


car_sales_missing =pd.read_csv("E:\data sceince csv\car-sales-missing-data.csv")


# In[93]:


car_sales_missing 


# In[95]:


car_sales_missing.info


# In[98]:


car_sales_missing.info()


# In[99]:


car_sales_missing["Odometer"].mean()


# In[100]:


car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean())


# In[101]:


car_sales_missing


# In[102]:


car_sales_missing["Odometer"] = car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean())


# In[103]:


car_sales_missing


# In[104]:


car_sales_missing.dropna()


# In[105]:


seats_column = pd.Series([4,4,4,4,4])


# In[106]:


seats_column


# In[107]:


car_sales['seats'] = seats_column


# In[108]:


car_sales


# In[111]:


car_sales["seats"].fillna(4)


# In[112]:


car_sales["seats"]=car_sales["seats"].fillna(4)


# In[113]:


car_sales


# In[114]:


fuel = [90,80,50,60,30,20,50,98,67,43]


# In[115]:


car_sales["fuel for 100 km"] = fuel


# In[116]:


car_sales


# In[ ]:




