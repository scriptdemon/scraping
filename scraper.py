from bs4 import BeautifulSoup
import requests
import json

reviews = []
for i in range(501,510):
    URL = "https://www.amazon.in/Moto-Plus-Lunar-Grey-64GB/product-reviews/B071HWTHPH/ref=dpx_acr_txt?showViewpoints="+str(i)
    page = requests.get(URL)
    parsed_input = BeautifulSoup(page.content,'html.parser')
    selected = parsed_input.find_all('span',class_='a-size-base review-text')
    for each in selected:
        review = each.get_text()
        reviews.append({"reviewText": review})
print(reviews)
print(len(reviews))

with open("reviews2.txt","w") as outfile:
    json.dump(reviews,outfile)