import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime


def main():
    yahoo_url = "https://news.yahoo.co.jp/topics/business"


    html =requests.get(yahoo_url)
    soup = BeautifulSoup(html.content,"html.parser")
    #print(soup)

    """
    # title、h2、liタグを検索して、その文字列を表示する
    print(soup.find("title").text)    # タグを検索して表示
    print(soup.find("h2").text)       # .textを追加
    print(soup.find("li").text)
    """


    #class_list = soup.find_all(class_="newsFeed_item_title")
    url_list = soup.find_all("a")
    date_list =soup.find_all(class_="newsFeed_item_date")

    tmp1_list=[]
    for date in date_list:
        tmp1_list.append(date.text)

    #tmp2_list=[]
    #for c in class_list:
    #    tmp2_list.append(c.text)


    tmp3_list=[]
    for url in url_list:
        link = url.get("href")
        if "pickup" in link and len(tmp3_list) < 25:
            tmp3_list.append(link)


    url_list=[]
    title_list=[]
    for tmp3 in tmp3_list:
        time.sleep(4)
        html = requests.get(tmp3)
        soup2 = BeautifulSoup(html.content,"html.parser")
        next_link = soup2.find_all("a")
        title_list.append(soup2.find("title").text)

        count=0
        for next in next_link:
            URL = next.get("href")
            if "https://headlines" in URL:
                count+=1
                if count==1:
                    continue
                elif count >2:
                    break
                url_list.append(URL)


    #print(len(tmp1_list),len(tmp2_list),len(url_list))

    topic_info ={'日付':tmp1_list,'タイトル':title_list,'URL':url_list}
    df = pd.DataFrame(topic_info)
    df.to_csv(str(datetime.date.today())+'.csv', encoding='utf_8_sig')


if __name__=='__main__':
    main()
