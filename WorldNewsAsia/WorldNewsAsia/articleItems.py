import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WorldNewsAsia.items import Article

class ArticleSpider(CrawlSpider):
    name = 'articles'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    allowed_domains = ['www.channelnewsasia.com']
    start_urls = ['https://www.channelnewsasia.com/news/world']
    rules = [Rule(LinkExtractor(allow='(/world/).*$'), callback='parse', follow=True)]

    
    def parse(self,response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@class="c-rte--article"]//text()').extract()
        return article