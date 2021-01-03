# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YenibirisSpider(CrawlSpider):
    name = 'yenibiris'
    allowed_domains = ['www.yenibiris.com']
    start_urls = [
        'https://www.yenibiris.com/is-ilanlari/tam-zamanli?sayfa-boyutu=100/']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//div[@class = 'jobTitleLnk jobHoover']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
          'title' : response.xpath(".//h1/text()").get(), 
          'company': response.xpath(".//div[@class = 'col-lg-10 col-md-10 col-sm-10']/div[@class = 'companyTitle' ]/a/text()").get(),
          'istanımı': response.xpath("normalize-space(string(//div[@class = 'mb20']))").get(),
          'aranannitelikler': response.xpath("normalize-space(string(//div[@class = 'mb20'][2]))").get(), 
          'Pozisyon': response.xpath(".//div[@class = 'col-lg-10 col-md-10 col-sm-10']/h1/text()").get(),
          'Sektör': response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Sektör')]/span[@class = 'col-lg-8 col-md-8 col-sm-8 col-xs-12']/a/text()").get(),
          'PozisyonSeviyesi': response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Pozisyon')][2]/span[@class = 'col-lg-8 col-md-8 col-sm-8 col-xs-12']/a/text()").get(),
          'Kategori': response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Kategori')]/span[@class = 'col-lg-8 col-md-8 col-sm-8 col-xs-12']/a/text()").get(),
          'ÇalışmaŞekli':  response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Çalışma Şekli')]/span[@class = 'col-lg-8 col-md-8 col-sm-8 col-xs-12']/a/text()").get(),
          'ÇalışmaYeri':  response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Çalışma Yeri')]/span[@class = 'col-lg-8 col-md-8 col-sm-8 col-xs-12']/a/text()").get(),
          'İlanTarihi':   response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'İl')]/span[2]/text()").get(),
          'GüncellemeTarihi': response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'G')]/span[2]/text()").get(),
          'SonBasvuruTarihi': response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'So')]/span[2]/text()").get(),
          'Maas' : response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Ma')]/span[2]/text()").get(),
          'Deneyim':  response.xpath(".//div[@class = 'well additionInfos mb0 borderBox']/ul[@class = 'list-unstyled']/li[starts-with(. , 'Den')]/span[@class = 'col-lg-8 col-md-8 col-sm-8 col-xs-12']/a/text()").get(),
          'Site':   response.xpath(".//div[@class = 'footerBottomTxt']/div[@class = 'container']/div[@class = 'row']/div[@class = 'col-lg-5 col-md-12 col-sm-12 footerBottomFirstCol']/div[@class = 'cl-2']/text()").get(),
        
            
         }
        
       
        for x in range(2, 91):

            next_page = "https://www.yenibiris.com/is-ilanlari?sayfa-boyutu=100&sayfa=" + \
                str(x)
            yield scrapy.Request(url=next_page, callback=self.parse)
