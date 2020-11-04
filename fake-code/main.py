# from simhash import *
from sim import *
from mysql_connector import *
from helper_functions import *
from simhash import Simhash,SimhashIndex
from urllib.parse import urlparse
HOST = '127.0.0.1'
USER_NAME = 'root'
PASSWORD = ''
DATABASE = 'testing'
dbc = DBConnector(HOST,USER_NAME,PASSWORD,DATABASE)
dbc.connect()
articlePaths = getFakeArticle(start=100,end=200)
for article in articlePaths:
    parsedData = parseArticle(article)
    print("*****************")
    print("Fake article:{}\n".format(parsedData['url']))
    print("*****************")
    dbc.insertHash(parsedData['url'],Simhash(get_features(parsedData['text'])).value)  #create the simhash value
    hashesIndex = SimhashIndex(dbc.getHashes(),k=5) #how much bits different for simhash
    searchQuery = parsedData['title']
    results = googleSearch(searchQuery, num=10) #number of search in web
    if results is None:
        print("Failed searching for ",searchQuery)
        continue
    for result in results:
        print('Downloading content from link ',result['link'])
        article = downloadArticle(result['link'])
        if article is None or article.text=='' or sameURL(article.url,result['link']):
            #if an error occured during downloading of article
            #or body is empty(maybe wrong parsing) , or they are from the same url continue
            continue
        # detectDuplicate(dbc.getHashes(),simhash.compute(hashedList))
        articleHash = Simhash(get_features(article.text))
        matchedList = hashesIndex.get_near_dups(articleHash)
        if len(matchedList)>0:
            #import pdb;pdb.set_trace()
            dbc.insertDuplicates(result['link'],matchedList[0])
