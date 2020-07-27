import requests
from bs4 import BeautifulSoup
from csv import writer

html_doc = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>My Webpage</title>
    </head>
    <body>
        <div id="section-1">
            <h3 data-hello="hi">Hello</h3>
            <img src="https://source.unsplash.com/200x200/?nature,water" />
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto
                culpa cumque velit aperiam officia molestias maiores qui
                officiis incidunt. Omnis vitae eveniet reprehenderit excepturi
                officiis quod, eum natus voluptatem nihil fugit necessitatibus
                dolorum quae accusamus aliquid enim fuga dicta beatae!
            </p>
        </div>
        <div id="section-2">
            <ul class="items">
                <li class="item"><a href="#">Item 1</a></li>
                <li class="item"><a href="#">Item 2</a></li>
                <li class="item"><a href="#">Item 3</a></li>
                <li class="item"><a href="#">Item 4</a></li>
                <li class="item"><a href="#">Item 5</a></li>
            </ul>
        </div>
    </body>
</html>"""






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


