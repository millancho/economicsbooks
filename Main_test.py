import pandas as pd
from selenium import webdriver
from getLinks import getLinks
from Cambridge import Cambridge
from Springer import Springer
from Columbia import Columbia
from Yale import Yale
from Harvard import Harvard
from MIT import MIT
from Oxford import Oxford


options=webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome('chromedriver.exe',options=options)

results = []

#CAMBRIDGE

results += list(map(Cambridge,getLinks('https://www.cambridge.org/co/academic/subjects/economics/titles?layout=listing&pageSize=100&Series=&sortOrder=answerMpubDate_unified_N%5Bdesc%5D&page=PAGE',
                                       'href="(.+?)"',
                                       'format',
                                      1)))

#SPRINGER

results += list(map(Springer,getLinks('https://www.springer.com/la/product-search/discipline?disciplineId=economics&facet-lan=lan__en&facet-type=type__book&page=PAGE&returnUrl=la%2Feconomics&topic=911020%2CS0000X%2CS11001%2CS12008%2CS13004%2CS14000%2CS15007%2CS16003%2CW00000%2CW28000%2CW28010%2CW28020%2CW29000%2CW29010%2CW29020%2CW29030%2CW31000%2CW31010%2CW31020%2CW32000%2CW33000%2CW33010%2CW34000%2CW34010%2CW34020%2CW34030%2CW35000%2CW36000%2CW37000%2CW38000%2CW39000%2CW41000%2CW42000%2CW43000%2CW44000%2CW45000%2CW45010%2CW46000%2CW47000%2CW48000%2CW48010%2CW49000%2CW49010%2CW49020%2CW51000%2CW51010%2CW52000',
                                      'a href="(.+?)"',
                                      '/la/book/',
                                     1)))

#COLUMBIA

results += list(map(Columbia,getLinks('https://cup.columbia.edu/search-results?keyword=Economics&amount=100&supapress_order=publishdate-desc&page_number=PAGE',
                                      'a href="(.+?)"',
                                      '/book/',
                                     1)))
#YALE

results += list(map(Yale,getLinks('https://yalebooks.yale.edu/search?field_book_disciplines=All&field_book_subdisciplines=All&search_api_views_fulltext=Economics&sort=field_book_publication_date%20DESC&page=PAGE',
                                      'a href="(.+?)"',
                                      '/book/',
                                     0)))

#HARVARD

results += list(map(Harvard,getLinks('https://www.hup.harvard.edu/results-list.php?hcid=9&skip=PAGE',
                                      'a href="(.+?)"',
                                      '/catalog.',
                                     0)))

#MIT

results += list(map(MIT,getLinks('https://mitpress.mit.edu/topics/economics?page=PAGE',
                                      'a href="(.+?)"',
                                      '/books/',
                                     0)))

#Oxford

results += list(map(Oxford,getLinks('https://global.oup.com/ushe/advanced_search?cc=co&lang=en&prevNumResPerPage=60&prevSortField=9&pubdateyearto=2050&pubdateyearfrom=1970&subjectcode1=3057634|SYN_00086&submitAdvSrch=Search&pubdatemonthto_default=select%20month&pubdatemonthfrom_default=select%20month&pubdatemonthto=1&resultsPerPage=60&pubdatemonthfrom=1&sortField=9&start=PAGE',
                                      'a href="(.+?)"',
                                      '/ushe/product/',
                                     0)))

df = pd.DataFrame(results)
df.to_excel('test_scraping.xlsx')


