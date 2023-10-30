import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://in.puma.com/in/en/collections/collections-football/collections-football-manchester-city-fc"
web_page = requests.get(start_url)
soup = BeautifulSoup(web_page.content, 'html.parser')

product_links = []
for link in soup.find_all(attrs={"data-test-id": "product-list-item-link"}):
    if link['href'] not in product_links:
        product_links.append('https://in.puma.com' + link['href'])

# print(product_links)
with open('puma_manchester_city.csv', 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Price', 'Description', 'Link'])

    
    for product_url in product_links:
        product_page = requests.get(product_url)
        product_soup = BeautifulSoup(product_page.content, 'html.parser')
        product_name = product_soup.find(attrs={"data-test-id": "pdp-title"}).text.strip()
        on_sale = product_soup.find(attrs={"data-test-id":"item-sale-price-pdp"})
        price =  on_sale.text.strip() if on_sale else  product_soup.find(attrs={"data-test-id":"item-price-pdp"}).text.strip()
        product_description = product_soup.find(attrs={"data-test-id":"pdp-product-description"}).text.strip()
        writer.writerow([product_name, price, product_description, product_url])