#!/usr/bin/env python
# coding: utf-8

# ## Objectives
# 

# After completing this lab you will be:
# 
# *   Familiar with the basics of the `BeautifulSoup` Python library
# *   Be able to scrape webpages for data and filter the data
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">  
#     <ul>
#         <li>
#             <a href="#Filter">Filter</a>
#             <ul>
#                 <li><a href="#find_All">find_All</a></li>
#                 <li><a href="#find">find</a></li>
#             </ul>
#         </li>
#      </ul>
#      <ul>
#         <li>
#             <a href="#Downloading-And-Scraping-The-Contents-Of-A-Web-Page">Downloading And Scraping The Contents Of A Web Page</a></li>
#          <li> <a href="#Scraping-tables-from-a-Web-page-using-Pandas">Scraping tables from a Web page using Pandas</a></li>
#     </ul>
# 
# </div>
# 
# <hr>
# 

# Import the required modules and functions
# 

# In[1]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# ## Beautiful Soup Object
# 

# We can store it as a string in the variable <code>table</code>:
# 

# In[2]:


table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td> <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> <td>300 kg</td></tr><tr><td>2</td> <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> <td>94 kg</td></tr><tr><td>3</td> <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> <td>80 kg</td></tr></table>"


# In[3]:


table_bs = BeautifulSoup(table, 'html5lib')


# ## find_All
# 

# The <code>find_all()</code> method looks through a tag's descendants and retrieves all descendants that match your filters.
# 
# <p>
# The Method signature for <code>find_all(name, attrs, recursive, string, limit, **kwargs)<c/ode>
# </p>
# 

# In[4]:


table_rows = table_bs.find_all('tr')
table_rows


# The result is a Python iterable just like a list, each element is a <code>tag</code> object:
# 

# In[5]:


first_row = table_rows[0]
first_row


# The type is <code>tag</code>
# 

# In[6]:


print(type(first_row))


# we can obtain the child
# 

# In[7]:


first_row.td


# If we iterate through the list, each element corresponds to a row in the table:
# 

# In[8]:


for i, row in enumerate(table_rows):
    print("row", i, "is", row)


# As <code>row</code> is a <code>cell</code> object, we can apply the method <code>find_all</code> to it and extract table cells in the object <code>cells</code> using the tag <code>td</code>, this is all the children with the name <code>td</code>. The result is a list, each element corresponds to a cell and is a <code>Tag</code> object, we can iterate through this list as well. We can extract the content using the <code>string</code> attribute.
# 

# In[9]:


for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('colunm', j, "cell", cell)


# If we use a list we can match against any item in that list.
# 

# In[10]:


list_input = table_bs.find_all(name=["tr", "td"])
list_input


# ### Attributes
# 

# If the argument is not recognized it will be turned into a filter on the tag's attributes. For example with the <code>id</code> argument, Beautiful Soup will filter against each tag's <code>id</code> attribute. For example, the first <code>td</code> elements have a value of <code>id</code> of <code>flight</code>, therefore we can filter based on that <code>id</code> value.
# 

# In[11]:


table_bs.find_all('td',id="flight")


# We can find all the elements that have links to the Florida Wikipedia page:
# 

# In[12]:


list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input


# If we set the <code>href</code> attribute to True, regardless of what the value is, the code finds all anchor tags with <code>href</code> value:
# 

# In[13]:


table_bs.find_all('a', href=True)


# There are other methods for dealing with attributes and other related methods. Check out the following <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01#css-selectors'>link</a>
# 
# beautifulsoap documentation in that link 
# 

# <h3 id="exer_type">Exercise: <code>find_all</code></h3>
# 

# Using the logic above, find all the anchor tags without <code>href</code> value
# 

# In[14]:


# Add response here
table_bs.find_all('a',href=False)


# ### string
# 

# With string you can search for strings instead of tags, where we find all the elments with Florida:
# 

# In[16]:


table_bs.find_all(string="Florida")


# ## find
# 

# The <code>find_all()</code> method scans the entire document looking for results. It’s useful if you are looking for one element, as you can use the <code>find()</code> method to find the first element in the document. Consider the following two tables:
# 

# In[17]:


