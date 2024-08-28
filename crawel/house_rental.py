import requests
from parsel import Selector



class house_crawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        page = requests.get(house_crawler.MAIN_URL, timeout=10)
        self.page = page.text

    def get_page_title(self):
        html = Selector(text=self.page)
        title = html.css('title::text').get()
        print(title)

    def get_house_links(self):
        html = Selector(text=self.page)
        links = html.css('div.listing a::attr(href)').getall()
        links = list(map(lambda l: house_crawler.BASE_URL + l, links))
        return links[:3]


if __name__ == "__main__":
    crawler = house_crawler()
    crawler.get_page()
    crawler.get_house_links()
