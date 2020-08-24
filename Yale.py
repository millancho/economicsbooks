from bs4 import BeautifulSoup as bs
import re

def Yale(book):
    tries = 1
    while True:
        if tries<4:
            try:
                browser.get('https://yalebooks.yale.edu'+book)
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
                    'Link':'https://yalebooks.yale.edu'+book,
                    'Source':'Yale'}
    try:
        title = soup.find('h1',{'id':'page-title'}).text.strip()
    except:
        title = ''
    try:
        date = soup.find('span',{"datatype":"xsd:dateTime"}).text
    except:
        date = ''
    try:
        authors = soup.find('span',{"class":"t-text"}).text
    except:
        authors = ''
    try:
        isbn = re.findall('ISBN:</span>(.+?)<br/>',str(soup.find('div',{'class':'col1'})))[0].strip()
    except:
        isbn = ''
    try:
        description = soup.find('section',{"class":"book-description"}).text.strip()
    except:
        description = ''
    if title != '' and isbn != '':
        return {'Title':title,
                'Publish Date':date, 
                'Author':authors,
                'ISBN':isbn,
                'Description':description, 
                'Link':'https://yalebooks.yale.edu'+book,
                'Source':'Yale'}