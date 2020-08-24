from bs4 import BeautifulSoup as bs
import re

def Harvard(book):
    tries = 1
    while True:
        if tries<4:
            try:
                browser.get('https://www.hup.harvard.edu'+book)
                html = browser.page_source
                soup = bs(html)
                break
            except:
                tries += 1
                pass
        else:
            return {'Title':'Error accessing the URL',
                    'Publish Date':'Error accessing the URL', 
                    'Author':'Error accessing the URL',
                    'ISBN':'Error accessing the URL',
                    'Description':'Error accessing the URL', 
                    'Link':'https://www.hup.harvard.edu'+book,
                    'Source':'Harvard'}
    try:
        title = soup.h1.text.strip()
    except:
        title = ''
    try:
        date = re.findall('Publication Date: (.+?)</p>',str(soup))[0]
    except:
        date = ''
    try:
        authors = ', '.join([x.text for x in soup.find_all('h3')])
    except:
        authors = ''
    try:
        isbn = book[18:]
    except:
        isbn = ''
    try:
        description = soup.find('div', {'id':'content'}).text.strip()
    except:
        description = ''
    if title != '' and isbn != '':
        return {'Title':title,
                'Publish Date':date, 
                'Author':authors,
                'ISBN':isbn,
                'Description':description, 
                'Link':'https://www.hup.harvard.edu'+book,
                'Source':'Harvard'}
