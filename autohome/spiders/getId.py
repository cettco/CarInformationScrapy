from scrapy.contrib.spiders import CrawlSpider
from autohome.items import IdItem
import string

class GetIdSpider(CrawlSpider):

    name = 'getIds'
    allowed_domains = ['www.autohome.com.cn']
    start_urls=[]
    base_url='http://www.autohome.com.cn/grade/carhtml/'
    i=0
    # for i in ['z']:
    #     start_urls.append(base_url+i+'.html')
    for i in list(string.ascii_lowercase):
        start_urls.append(base_url+i+'.html')
    #start_urls = ['http://www.autohome.com']
    #rules = [Rule(LinkExtractor(allow=['cn/\d+'],deny=['\.html']), 'parse_torrent')]
    def parse(self, response):
        torrent = IdItem()
        torrent['id'] = response.xpath("//li/@id").extract()
        #k=response.xpath("//li/@id").extract()
        #torrent['font_score']=response.xpath("//div[@class='koubei']/div[@class='koubei-score']/a[@class='font-score']/text()").extract()
        return torrent  