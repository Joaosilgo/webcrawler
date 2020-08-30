



# web crawler 🎯


[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Joaosilgo/webcrawler)



Retrive text data from a dummy website and post on a file
Csv 


## Imports

BeautifulSoup

Writer

````python 

import requests
from bs4 import BeautifulSoup
from csv import writer


````



## Code
``````python


response = requests.get('https://webscraper.io/blog/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='blogno')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='titleblog').get_text().replace('\n', '')
        link = post.find('a')['href']
        date = post.select('.date')[0].get_text()
        csv_writer.writerow([title, link, date])



``````





> py -3 -m venv .venv
.venv\scripts\activate

> python -m pip install bs4

> pip install requests








