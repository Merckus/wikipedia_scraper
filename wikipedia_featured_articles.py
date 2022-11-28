import re
import requests
from bs4 import BeautifulSoup as bs
import csv

headers = {'zzz'}
url = 'https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/'

year_range = list(range(2005, 2010))
months = ['January_', 'February_', 'March_', 'April_', 'May_', 'June_',
          'July_', 'August_', 'September_', 'October_', 'November_', 'December_']

url_list = []
articles = []


for year in year_range:
    for month in months:
        url_list.append(f'{url}{month}{year}')

for i in url_list:
    page = requests.get(i, headers=headers)
    page_content = page.content
    soup = bs(page_content, 'html.parser')
    body = soup.find('div', class_="mw-parser-output")
    pees = body.find_all('p')
    for p in pees[5:]:
        row = {}
        try:
            if re.match(r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})", p.text):
                a = f'{p.text.strip()} {i[-4:]}'
                #articles.append(row)
        except AttributeError:
            continue
        if '\n' in a:
            continue
        row['Date'] = a
        try:
            p = p.find('b')
            p = p.find('a', href=True)
            if len(p.text) > 0:
                row['Title'] = p.text
                sci_page = requests.get('https://en.wikipedia.org/' + p['href'], headers=headers)
                sci_page_content = sci_page.content
                sci_soup = bs(sci_page_content, 'html.parser')
                sci_paragraph = sci_soup.find_all('p')
                names = []
                for p in sci_paragraph:
                    a = p.text
                    b = len(a)
                    names.append(b)
                row['Length'] = sum(names)
            articles.append(row)
        except AttributeError:
            continue

with open(f'featured_articles2005-2009.csv', 'w+', encoding='utf-8') as file:
    fieldnames = ['Date', 'Title', 'Length']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in articles:
        writer.writerow(item)



