from StoryScraper.items import StoryscraperItem
import scrapy

class BedtimeStories(scrapy.Spider):
    name = "BedtimeStories"

    def __init__(self):
        super().__init__()
        self.start_urls = []

        for i in range(1, 50):
            self.start_urls.append(f'https://blog.reedsy.com/short-stories/bedtime/page/{i}/')

    def parse(self, response):
        hrefs = response.xpath("//a[@class = 'btn-blue btn-rounded btn-xxs']/@href").extract()
        
        for i in hrefs:
            url = "https://blog.reedsy.com" + i
            print(url)
            yield scrapy.Request(url,callback = self.parse_dir_contents)
                
    def parse_dir_contents(self, response):
        item =  StoryscraperItem()

        title = response.xpath("//div[@class = 'content-thin']/h1/text()").extract()
        lst_text = response.xpath("//article[@class = 'font-alt submission-content space-top-xs-md space-bottom-xs-lg']/p/text()").extract()

        item['title'] = self.preprocess_title(title)
        item['story'] = self.preprocess_text(lst_text)

        yield item 

    def preprocess_title(self,title):
        return title[0].strip().strip(" ")

    def preprocess_text(self,text):
        return '\n'.join(text)