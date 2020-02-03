__author__ = 'gengyc'
# -*- coding: utf-8 -*-
import jieba  #分词
import matplotlib.pyplot as plt #数据可视化
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS  #词云的参数
import numpy as np  #科学计算
from PIL import Image  #处理图片


#打开文本
textfile = open('test.txt').read() #读取文本内容
wordlist = jieba.cut_for_search(textfile)  #分割
space_list = " ".join(wordlist)
background = np.array(Image.open("timg.jpg"))   #背景图片
mywordcloud = WordCloud(background_color="black",
                        mask=background,
                        max_words=20,
                        stopwords=STOPWORDS,
                        font_path='simkai.ttf',
                        max_font_size=200,
                        random_state=50,
                        scale=2).generate(space_list) #shengchengciyun

image_color = ImageColorGenerator(background)
plt.imshow(mywordcloud)
plt.axis("off")
plt.show()

