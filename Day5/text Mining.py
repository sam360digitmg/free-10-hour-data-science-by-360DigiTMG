# import requests   # Importing requests to extract content from a url
# from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 

import re # Regular expressions
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# load reviews data
with open("C:\\Users\\Bharani Kumar\\Downloads\\oneplusseven.txt","r",encoding="utf-8") as sw:
    rev_string = sw.read()
    
# Removing unwanted symbols incase if exists
rev_string = re.sub("[^A-Za-z" "]+", " ", rev_string).lower()
rev_string = re.sub("[0-9" "]+", " ", rev_string)

# words that contained in iphone 7 reviews
reviews_words = rev_string.split(" ")

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

temp = ["this","is","awsome","Data","Science"]
[i for i in temp if i not in "is"]

reviews_words = [w for w in reviews_words if not w in stop_words]

# Joinining all the reviews into single paragraph 
rev_string = " ".join(reviews_words)

# WordCloud can be performed on the string inputs.
# Corpus level word cloud

wordcloud_ip = WordCloud(
                      background_color='white',
                      width=2000,
                      height=1500
                     ).generate(rev_string)

plt.imshow(wordcloud_ip)

# positive words # Choose the path for +ve words stored in system
with open("C:\\Users\\Bharani Kumar\\Downloads\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
# Positive word cloud
# Choosing the only words which are present in positive words
pos_in_pos = " ".join ([w for w in reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='white',
                      width=1800,
                      height=1400
                     ).generate(pos_in_pos)

plt.figure(2)
plt.imshow(wordcloud_pos_in_pos)


# negative words  Choose path for -ve words stored in system
with open("C:\\Users\\Bharani Kumar\\Downloads\\negative-words.txt", "r") as neg:
  negwords = neg.read().split("\n")

# negative word cloud
# Choosing the only words which are present in negwords
neg_in_neg = " ".join ([w for w in reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(neg_in_neg)
plt.figure(3)
plt.imshow(wordcloud_neg_in_neg)
