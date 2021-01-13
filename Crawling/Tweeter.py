import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import re
from apyori import apriori

CONSUMER_KEY = "(input)"
CONSUMER_SECRET = "(input)"
ACCESS_TOKEN_KEY = "(input)"
ACCESS_TOKEN_SECRET = "(input)"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, timeout=180)

keyword = "손흥민"
# tweets = api.search(keyword)
# for tweet in tweets:
#     print(tweet.entities['user_mentions'],'-usermention-')
#     print(tweet.entities['hashtags'],'-hashtag-')
#     print(tweet.text, '-text-')

columns = ['created', 'tweet_text']
df = pd.DataFrame(columns=columns)

for i in range(1,10):
    print("Get data", str(i*10), "% complete..")
    tweets = api.search(keyword)
    time.sleep(0.2)
    for tweet in tweets:
        tweet_text = tweet.text
        created = tweet.created_at
        row = [created, tweet_text]
        series = pd.Series(row, index=df.columns)
        df = df.append(series, ignore_index=True)
print("Get data 100 % complete..")
print(df.head())

def text_cleaning(text):
    hangul = re.compile('[^ㄱ-ㅣ가-힣]+')
    result = hangul.sub("", text)
    return(result)

df['ko_text'] = df['tweet_text'].apply(lambda x: text_cleaning(x))
print(df.head())

from konlpy.tag import Okt
from collections import Counter

path = "(input)dateframe file path"
path = path.replace("\\", "/")
korean_stopwords_path = path+"/korean_stopwords.txt"
print(korean_stopwords_path)
with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]

def get_nouns(x):
    nouns_tagger = Okt()
    nouns = nouns_tagger.nouns(x)

    nouns = [noun for noun in nouns if len(noun) > 1]
    nouns = [noun for noun in nouns if noun not in stopwords]
    return nouns
df['nouns'] = df['ko_text'].apply(lambda x: get_nouns(x))
print(df.shape)
print(df.head())

transactions = [
    ['손흥민', '시소코'],
    ['손흥민', '케인'],
    ['손흥민','케인','포체티노']
]

results = list(apriori(transactions))
for result in results:
    print(result)
