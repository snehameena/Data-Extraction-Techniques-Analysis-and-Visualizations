from datetime import datetime
from WorldNewsAsia.items import Article
from string import whitespace

class WorldnewsasiaPipeline(object):
    def process_item(self, article, spider):
        print("article:::",article)
        article['text'] = [line for line in article['text'] if line not in whitespace]
        article['text'] = ''.join(article['text'])
        return article
