# -*- coding: utf-8 -*-
import scrapy


 

class Job1Spider(scrapy.Spider):
    name = 'job1'
    allowed_domains = ['tr.jooble.org']
    start_urls = ['https://tr.jooble.org/i%C5%9F-ilanlar%C4%B1-bilgisayar-m%C3%BChendisi?p=1']
    

    def parse(self, response):
        for product in response.xpath("//div[@class = 'result saved paddings']"):
            yield{
                'title' : product.xpath('normalize-space(.//a[@class= "link-position job-marker-js"])').get(),
                'company' : product.xpath(".//span[@class= 'gray_text company-name']/text()").get(),
                'date' : product.xpath('normalize-space(.//div[@class= "date_from_creation"])').get(),
                'location' : product.xpath('normalize-space(.//span[@class= "serp_location__region"])').get(),

            }

        

         
            
                    
        for x in range(2,50):
            print(x)
            next_page = "https://tr.jooble.org/i%C5%9F-ilanlar%C4%B1-bilgisayar-m%C3%BChendisi?p="+ str(x)
            yield scrapy.Request(url=next_page, callback=self.parse)




                
       
       
       
        
        
        
        
        
        
       