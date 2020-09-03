# -*- coding: utf-8 -*-
import scrapy


class JooblebilisimSpider(scrapy.Spider):
    name = 'jooblebilisim'
    allowed_domains = ['tr.jooble.org']
    start_urls = ['https://tr.jooble.org/iş-ilanları-bilişim?p=1/']

    def parse(self, response):
        for product in response.xpath("//div[@class = 'result saved paddings']"):
            yield{
                'title' : product.xpath('normalize-space(.//a[@class= "link-position job-marker-js"])').get(),
                'company' : product.xpath(".//span[@class= 'gray_text company-name']/text()").get(),
                'date' : product.xpath('normalize-space(.//div[@class= "date_from_creation"])').get(),
                'location' : product.xpath('normalize-space(.//span[@class= "serp_location__region"])').get(),

            }

        

         
            
                    
        for x in range(2,50):
            
            next_page = "https://tr.jooble.org/iş-ilanları-bilişim?p="+ str(x)
            yield scrapy.Request(url=next_page, callback=self.parse)
