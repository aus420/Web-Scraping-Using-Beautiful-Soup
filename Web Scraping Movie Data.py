#!/usr/bin/env python
# coding: utf-8

# In[22]:


from bs4 import BeautifulSoup


# In[23]:


import requests


# In[24]:


#import openpyxl


# In[26]:


#excel=openpyxl.Workbook()


# In[28]:


#print(excel.sheetnames)


# In[29]:


#sheet=excel.active


# In[30]:


#sheet.title='Top Rated Movies'


# In[31]:


#print(excel.sheetnames)


# In[32]:


#sheet.append(['Movie Rank','Movie Name','IMDB Rating'])


# In[44]:


try:
    source=requests.get('https://www.imdb.com/chart/top')
    source.raise_for_status()
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        name=movie.find('td',class_="titleColumn").a.text
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        rating=movie.find('td',class_="ratingColumn imdbRating").strong.text
        print(rank,name,rating)
        #sheet.append([rank,name,rating])
except Exception as e:
    print(e)
#excel.save('IMDB Movie Rating.xlsx')


# In[ ]:




