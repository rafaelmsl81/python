#!/usr/bin/env python
# coding: utf-8

# In[1]:


original_file = input('Name of original file? ')
with open(original_file) as file:
    data = file.read()


# In[5]:


def get_upper_words(text):
    uppers = []
    for word in text.split():
        if word[0].isupper():
            uppers.append(word)
    return uppers


# In[9]:


def check_sigla(text):
    uppers = get_upper_words(text)
    siglas = []
    for i in uppers:
        count = 0
        for c in i:
            if c.isupper():
                count += 1
        if count > 1:
            siglas.append(i)
        count = 0
    return siglas


# In[10]:


def write_siglas_file(text):
    siglas = check_sigla(text)
    new_filename = input('New filename? ')
    fh = open(new_filename, 'w')
    for i in siglas:
        fh.write(i + ',')
    fh.close()


# In[11]:


write_siglas_file(data)


# In[ ]:




