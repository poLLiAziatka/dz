import scrapy

request = "Первая мировая война"

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        f'https://ru.wikipedia.org/wiki/{request}']

    def parse(self, response):
        th = response.xpath('//th[has-class("plainlist")]').extract_first()
        td = response.xpath('//td[has-class("plainlist")]').extract_first()




