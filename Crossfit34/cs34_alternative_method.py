import scrapy
from scrapy.crawler import CrawlerProcess


class Crossfit34spider(scrapy.Spider):
    name = 'cs34_spider'

    def start_requests(self):
        urls = ['https://crossfit34.com/gunun-antrenmani/page/']
        urls =  ['datacamp.com/courses/all']
        # ['www.abc.com/{}'.format(x) for x in range(1,10)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('div.course-block > a::attr(href)').extract()
        #     author_names = response.css('p.course-block__author-name ::text').extract()

        for link in links:
            yield response.follow( url = link, callback=self.parse2)

    def parse2(self, response):
        # parse the course sites here

        file_path = 'DC_links.csv'
        with open(file_path, 'w') as f:
            f.writelines( [link + '/n' for link in links])

        # # write out the html
        # html_file = 'CS34.html'
        # with open(html_file, 'wb') as fout:
        #     fout.write(response.body)


dc_dict = dict()

process = CrawlerProcess()

process.crawl(Crossfit34spider)
# cast on a Spider class object

process.start()