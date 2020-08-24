from bs4 import BeautifulSoup as bs
import re

def getLinks(url,href,cond, start):
    books = []
    pages = [str(i) for i in range(start,2)]
    for page in pages:
        if 'harvard' in url:
            page = str(int(page)*50)
        if 'global.uop' in url:
            page = str(int(page)*60)
        browser.get(url.replace('PAGE',page))
        html = browser.page_source
        soup = bs(html)
        links = list({x for x in re.findall(href,str(soup)) if  cond in x and 'columbia.edu' not in x})
        if links == []:
            break
        else:
            if links[-1] in books:
                break
            books += links
    return [x.split(';prevNumResPerPage',1)[0].replace('amp;','') for x in books]

