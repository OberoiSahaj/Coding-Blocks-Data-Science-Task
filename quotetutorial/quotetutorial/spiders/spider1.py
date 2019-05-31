import scrapy

class Spider1(scrapy.Spider):
    name = 'quotes'
    start_urls = [ 'http://quotes.toscrape.com/']

    def parse(self, response):
        quote_cont = response.css('div.quote')
        for quote in quote_cont:
            q = quote.css('span.text::text').get().strip()
            author = quote.css('small.author::text').get()
            tag = quote.css('a.tag::text').get()
            yield {'quote': q,
                   'author': author,
                    'tags': tag }

