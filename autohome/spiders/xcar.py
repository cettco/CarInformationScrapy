# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from autohome.items import XcarItem
import json
from scrapy import log
from scrapy.selector import Selector
from scrapy.exceptions import DropItem
import Model
import sys
import re
reload(sys)
sys.setdefaultencoding='utf-8'


class XcarSpider(CrawlSpider):

    name = 'xcar'
    allowed_domains = ['newcar.xcar.com.cn']
    start_urls=[]
    base_url='http://newcar.xcar.com.cn/'
    f=open('brand.txt','r')
    context = f.read()
    brands=context.split(',')
    i=0
    n=len(brands)
    while i<n:
        id=brands[i]
        models= (Model.getModel(id).encode('utf-8')).split(',')
        j=0
        m=len(models)
        while j<m:
            car_id=models[j]
            start_urls.append(base_url+car_id+"/review/2/0.htm")
            j+=2
        i+=2

    def parse(self, response):
        torrent = XcarItem()
        print response.url
        sid = response.url.split('/')[3]
        torrent['sid']=sid
        brand = (''.join(response.xpath("//li[@id='nav_pb']/em/a/text()").extract())).replace("'",'')
        brand = re.sub(r'[\t\n\r]','',brand)
        model = (''.join(response.xpath("//li[@id='nav_ps']/em/a/text()").extract())).replace("'",'')
        model = re.sub(r'[\t\n\r]','',model)
        print brand
        print model
        if not brand in model:
            model=brand+model
        #print model
        torrent['name']=model
        torrent['comment']=response.xpath("//div[@class='review_comments_dl']/dl/dt/a/text()").extract()

        return torrent  
