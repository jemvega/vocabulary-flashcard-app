#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series, DataFrame


# In[2]:


# Load vocabulary list
words = pd.read_csv("vocabulary-flashcard-vocabulary-list.csv", encoding='latin-1')
words.head(6)


# In[3]:


# Need to remove leading spaces in definition column to sort values alphabetically
words["Definition"] = words["Definition"].apply(lambda x: x.lstrip())
words.head(6)


# In[4]:


# Need to capitalize first word in definitons for consistency
# NOTE: words are intentionally left lowercase
words["Definition"] = words["Definition"].apply(lambda x: x.capitalize())
words.head(6)


# In[5]:


# Need to remove leading spaces in Word column to sort values alphabetically
words["Word"] = words["Word"].apply(lambda x: x.lstrip())
words.head(6)


# In[6]:


sorted_words = words.sort_values("Word")
sorted_words.head(6)


# In[7]:


# Need to reset index of words and definitions once in alphabetical order
sorted_words = sorted_words.reset_index()
sorted_words.head(6)


# In[8]:


# Need to drop previous index of words and definitions after resetting index and sorting words in alphabetical order
sorted_words.drop("index", axis = 1, inplace = True)
sorted_words.head(6)


# In[9]:


def check_duplicates(list_of_words):
    result = False
    setofwords = set()
    for elem in list_of_words:
        if elem in setofwords:
            result = True
        else: 
            setofwords.add(elem)
    if result == True:
        print("This list contains duplicated words.")
    elif result == False:
        print("There are no duplicate words.")

check_duplicates(sorted_words["Word"])


# In[10]:


# Need to show which words are duplicated
# Select duplicate rows except first occurrence based on all columns
duplicate_df = sorted_words[sorted_words.duplicated(['Word'], keep = False)]
duplicate_df.head(6)


# In[11]:


# Need to create two different dataframes to merge duplicated values
# Select duplicate rows except first occurrence based on all columns
duplicate_df_first = sorted_words[sorted_words.duplicated(['Word'], keep = 'first')]
duplicate_df_first.head(6)


# In[12]:


# Need to create two different dataframes to merge duplicated values
# Select duplicate rows except first occurrence based on all columns
duplicate_df_last = sorted_words[sorted_words.duplicated(['Word'], keep = 'last')]
duplicate_df_last.head(6)


# In[13]:


duplicate_rows = duplicate_df.reset_index()
duplicate_rows.drop("index", axis = 1, inplace = True)
duplicate_rows.head(6)


# In[14]:


merge_words = pd.merge(duplicate_df_first, duplicate_df_last, on = ['Word'])
merge_words.head(6)


# In[15]:


merge_words['Definition'] = merge_words[["Definition_x", "Definition_y"]].apply(lambda x: "; ".join(x), axis=1)
merge_words.head(6)


# In[16]:


merge_words.drop(["Definition_x", "Definition_y"], axis = 1, inplace = True)
merge_words.head(6)


# In[17]:


duplicates_dropped = sorted_words.drop_duplicates(["Word"], keep = False)
duplicates_dropped.head(6)


# In[18]:


vocabulary_list = pd.concat([duplicates_dropped, merge_words])
vocabulary_list.head(6)


# In[19]:


# Sorting word values alphabetically again
vocabulary_list = vocabulary_list.sort_values("Word")
vocabulary_list.head(6)


# In[20]:


# Need to reset index of words and definitions once in alphabetical order again
# Need to drop previous index of words and definitions after resetting index and sorting words in alphabetical order
vocabulary_list = vocabulary_list.reset_index()
vocabulary_list.drop("index", axis = 1, inplace = True)
vocabulary_list.head(6)


# In[21]:


# Need to double check for duplicates again
def check_duplicates(list_of_words):
    result = False
    setofwords = set()
    for elem in list_of_words:
        if elem in setofwords:
            result = True
        else: 
            setofwords.add(elem)
    if result == True:
        print("This list contains duplicated words.")
    elif result == False:
        print("There are no duplicate words.")

check_duplicates(vocabulary_list["Word"])


# In[22]:


vocabulary_list = vocabulary_list.set_index('Word')


# In[23]:


vocabulary_list.head(6)


# In[ ]:


# Need to create a copy of sorted and cleaned vocabulary that is different from raw data .csv file 
vocabulary_list.to_csv(r'C:\Users\jacqu\Desktop\Python Portfolio\Vocabulary Flashcard Quiz\vfq vocabulary list.csv')

