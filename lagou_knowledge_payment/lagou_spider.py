__author__ = 'gengyc'
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import json
import os
os.chdir('‪C:/Users/DELL/Desktop'.strip('\u202a'))
url_start = 'https://www.lagou.com/jobs/list_%E7%9F%A5%E8%AF%86%E4%BB%98%E8%B4%B9/p-city_0?px=default#filterBox'
url_parse = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E7%9F%A5%E8%AF%86%E4%BB%98%E8%B4%B9/p-city_0?px=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

}

def fetchData(url_start,url_parse,page_Nums):

    data = {
            'first': 'true',
            'pn': str(page_Nums),
            'kd': '知识付费'
    }
    session = requests.Session()
    session.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
    cookie = session.cookies
    response = session.post(url_parse, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
    result = json.loads(response.text)['content']['positionResult']['result']
    return result


def save_to_excel(result1,result2,result3,result4):
    df = pd.DataFrame(data={'positionName':result1,'minsalary':result2,'maxSalary':result3,'asd':result4},index=[0])
    df.to_csv("./Test1.xlsx", encoding="utf-8-sig", mode="a", header=False, index=False)


if __name__ == '__main__':

    for i in range(10):
        results = fetchData(url_start,url_parse,i)
        for result in results:
            pos_Name = result['positionName']
            minsal = int(result['salary'].split('-')[0].strip('k'))*1000
            maxsal = int(result['salary'].split('-')[1].strip('k'))*1000
            city = result['city']
            save_to_excel(pos_Name,minsal,maxsal,city)





