### Additional Examples

Let’s use a test scraping site: http://webscraper.io/test-sites/e-commerce/allinone/phones 

Let’s create new file called webscraperio.py 

We’re going to take the input of the webpage, run it through BeautifulSoup and parse the output using RegEx.  

First, import your modules 

```python
import requests, re 

from bs4 import BeautifulSoup 
```

Then, create the request and assign the output of it to a variable called “r” 
 
```python
r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content 
```

Now, run r through BeautifulSoup and assign it to another variable called “soup” 

```python
soup = BeautifulSoup(r, "lxml") 
```

Let’s use our soup data to find all of the links on this page. Let’s create a variable called “tags”. This variable will use soup.findAll to search through the page’s content using regular expression.  

We can change our compile code another look for specific text in the href 

```python
tags = soup.findAll("a", {"href":re.compile('(allinone)')}) 
for a in tags: 
        print(a.get('href')) 
```
 

That is pretty simple, but we can get as complex as we want. Change your regex check to something different: 

 
```python
tags = soup.findAll("a", {"href":re.compile('[<>#%|\{\}!\\^~\[\]`/]')}) 
for a in tags: 
        print(a.get('href')) 
```
 
Let’s try searching for all reviews on this page.  

Look at the page source and find the reviews. It looks like the reviews are in a “ratings” div class. Let’s try pulling that.  

 
```python
import requests, re  
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content  
soup = BeautifulSoup(r, "lxml")  
tags = soup.findAll("div", {"class":re.compile('(ratings)')})  
for p in tags:  
        a = p.findAll("p",{"class":"pull-right"})  
        print(a[0].string)  
```
 

Notice the use of the lxml parser when we define our BeautifulSoup object names “soup”.  
