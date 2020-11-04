import json
from helper_functions import *
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt


fake_article = getFakeArticle(FAKE_PATH='fakenewsnet_dataset/politifact/fake')
true_article = getFakeArticle(FAKE_PATH='fakenewsnet_dataset/politifact/real')


#create a pandas with 3 columns
#table=pd.DataFrame({'text':[],'title':[],'publish_date':[]})
table = pd.DataFrame(columns=['text', 'title', 'publish_date'])
print('Real news')
for true in true_article:
    parsedData = parseArticle(true)
    toAppend = pd.DataFrame({'text':[parsedData['text']],
                  'title':[parsedData['title']],
                  'publish_date':[parsedData['publish_date']],
                  'label':['0']})#true is 0
    table = table.append(toAppend,ignore_index=True,sort=True)

print('Fake news')
for fake in fake_article:
    parsedData = parseArticle(fake)
    toAppend = pd.DataFrame({'text':[parsedData['text']],
                  'title':[parsedData['title']],
                  'publish_date':[parsedData['publish_date']],
                  'label':['1']})#false is 1
    #table = table.append(toAppend,ignore_index=True,sort=True)


#print(table)

example1=BeautifulSoup(table['text'][0],"html.parser")  #use beautifier to get the text
print(table['text'][0])
#print(example1.getText())

text_cleared=re.sub("[^a-zA-Z]"," ",example1.getText())
#print(text_cleared)



print()
lower_case=text_cleared.lower()
words=lower_case.split()
#print(words)
#print(stopwords.words("english"))
#import pdb;pdb.set_trace()

#remove stopwords from text
filtered_words=[w for w in words if not w in stopwords.words("english")]
#print(filtered_words)

#take the root of all words
from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer('english')
stops= set(stopwords.words("english"))


def review_to_words( raw_review ):
 # Function to convert a raw review to a string of words
 # The input is a single string (a raw movie review), and
 # the output is a single string (a pre-processed movie
 # review)
 #
 # 1. Remove HTML
    review_text = BeautifulSoup(raw_review,"html.parser").get_text()
 #
 # 2. Remove non-letters
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
 #
 # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
 #
 # 4. Remove stop words
    meaningful_words = [w for w in words if not w in stops]
 #
 # 5. Stem words
    stemmed_meaningful_words = [stemmer.stem(w) for w in meaningful_words]
 #
 # 6. Join the words back into one string separated by space,
 # and return the result.
 #return( " ".join( stemmed_meaningful_words ))
    return( meaningful_words)

clean_text=[];
#do the cleaning for the text that we have in the table
for i in range(0,len(table['text'])):
    clean_text.extend(review_to_words(table['text'][i]))

print("significant words")
print(clean_text)

freq=nltk.FreqDist(clean_text)
freq.plot(20,cumulative=False)
plt.show()