# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from autohome.items import TorrentItem
import json
from scrapy import log
from scrapy.selector import Selector
from scrapy.exceptions import DropItem


class MininovaSpider(CrawlSpider):

    name = 'autohome'
    allowed_domains = ['www.autohome.com.cn']
    start_urls=[]
    base_url='http://www.autohome.com/'
    f=open('scraped_id_data.json','r')
    jsonT = json.loads(f.read())
    f.close()
    for item in jsonT:
        ids=item['id']
        for mId in ids:
            start_urls.append(base_url+mId[1:])
    #start_urls = ['http://www.autohome.com']
    #rules = [Rule(LinkExtractor(allow=['cn/\d+'],deny=['\.html']), 'parse_torrent')]

    # def parse_torrent(self, response):
    #     torrent = TorrentItem()
    #     torrent['url'] = response.url
    #     koubei=response.xpath("//div[@class='koubei']")
    #     torrent['font_score']=response.xpath("//div[@class='koubei']/div[@class='koubei-score']/a[@class='font-score']/text()").extract()

    #     koubei-con-rank
    #     return torrent
    def parse(self, response):
        torrent = TorrentItem()
        torrent['sid'] = response.url.split('/')[3]
        torrent['name']=''.join(response.xpath("//div[@class='subnav-title-name']/a/h1/text()").extract())
        mKoubei=response.xpath("//div[@class='koubei']/div[@class='koubei-score']/a[@class='font-score']/text()").extract()
        if mKoubei==None:
            print 'Null'
            return None
        torrent['font_score']=''.join(mKoubei)
        con_ranks=response.xpath("//table[@class='table-rank']/tr")
        koubei_con=''
        cons=[]
        for item in con_ranks:
            con_dic={}
            title=''.join(item.xpath("th/text()").extract())
            tds=item.xpath("td")
            mRank=''.join(tds[0].xpath("a/text()").extract())+" "
            mRank+=''.join(tds[1].xpath("a/text()").extract())
            con_dic['title']=title
            con_dic['rank']=mRank
            cons.append(con_dic)
            # koubei_con+=''.join(item.xpath("th/text()").extract())+" "
            # tds=item.xpath("td")
            # koubei_con+=''.join(tds[0].xpath("a/text()").extract())+" "
            # koubei_con+=''.join(tds[1].xpath("a/text()").extract())+"\n "
        torrent['koubei_con']=cons
        #
        con_rivals=response.xpath("//table[@class='table-rival']/tr")
        #koubei_rival=''
        rivals=[]
        i=0
        for item in con_rivals:
            if i==0:
                i+=1
                continue
            i+=1
            rival_dic={}
            tds=item.xpath("td")
            title=''.join(tds[0].xpath("div/a/text()").extract())
            mRank=''.join(tds[1].xpath("div/a/text()").extract())
            rival_dic['brand']=title
            rival_dic['rank']=mRank
            rivals.append(rival_dic)
        torrent['koubei_rival']=rivals
        return torrent  
