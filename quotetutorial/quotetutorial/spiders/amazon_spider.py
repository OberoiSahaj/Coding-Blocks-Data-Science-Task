import scrapy

class Spider2(scrapy.Spider):
    name = 'amazon'
    start_urls = [ 'https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_2']

    def parse(self, response):
        # mobile_container = response.css('div.s-include-content-margin s-border-bottom')
        # for mobile in mobile_container:

        name = response.css('span.a-size-medium a-color-base a-text-normal').css("::text").extract()  # Unable to obtain the mobile name. Couldn't find any solution..
        price = response.css('span.a-price-whole::text').extract()
        rating = response.css('span.a-icon-alt::text').extract()
        yield {'Mobile_Name': name,
               'Price': price,
                'Rating': rating }
