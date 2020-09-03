# -*- coding: utf-8 -*-
import scrapy


class IndeedyazılımSpider(scrapy.Spider):
    name = 'indeedyazılım'
    allowed_domains = ['tr.indeed.com']
    start_urls = ['https://tr.indeed.com/jobs?q=Yazılım+Mühendisi&start=0']

    def parse(self, response):
        for product in response.xpath("//div[@class = 'jobsearch-SerpJobCard unifiedRow row result']"):
          yield{
              'title' : product.xpath('normalize-space(.//h2[@class = "title"])').get(),
              'company' : product.xpath('normalize-space(.//span[@class = "company"])').get(),
              'date' : product.xpath('normalize-space(.//span[@class = "date "])').get(),
              'location' : product.xpath('normalize-space(.//span[@class = "location accessible-contrast-color-location"])').get(),


            }  


        next_page = response.xpath("//a[@aria-label = 'Sonraki']/@href").get()

        new_url = 'https://tr.indeed.com/'+str(next_page)
        if new_url:
            yield scrapy.Request(url = new_url, callback=self.parse)
