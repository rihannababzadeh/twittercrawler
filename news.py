import feedparser
from bs4 import BeautifulSoup
import requests

def get_text(fp):
    i=0
    for e in fp.entries :
        if i < 200:

            if ('Trump' in e.title or 'Trump' in e.description or 'white house' in e.description or 'potus' in e.description ):
                print('title :', e.title)
                url = e.link
                print(url)
    #response[text] is a string
                response=requests.get(url).text
    #cleandata is a beautifulsoup
                CleanData=BeautifulSoup(response,"lxml")
    #CleanData.text==get_text(CleanData) ==> get string data without markups
                   #print(CleanData.text)
                #Main_Data = CleanData.findAll('p', attrs={'itemprop': 'articleBody'})
                Main_Data = CleanData.findAll('p', attrs={'itemprop': 'articleBody'},limit=25)
                  # html = "".join(line.strip() for line in Main_Data.split("\n"))
                CleanData = BeautifulSoup(str(Main_Data), "lxml")
                print(CleanData.text+"\n")
                i+=1
        else:break

    return 1

print('******************************************Trump News***************************************'+"\n")
fp = feedparser.parse('https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml')
s = get_text(fp)