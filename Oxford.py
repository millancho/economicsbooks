from bs4 import BeautifulSoup as bs
import re

def Oxford(book):
    tries = 1
    while True:
        if tries<4:
            try:
                browser.get('https://global.oup.com'+book)
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
                    'Link':browser.current_url,
                    'Source':'Oxford'}
        
    info = soup.find('div', {'class':'content_block marginLeft195'})
    if info != None:
        try:
            title = re.findall('id="content">(.+?)</h1>',str(info))[0].strip()
        except:
            title = ''
        try:
            date = re.findall('Date - (.+?)</p>',str(info))[0].strip()
        except:
            date = ''
        try:
            authors = re.findall('<br/>(.+?)</p>',str(info))[0].strip()
        except:
            authors = ''
        try:
            isbn = re.findall('ISBN: (.+?)</p>',str(info))[0].strip()
        except:
            isbn = ''
        try:
            description = soup.find('div', {'id':'fragment-1'}).text.strip()
        except:
            description = ''
        if title != '' and isbn != '':
            return {'Title':title,
                    'Publish Date':date, 
                    'Author':authors,
                    'ISBN':isbn,
                    'Description':description, 
                    'Link':browser.current_url,
                    'Source':'Oxford'}
    else:
        return {'Title':'Error accessing the URL',
                    'Publish Date':'Error accessing the URL', 
                    'Author':'Error accessing the URL',
                    'ISBN':'Error accessing the URL',
                    'Description':'Error accessing the URL', 
                    'Link':browser.current_url,
                    'Source':'Oxford'}