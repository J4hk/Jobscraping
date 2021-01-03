# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IndeedSpider(CrawlSpider):
    name = 'indeed'
    allowed_domains = ['tr.indeed.com']
    start_urls = ['https://tr.indeed.com/jobs?l=Türkiye&fromage=365']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//div[@class = 'jobsearch-SerpJobCard unifiedRow row result']/h2/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
             'title': response.xpath("normalize-space(//h1)").get(),
             'company': response.xpath("normalize-space(//div[@class = ' jobsearch-CompanyInfoWithoutHeaderImage']/div/div/div/div[@class = 'icl-u-lg-mr--sm icl-u-xs-mr--xs'][1])" or "normalize-space(//div[@class = 'icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle']/div/div[@class = 'icl-u-lg-mr--sm icl-u-xs-mr--xs'][1])").get(),
             'istanımı': response.xpath("normalize-space(string(//div[@class = 'jobsearch-jobDescriptionText']))" or "normalize-space(string(//div[@class = 'jobsearch-JobComponent-description  icl-u-xs-mt--md  ']//ul[2]/li/text()))" ).get(),
             'aranannitelikler': response.xpath("normalize-space(string(//div[@id = 'jobDescriptionText']/div/div/div//h2[contains(., 'telikler')]/following::div[1]))").get(),
             'Pozisyon': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(. , 'ozisyon')][1]/div[2]/text())").get(),
             'Sektör': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[starts-with(. , 'ekt')]/div[2])").get(),
             'PozisyonSeviyesi': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[starts-with(. , 'ate')]/div[2])").get(),
             'Kategori': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(., 'ego')]/div[2])").get(),
             'ÇalışmaŞekli':  response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(., 'şma Ş')]/div[2])").get(),
             'ÇalışmaYeri':   response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(., 'şma Y')]/div[2])").get(),
             'İlanTarihi':   response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(., 'k Yayı')]/div[2])").get(),
             'GüncellemeTarihi': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[starts-with(., 'Gün')]/div[2])").get(),
             'SonBasvuruTarihi': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(., 'on B')]/div[2])").get(),
             'Maas': response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[starts-with(., 'Ma')]/div[2])").get(),
             'Deneyim':  response.xpath("normalize-space(//div[@id= 'jobDescriptionText']/div/div/div/div/div[contains(., 'neyim')]/div[2])").get(),
             'Site': response.xpath("normalize-space(//div[@class = 'main']/footer/nav/ul/li[contains(. , '2020')])").get(),



        }

        for x in range(10, 670, 10):

            next_page = "https://tr.indeed.com/jobs?q=&l=Türkiye&start=" + \
                str(x)
            yield scrapy.Request(url=next_page, callback=self.parse)
