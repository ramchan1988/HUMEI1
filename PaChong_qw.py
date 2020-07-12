from urllib import request
import re
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
#import scrapy

def html1(self):

    url_0 = "http://www.leyushop.cn/SubCategory?keywords="
    name_ = self
    url_1 = url_0 + name_
    url = []
    url.append(url_1)
    print(url)

    # ======================================================
    html1 = requests.get(url_1)


    # ======================================================

    paname = re.compile(r'<div class="category_pro_name".+?>(.+?)</a></div>')
    optionname = paname.findall(html1.text)

    paprice = re.compile(r'<span id=".+?>(.+?)</span></strong></p><em>')
    optionprice = paprice.findall(html1.text)
    print(optionprice)

    #page=re.compile(r'<span id=".+?>(.+?)</span></strong></p><em>')
    #page=re.compile(r'<div class="page">.+?<span class="page-skip">第1/(.+?)页')
    #optionpage = page.findall(html1.text)
    #print("page",optionpage)



    # 用numpy 把列表字符串转成数字
    low_ndarray = np.array(optionprice)
    low_ndarray = low_ndarray.astype(np.float).tolist()
    print(low_ndarray)
    # 用numpy 把列表字符串转成数字

    se = pd.Series(optionname, low_ndarray)
    print(se)
    se = se.sort_index()
    try:
        se.to_csv("data_test_name_2.csv")
        data = pd.read_csv("data_test_name_2.csv")
        sl = data.values.tolist()
        # sl=str(sl)

        name_id = [str(sl[i][0]) for i in range(len(sl))]
        # print(name_id)
        name_data = [str(sl[i][1]) for i in range(len(sl))]
        # print(name_data)
        # print(len(name_id))

        s = ''
        for i in range(len(name_id)):
            s = s + "<tr><td>" + str(i + 1) + "</td><td>" + name_data[i] + "</td><td>" + name_id[i] + "</td></tr>"
            # print(i,s)
        a = s
        print(a)
        return a

    except:
        return "找不到"

    a = ""
    # print(len(optionname))
    for i in range(len(optionname)):
        b = optionname[i] + "  " + optionprice[i] + "元" + "<br>"
        # print(b)
        a = a + b
        # print("c", a)

    # return a

def a(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (WindowsNT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/78.0.3904.108 Safari/537.36"}
    req = request.Request(url, headers=headers)
    try:
        response = request.urlopen(req)
        resHtml = response.read()
        resHtml = resHtml.decode("utf-8", 'ignore')
        soup = BeautifulSoup(resHtml, 'lxml')
        soup=soup.select('.page')
        #print(soup)
        #soup=soup[0].select('.page-skip')
        print(soup)
        page_skip=re.compile(r'<span class="page-skip">第1/(.+?)页 共170记录<input')
        optionpage = page_skip.findall(str(soup[0]))
        print("page",optionpage[0])


    except Exception as e:
        print(e)


if __name__ == '__main__':
    #print(html1("奶粉"))
    a("http://www.leyushop.cn/SubCategory?keywords=%E9%9B%85%E8%AF%97%E5%85%B0%E9%BB%9B")

