from bs4 import BeautifulSoup as bs
import json

def Cambridge(book):
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
                    'Source':'Cambridge'}
    try:
        info = json.loads(soup.find("script",type="application/ld+json").text)
    except:
        info = None
    if info != None:
        try:
            title = info['name']
        except:
            title = ''
        try:
            date = info['datePublished']
        except:
            date = ''
        try:
            authors = ', '.join([x['name'] for x in info['author']])
        except:
            authors = ''
        try:
            isbn = info['isbn']
        except:
            isbn = ''
        try:
            description = info['description']
        except:
            description = ''
        if title != '' and isbn != '':
            return {'Title':title,
                    'Publish Date':date, 
                    'Author':authors,
                    'ISBN':isbn,
                    'Description':description, 
                    'Link':book,
                    'Source':'Cambridge'}
        
    return {'Title':'ERROR',
            'Publish Date':'ERROR', 
            'Author':'ERROR',
            'ISBN':'ERROR',
            'Description':'ERROR', 
            'Link':book,
            'Source':'Cambridge'}