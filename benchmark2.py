# Import the scrapy library
import scrapy
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
    name = 'dc_chapter_spider'

    # start_requests method

    def start_requests(self):
        yield scrapy.Request(url=url_short, callback=self.parse)

    def parse_front(self, response):
        # narrow in on the course blocks
        course_blocks = response.css('div.course-block')

        # direct to the course links
        course_links = course_blocks.xpath('./a/@href')

        # extract the links
        links_to_follow = course_links.extract()

        # follow the links to the next parser
        for link in links_to_follow:
            yield response.follow(url=link, callback=self.parse_pages)


    def parse_pages(self, response):
        # direct to the course title
        crs_title = response.xpath('//h1[contains(@class, "title")]/text()')

        # extract and clean the course title text
        crs_title_ext = crs_title.extract_first().strip()
        # bc. extract() would return a list, whereas extract_first returns a string

        # direct to the chapter title
        chp_titles = response.css('h4.chapter__title::text')

        # extract and clean the chapter title text
        chp_titles_ext = [title.strip() for title in chp_titles.extract()]

        # store this in our dictionary
        dc_dict[crs_title_ext] = chp_titles_ext


dc_dict = dict()

process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)

process.start()

'''
# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    # Create a SelectorList of the course titles text
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    # Extract the text and strip it clean
    crs_title_ext = crs_title.extract_first().strip()
    # Create a SelectorList of course descriptions text
    crs_descr = response.css( 'p.course__description' )
    # Extract the text and strip it clean
    crs_descr_ext = crs_descr.extract_first().strip()
    # Fill in the dictionary
    dc_dict[crs_title_ext] = crs_descr_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)'''