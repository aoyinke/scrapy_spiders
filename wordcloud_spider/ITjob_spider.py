__author__ = 'gengyc'
# -*- coding: utf-8 -*-

import requests
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
url = "https://zhaopin.baidu.com/api/qzasync?query=%E6%99%BA%E8%83%BD%E6%8B%9B%E8%81%98&city=%E5%B8%B8%E5%B7%9E&is_adq=1&pcmod=1&token=%3D%3DwkmGLpG76oHeoadOZmWqGasVmaFaYnihGaSiZZtt5Y&pn={}&rn=20"
path = r"test.txt"

def get_data(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
               'Cookie':'BIDUPSID=945A1A6DAC6F23B8AEC63B35F1496D48; PSTM=1541552217; BAIDUID=5EB50D8754858698B078CFF8A9540802:FG=1; BDUSS=zkzYzl-bEZjbDViSWtpR2Q2fnBBTkpFZmVySVdlY1c1b28wbzV0RjI5Y1BhRDVlRVFBQUFBJCQAAAAAAAAAAAEAAABMbNnizOzMw83At~I3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA~bFl4P2xZeT; delPer=0; PSINO=7; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[uUYFSS3d-DY]=mk3SLVN4HKm; BCLID=8625417288947489124; BDSFRCVID=KntOJeC62iJtZWoubFdBhHjeK2KaQdjTH6aoEdHgPLPZeEw2a2UVEG0PeM8g0KubcYoEogKKL2OTHm8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJkt_K-5JKvjD4-k247Hhn8thmT22-us52rt2hcH0KLKM-b90jQG5tDzQlO3BPT-Wbri3xje2fb1MRjvMtTx0pTLeq6JqpTtQC3XVp5TtUJ18DnTDMRhqtIsXpbyKMniBnr9-pnEfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuD6DBDjc0DG8s-njKKKIX_Cj_ab__Hn7zeUR_5M4pbt-qJtcZbNQUW-5t3JbIjhnFbf4KyP_ubM6nBT5Ka2Tban3xBUJAeq56D4LK3qKkQN3TKxuO5bRiLRoJyR7pDn3oyUkKXp0nhH7ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJUutfD7H3KCbtDIMhM5; ZP_FR=aladdin-5463-zp_exact_new; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0'}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    data = json.loads(res.text)
    return data





if __name__ == "__main__":
    for i in range(40,50):
        try:
            file = open(path,'a+')
            url = url.format(i*20)
            data = get_data(url)['data']['disp_data']
            for item in data:
                print(item['title'],item['education'])
                file.write(item['title']+'\n' + '  ' + item['education'])
        except:
            print("="*30)
    file.close()

