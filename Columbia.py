from bs4 import BeautifulSoup as bs
import re

def Columbia(book):
    tries = 1
    while True:
        if tries<4:
            try:
                browser.get('https://cup.columbia.edu'+book)
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
                    'Link':'https://cup.columbia.edu'+book,
                    'Source':'Columbia'}
    try:
        title = soup.find('h1',{'class':'title'}).text
    except:
        title = ''
    try:
        date = soup.find('p',{'class':'pubdate'}).text.replace('Pub Date:','').strip()
    except:
        date = ''
    try:
        authors = soup.find('p',{'class':'author'}).text.replace('Edited by','').strip()
    except:
        authors = ''
    try:
        isbn = soup.find('p',{'class':'isbn'}).text.replace('ISBN:','').strip()
    except:
        isbn = ''
    try:
        description = soup.find('div',{'class':'sp__the-description'}).text
    except:
        description = ''
    if title != '' and isbn != '':
        return {'Title':title,
                'Publish Date':date, 
                'Author':authors,
                'ISBN':isbn,
                'Description':description, 
                'Link':'https://cup.columbia.edu'+book,
                'Source':'Columbia'}
