import time
from bs4 import BeautifulSoup
import csv

html_filename = "c:/Users/Gokul Prasad I G/Desktop/po/Amazon.html"

with open(html_filename, "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

data = []

def get_product_info(product):
    product_name_element = product.find("span", class_="a-size-medium a-color-base a-text-normal")
    if product_name_element:
        product_name = product_name_element.get_text()
    else:
        product_name = "N/A"

    product_price_element = product.find("span", class_="a-price-whole")
    if product_price_element:
        product_price = product_price_element.get_text()
    else:
        product_price = "N/A"

    rating_element = product.find("span", class_="a-size-base puis-bold-weight-text")
    if rating_element:
        rating = rating_element.get_text()
    else:
        rating = "N/A"

    return [product_name, product_price, rating]

products = soup.find_all("div", class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vfcg1duwvmpo42mcln9ojhiljk s-latency-cf-section s-card-border")
for product in products:
    product_data = get_product_info(product)
    data.append(product_data)

csv_filename = "amazon_pro.csv"
with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Product Price", "Rating"])
    writer.writerows(data)

print("Scraping and writing to CSV complete.")
