from bs4 import BeautifulSoup
import requests
import json

dict = {}
detail_page = open("honor-6X.html","r",encoding="utf8")
parsed_input = BeautifulSoup(detail_page,'html.parser')

#extracting asin
selected = parsed_input.find('div',{"id" : "cerberus-data-metrics" })
dict["asin"] = selected['data-asin']

#extracting imUrl
selected_imUrl = parsed_input.find('div',{"id" : "imgTagWrapperId" })
dict["imUrl"] = selected_imUrl.img['data-old-hires']

#extracting title
selected_title = parsed_input.find('span',{"id" : "productTitle"})
title = selected_title.get_text()
title = title.replace('\n','').replace('\t','')
dict["title"] = title


#extracting description
selected_desc = parsed_input.find('div',{"id" : "feature-bullets"})
descs = selected_desc.ul.find_all('li')
desc = ""
for each in descs:
    desc = desc+each.get_text().replace('\n','').replace('\t','')+"."
dict["description"] = desc

#buy after viewing
selected_bav = parsed_input.find('div',{"class" : "a-section p13n-sc-list-cells-container"})
if(selected_bav):
    bavs = selected_bav.ul.find_all('li')
    bavlist = []
    for each in bavs:
        meta_data = each.div
        meta_json = json.loads(meta_data['data-p13n-asin-metadata'])
        asin = meta_json['asin']
        bavlist.append(asin)
    dict["buy_after_viewing"] = bavlist
detail_page.close()

reviews = []
detail_page = open("honor-6X-reviews.html","r",encoding="utf8")
parsed_input = BeautifulSoup(detail_page,'html.parser')

#Finding all reviews container
review_container = parsed_input.find('div',{"id":"cm_cr-review_list"})
all_reviews = review_container.find_all('div',{"class":"a-section review"})
for each in all_reviews:
    dict_temp = {}
    #reviewerID
    reviewerID = each['id']
    #print(reviewerID)
    dict_temp['reviewerID'] = reviewerID

    #reviewText
    content_html = each.find('span', {"class": "a-size-base review-text"})
    reviewText = content_html.get_text()
    #print(reviewText)
    dict_temp['reviewText'] = reviewText

    #overall rating
    content_rating = each.find('a',{"class":"a-link-normal"})
    whole_title = content_rating["title"]
    overall_rating = whole_title[0:3]
    #print(overall_rating)
    dict_temp['overall'] = overall_rating

    #summary
    content_summary = each.find('a',{"class":"review-title"})
    summary = content_summary.get_text()
    #print(summary)
    dict_temp['summary'] = summary

    #reviewTime
    content_reviewTime = each.find('span',{"data-hook":"review-date"})
    whole_reviewTime = content_reviewTime.get_text()
    reviewTime = whole_reviewTime[3:]
    #print(reviewTime)
    dict_temp['reviewTime'] = reviewTime

    #helpful
    contentHelp = each.find('span',{"data-hook":"helpful-vote-statement"})
    if(contentHelp):
        contentHelp_text = contentHelp.get_text().replace('\n','').replace('\t','')
        if(contentHelp_text[6:9] == 'One'):
            dict_temp['helpful'] = [1,1]
        else:
            helpful = int(contentHelp_text[6])
            dict_temp['helpful'] = [helpful,helpful]

    reviews.append(dict_temp)

dict['reviews'] = reviews
print(dict)
print(len(dict['reviews']))

with open("honor-6X-reviews.txt","w") as outfile:
    json.dump(dict,outfile)
    outfile.close()