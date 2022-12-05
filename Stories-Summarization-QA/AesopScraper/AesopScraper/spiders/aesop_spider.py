import scrapy
from AesopScraper.items import AesopscraperItem

class AesopSpider(scrapy.Spider):
    name = "aesop"

    def __init__(self):
        super().__init__()
        self.start_urls = []

        for i in range(2, 148):
            index = str(i)
            while len(index) != 3:
                index = '0' + index
            self.start_urls.append(f'https://read.gov/aesop/{index}.html')

    def parse(self, response):
        # Extract title
        title = response.xpath("//h1/text()").extract()[0]

        # Extract story
        paragraphs = [
            ' '.join(
                line.strip()
                for line in p.xpath('.//text()').extract()
                if line.strip()
            )
            for p in response.xpath('//p')
        ]
        story = ''
        for text in paragraphs:
            story += text
        
        # Extract moral
        moral = response.xpath('//blockquote/text()').extract()[0]

        item = AesopscraperItem()
        item['title'] = title
        item['story'] = story
        item['moral'] = moral

        yield item