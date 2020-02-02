# -*- coding: utf-8 -*-
import scrapy
from IpFreePool.items import IpfreepoolItem

class IpSpiderSpider(scrapy.Spider):
    name = 'Ip_spider'
    allowed_domains = ['www.kuaidaili.com/free/']
    start_urls = ['https://www.kuaidaili.com/free/inha/3/']
    items = IpfreepoolItem()
    def parse(self, response):
        trs = response.xpath("//div[@id='list']/table//tr")

        for tr in trs:
            self.items['IP'] = tr.xpath("td[@data-title='IP']/text()").extract_first()
            self.items["PORT"] = tr.xpath("td[@data-title='PORT']/text()").extract_first()
            self.items["ProxyDegree"] = tr.xpath("td[@data-title='匿名度']/text()").extract_first()
            ResSpeed = tr.xpath("td[@data-title='响应速度']/text()").extract_first()
            if(ResSpeed):
                self.items['ResSpeed'] = ResSpeed.replace('秒','')
                if(float(self.items['ResSpeed']) <=1.0):
                    yield self.items