get_ipython().run_cell_magic('html', '', "<h3>Rocket Launch </h3>\n\n<p>\n<table class='rocket'>\n  <tr>\n    <td>Flight No</td>\n    <td>Launch site</td> \n    <td>Payload mass</td>\n  </tr>\n  <tr>\n    <td>1</td>\n    <td>Florida</td>\n    <td>300 kg</td>\n  </tr>\n  <tr>\n    <td>2</td>\n    <td>Texas</td>\n    <td>94 kg</td>\n  </tr>\n  <tr>\n    <td>3</td>\n    <td>Florida </td>\n    <td>80 kg</td>\n  </tr>\n</table>\n</p>\n<p>\n\n<h3>Pizza Party</h3>\n  \n    \n<table class='pizza'>\n  <tr>\n    <td>Pizza Place</td>\n    <td>Orders</td> \n    <td>Slices </td>\n   </tr>\n  <tr>\n    <td>Domino's Pizza</td>\n    <td>10</td>\n    <td>100</td>\n  </tr>\n  <tr>\n    <td>Little Caesars</td>\n    <td>12</td>\n    <td >144 </td>\n  </tr>\n  <tr>\n    <td>Papa John's </td>\n    <td>15 </td>\n    <td>165</td>\n  </tr>")


# We store the HTML as a Python string and assign <code>two_tables</code>:
# 

# In[18]:


two_tables="<h3>Rocket Launch </h3> <p><table class='rocket'> <tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr> <tr><td>1</td><td>Florida</td><td>300 kg</td></tr> <tr><td>2</td><td>Texas</td><td>94 kg</td></tr> <tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party</h3> <table class='pizza'> <tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr> <tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr> <tr><td>Little Caesars</td><td>12</td><td >144 </td></tr> <tr><td>Papa John's</td><td>15 </td><td>165</td></tr>"


# We create a <code>BeautifulSoup</code> object  <code>two_tables_bs</code>
# 

# In[19]:


two_tables_bs = BeautifulSoup(two_tables, 'html.parser')


# We can find the first table using the tag name table
# 

# In[20]:


two_tables_bs.find("table")


# We can filter on the class attribute to find the second table, but because class is a keyword in Python, we add an underscore to differentiate them.
# 

# In[21]:


two_tables_bs.find("table", class_='pizza')


# <h2 id="DSCW">Downloading And Scraping The Contents Of A Web Page</h2> 
# 

# We Download the contents of the web page:
# 

# In[22]:


url = "http://www.ibm.com"


# We use <code>get</code> to download the contents of the webpage in text format and store in a variable called <code>data</code>:
# 

# In[23]:


data = requests.get(url).text


# We create a <code>BeautifulSoup</code> object using the <code>BeautifulSoup</code> constructor
# 

# In[32]:


soup = BeautifulSoup(data, "html5lib")  # create a soup object using the variable 'data'


# Scrape all links
# 

# In[25]:


for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))


# ### Scrape all images Tags
# 

# In[26]:


for link in soup.find_all('img'):  # in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# ### Scrape data from HTML tables
# 

# In[27]:


# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# Before proceeding to scrape a web site, you need to examine the contents and the way data is organized on the website. Open the above url in your browser and check how many rows and columns there are in the color table.
# 

# In[33]:


# get the contents of the webpage in text format and store in a variable called data
data = requests.get(url).text


# In[34]:


soup = BeautifulSoup(data, "html5lib")


# In[36]:


# find a html table in the web page
table = soup.find('table')  # in html table is represented by the tag <table>
table


# In[37]:


# Get all rows from the table
for row in table.find_all('tr'):  # in html table row represented by tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td')  # in html a column is represented by tag <td>
    color_name = cols[2].string  # store the value in column 3 as color_name
    color_code = cols[3].text  # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))


# ## Scraping tables from a Web page using Pandas
# 

# Particularly for extracting tabular data from a web page, you may also use the `read_html()` method of the Pandas library. 
# 

# In[38]:


# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# You may extract all the tables from the given webpage simply by using the following commands.
# 

# In[39]:


import pandas as pd

tables = pd.read_html(url)
tables


# `tables` is now a list of dataframes representing the tables from the web page, in the sequence of their appearance. In the current  URL, there is only a single table, so the same can be accessed as shown below.
# 

# In[40]:


tables[0]

