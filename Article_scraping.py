import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime

def main():
    filename= str(datetime.date.today())
    df = pd.read_csv(filename+".csv")
    #print(df["URL"])

    articles=[]
    title_list=[]

    for url in df["URL"]:
        html =requests.get(url)
        soup = BeautifulSoup(html.content,"html.parser")

        title = soup.find("title")
        title_list.append(title.text)

        paragraph_list =soup.find_all("p")

        article=""
        count=0
        for p in paragraph_list:
            if p.text =="Yahoo!ニュース 特設ページ":
                break
            if count>4:
                article += p.text

            count+=1

        articles.append(article)

    topic_info ={'タイトル':title_list,'記事':articles}
    df = pd.DataFrame(topic_info)
    df.to_csv("EX_&_"+str(filename)+'.csv', encoding='utf_8_sig')




if __name__=='__main__':
    main()
