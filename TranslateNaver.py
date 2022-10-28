from turtle import clear
import bs4
import requests
import re
import nltk
from googletrans import Translator

translator = Translator()


# access website, strip tags, print the text
html = "https://sports.news.naver.com/news.nhn?oid=347&aid=0000162227"
page = requests.get(html)

node = bs4.BeautifulSoup(page.content, "html.parser").find('div', id="newsEndContents")

#get the text
article_text = "".join([t for t in node.contents if type(t)==bs4.element.NavigableString]).strip()

#print(article_text)

#regex to remove punctuation
res = re.sub(r'[^\w\s]', ' ', article_text)

#tokenizes the string
article_tokenized = nltk.word_tokenize(res)

#prints each word
 
for word in article_tokenized:
    print(word) 


resultArray = []

for word in article_tokenized:
    
    result = translator.translate(word)
    resultArray.append(result.text)

print(resultArray)

