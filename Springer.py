from bs4 import BeautifulSoup as bs
import re

def Springer(book):
    tries = 1
    while True:
        if tries<4:
            try:
                browser.get('https://www.springer.com'+book)
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
                    'Link':'https://www.springer.com'+book,
                    'Source':'Springer'}
    try:
        title = re.findall('<dd itemprop="name">(.+?)</dd>',str(soup))[0]
    except:
        title = ''
    try:
        date = [x.replace('\xa0',' ').strip() for x in re.findall(':(.+?)</li>',str(soup)) if '\xa0' in x][0]
    except:
        date = ''
    try:
        authors = ', '.join([x.text for x in soup.find_all('span',{'itemprop':'name'})][:-1])
    except:
        authors = ''
    try:
        isbn = re.findall('li>ISBN(.+?)</li>',str(soup))[0].replace('-','')
    except:
        isbn = ''
    try:
        description = '. '.join(re.findall('<li>(.+?)</li>',str(soup.find('div',{'class':'usps'}))))
    except:
        description = ''
    if title != '' and isbn != '':
        return {'Title':title,
                'Publish Date':date, 
                'Author':authors,
                'ISBN':isbn,
                'Description':description, 
                'Link':'https://www.springer.com'+book,
                'Source':'Springer'}
