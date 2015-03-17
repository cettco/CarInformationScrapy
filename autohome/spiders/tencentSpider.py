# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from autohome.items import TencentItem
import json
from scrapy import log
from scrapy.selector import Selector
from scrapy.exceptions import DropItem


class TencentSpider(CrawlSpider):

    name = 'tencent'
    allowed_domains = ['cgi.data.auto.qq.com/']
    start_urls=[]
    base_url='http://cgi.data.auto.qq.com/php/index.php?mod=wom&serial='
    f=open('tencent_sid.json','r')
    jsonT = json.loads(f.read())
    f.close()
    for item in jsonT:
        sid=item['serialID']
        start_urls.append(base_url+str(sid)+"&pos=top&class=1")

    def parse(self, response):
        torrent = TencentItem()
        torrent['sid'] = (response.url.split('&')[1]).split('=')[1]
        torrent['name']=''.join(response.xpath("//a[@class='nav_two_level_a_b']/text()").extract())
        yqlist=response.xpath("//dl[@class='yqlist cl']/dd/text()").extract()
        #koubei_rival=''
        # comment=[]
        # for item in yqlist:
        #     dd=item.xpath("dd/text()").extract()
        #     comment.append(dd)
        torrent['comment']=yqlist
        return torrent  
