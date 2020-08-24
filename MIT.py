from bs4 import BeautifulSoup as bs
import re

def MIT(book):
    tries = 1
    while True:
        if tries<4:
            try:
                browser.get(book)
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
                    'Link':book,
                    'Source':'MIT'}
    try:
        title = soup.find('h1', {'class':'book__title'}).text.strip()
    except:
        title = ''
    try:
        date = soup.find('time')['content']
    except:
        date = ''
    try:
        authors = soup.find('span', {'class':'book__authors'}).text.strip()
    except:
        authors = ''
    try:
        isbn = soup.find('span', {'property':'isbn'}).text
    except:
        isbn = ''
    try:
        description = soup.find('div', {'class':'l-tabs--left'}).text.strip()
    except:
        description = ''
    if title != '' and isbn != '':
        return {'Title':title,
                'Publish Date':date, 
                'Author':authors,
                'ISBN':isbn,
                'Description':description, 
                'Link':book,
                'Source':'MIT'}
