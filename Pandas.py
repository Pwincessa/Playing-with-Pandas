
# coding: utf-8

# In[45]:


import numpy as np


# In[3]:


import pandas as pd


# In[44]:


from numpy.random import randn


# In[5]:


# creating two lists
list1 = ["a","b", "c","d", "e"]
list2 = [1,2,3,4,5]


# In[6]:


x = np.array(list2)


# In[7]:


x


# In[9]:


dic1 = {"a": 1, "b": 2, "c":3, "d":4, "e":5}


# In[10]:


dic1


# In[15]:


pd.Series(list1) #creating a pandas series, also note that the numbers at the side indicates the row numbers e.g "a" is row 0


# In[16]:


pd.Series(data= list2, index =list1) # this implies the alphabeth value are the rows and the numbers are the column


# In[18]:


new =pd.Series(data= list2, index =list1)


# In[20]:


new['b']  # Indexing out b


# In[22]:


mew2 =pd.Series([1,2,3,4], index = ["Nigeria", "France", "Belgium", "England"])


# In[34]:


mew2


# In[28]:


mew2["Belgium"] # There are two ways to index a data series, using the index name or position


# In[30]:


mew2[2]


# In[31]:


new = pd.Series([5,6,7,8], index = ["Ghana", "France", "Belgium", "England"])


# In[32]:


new


# In[35]:


mew2 + new # adds up similar rows together, for example in mew2[3] = Belguim, 7 and in new[2] = 


# ##  Data Frames

# These are a combination of many series put together, different columns are present.

# In[38]:


np.random.randint(0,100, 100) # This creates 100 random numbers


# In[46]:


y = np.random.seed(101) # This returns the same random number


# In[48]:


pd.DataFrame(randn(5,4)) # This creates a dataframe


# In[50]:


pd.DataFrame(randn(5,4), index = ["A", "B","C","D","E"], columns = ["W", "X","Y","Z"] ) #Changing the row index to a-e and the coulums to w-z


# In[57]:


r = pd.DataFrame(randn(5,4), index = ["A", "B","C","D","E"], columns = ["W", "X","Y","Z"] ) # To get the same column value of W, make sure you 
r


# In[58]:


r["W"] # indexing out a whole column in the dataset r so that you can whork soely on it


# In[98]:


r[index = "A"] # To get an entire row ()


# In[70]:


sumColumn = r[["Y","Z"]] # To index out column y and z


# In[89]:


r["addition"] = r["Y"] + r["Z"] # Adding two columns within a dataset


# In[90]:


r # This adds the addition of y and z to the original dataset


# In[91]:


r.drop('addition', axis = 1, inplace = True) # this drops the addition column


# In[92]:


r


# In[114]:


r.drop("A", axis = 0, inplace = True) # This drops row D


# In[115]:


r


# In[103]:


# To select a column use loc[name of location] or iloc[index of location]


# In[111]:


r.iloc[1] # selecting row B


# In[116]:


r.loc["B"] # Selecting row with index B


# ## Conditional Selection

# This selects a row and column of a dataset based on certain conditions

# In[117]:


r > 1 # This checks the cells that are greater than 1


# In[119]:


r [r<1]


# In[129]:


r["W"]>1


# In[132]:


r[r["W"]<1]


# ###  using .set-index 

# In[133]:


r.set_index(r["X"]) # This sets the colomn  X as an index of the data set


# ## Merging , joining and concatenation -This merges dataframes 

# In[145]:


df1 = pd.DataFrame({'A': ["A0", "A1", "A2", "A3"], "B": ["B0", "B1","B2", "B3"], "C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"]}, index = [0,1,2,3])


# In[146]:


df2 = pd.DataFrame({'A': ["A4", "A5", "A6", "A7"], "B": ["B4", "B5","B6", "B7"], "C": ["C4", "C5", "C6", "C7"], "D": ["D4", "D5", "D6", "D7"]}, index = [4,5,6,7])


# In[147]:


df3 = pd.DataFrame({'A': ["A8", "A9", "A10", "A11"], "B": ["B8", "B9","B10", "B11"], "C": ["C8", "C9", "C10", "C11"], "D": ["D8", "D9", "D10", "D11"]}, index = [8,9,10,11])


# In[148]:


df1


# In[149]:


df2


# In[150]:


df3


# ## Concatenation

# Concatenation basically glues dataframes together vertically in rows

# In[153]:


pd.concat([df1, df2, df3])  # this concatenates by rows


# In[152]:


pd.concat([df1, df2, df3], axis = 1) # this concatenates by columns


# # Merging Dataframes

# In[154]:


# pd.merge(left, right)

