__author__ = 'gengyc'
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
plt.rcParams['axes.unicode_minus'] = False
os.chdir('‪C:/Users/DELL/Desktop'.strip('\u202a'))
data = pd.read_excel('Test.xlsx')
plt.figure(figsize=(10,6))#将画布设定为正方形，则绘制的饼图是正圆


#拉勾网各城市关于知识付费工作的最低工资分布折线图
plt.title("拉勾网各城市关于知识付费工作的最低工资分布折线图")  #设置标题
data_1 = data.groupby('city').mean()
minSalary = data_1.mean()['minSalary']
labels = data_1.index
explode = [0,0.1,0.01,0,0.2,0,0,0,0,0.01]
colors = ['red','gray','blue','yellow',
         'orange','lightblue','lintgreen',
         'purple','green','gold']
plt.pie(x=minSalary,
       explode=explode,
       labels=labels,
       colors = colors,
       autopct="%.1f%%",
       pctdistance=0.5,
       labeldistance=1.1,
       startangle=120,
       radius=1.2,
       counterclock=False,
       wedgeprops={'linewidth':1.5,'edgecolor':"green"},
       textprops={'fontsize':10,'color':'black'}
       )
plt.savefig('./拉勾网各城市关于知识付费工作的最低工资分布饼状图')


#拉勾网各城市关于知识付费工作的最低/高工资分布条形图
plt.xlabel('城市名称')
plt.ylabel('最高工资水平')
plt.title('拉勾网各城市关于知识付费工作的最高工资分布条形图')
data_1 = data.groupby('city').mean()
minSalary = data_1['maxSalary'].values
labels = data_1.index
plt.bar(x=range(0,len(minSalary)),
        height=minSalary,
        tick_label=labels,
        align='center',
        color='blue',
        )
plt.savefig('./拉勾网各城市关于知识付费工作的最高工资分布条形图')
plt.show()


