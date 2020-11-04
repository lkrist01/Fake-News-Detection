my_api_key = "AIzaSyAhBp2Re1cUHaFA2_1On9-7eoeIQRd-7QQ"
my_cse_id = "013056498919336478417:aty8hvcobve"
from urllib.parse import urlparse
from os import listdir
import json
from os.path import isfile,join,isdir
from googleapiclient.discovery import build
from newspaper import Article
"""
Performs the google search
"""
def googleSearch(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=my_api_key)
    res = service.cse().list(q=search_term, cx=my_cse_id, **kwargs).execute()
    if not 'items' in res:#in case an error has occured , return null
        return None
    return res['items']

"""
Downloads the articles from the input url
:Returns Article parsed object if download and parsing was successful else None
"""
def downloadArticle(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except:#return None if failed
        print("Failed to download article with url:",url)
        return None
    return article
"""
Returns a list with json files containing fake articles
:param start The index of the starting folder
:param end The index of the ending folder
"""
def getFakeArticle(FAKE_PATH='fakenewsnet_dataset/politifact/fake'):
    # import pdb;pdb.set_trace()
    #first view all the folders in the given path
    folders = [folder for folder in listdir(FAKE_PATH) if isdir(join(FAKE_PATH, folder))] #is folder
    fileList = []
    #loop through each folder to read the json file
    for folder in folders:
        for file in listdir(join(FAKE_PATH,folder)):
            if isfile(join(FAKE_PATH,folder,file)):  #if file
                fileList.append(join(FAKE_PATH,folder,file))  #list with all the path from begining to the file
    return fileList

def parseArticle(articlePath):
    with open(articlePath) as json_file:
        data = json.load(json_file)
    return data

"""
Checks if the two url hosts provided are the same , using urllib
:param firstUrl the first url to be checked for equality
:param secondUrl the second url to be checked for equality
:Returns true if the two provided urls are the same
"""
def sameURL(firstUrl,secondUrl):
    firstParse = urlparse(firstUrl)
    secondParse = urlparse(secondUrl)
    return firstParse.netloc==secondParse.netloc or firstParse.path==secondParse.path
