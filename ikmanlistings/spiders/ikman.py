
# This is a Scrapy spider for scraping vehicle listings from the ikman.lk website.
# It extracts details such as title, price, location, days since posted, mileage, link, and image URL.  

## Import necessary libraries
import scrapy
import re
from bs4 import BeautifulSoup
from scrapy import Selector

# Define the spider class
class TableSpider(scrapy.Spider):
    name = 'ikman'
    base_url = ['https://ikman.lk/en/ads/sri-lanka/vehicles']  # Replace with your actual URL
    name = "ikman"
    allowed_domains = ["ikman.lk"]
    max_pages = 4  # adjust this as needed
    query_string = "alto"  # adjust this as needed




    # Start URLs for the spider
    async def start(self):
        for page in range(1, self.max_pages):
            yield scrapy.Request(url=f'https://ikman.lk/en/ads/sri-lanka/vehicles?page={page}&query={self.query_string}', callback=self.parse)


    # Parse the response from the request
    def parse(self, response):
        # Get the entire table body (as HTML)
        table_body_html = response.xpath("/html/body").get()
        ul = response.xpath("//ul[contains(@class, 'list--3NxGO')]")

        
        for item in ul:
            html_string = item.get()
            soup = BeautifulSoup(str(html_string), 'html.parser')

            # Find all <li> inside <ul> with exact class match
            filtered_li_tags = soup.select("ul li.normal--2QYVk.gtm-normal-ad")
            # Print the filtered list items
            for li in filtered_li_tags:
                print("li_33333333:: " + str(li))    
                self.log(li)          
                
                soup = BeautifulSoup(str(li), 'html.parser')

                # Extract values
                title = soup.find('h2').get_text(strip=True)
                price = soup.find('div', class_='price--3SnqI color--t0tGX').get_text(strip=True)
                location = soup.find('div', class_='description--2-ez3').get_text(strip=True)
                days = soup.find('div', class_='updated-time--1DbCk').get_text(strip=True)
                mileage = soup.find('div', class_='details--1GUIn')
                mileage = mileage.get_text(strip=True) if mileage else 'N/A'

                # Link and image
                link = soup.find('a', class_='card-link--3ssYv gtm-ad-item')['href']
                image_url = soup.find('img')['src']



                yield {

                    'title': title,
                    'price': price,
                    'location': location,
                    'days': days,
                    'mileage': mileage,
                    'link': response.urljoin(link),
                    'image_url': image_url

                }