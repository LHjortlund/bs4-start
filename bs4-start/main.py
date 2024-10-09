from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles= soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number= max(article_upvotes)
# print(largest_number)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)







# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.prettify())
#
# # print(soup.a) #printing the first anker tag men kan udskiftes med andre attributter fx p
# # all_anchor_tags = soup.find_all("a") #sådan printer den ALLE anchor tags
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     #print(tag.getText)
# #     print(tag.get("href"))
#
# #looking for specifict text
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
#
# #print company url
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# #print name
# name = soup.select_one(selector="#name")
# print(name)
#
# #print heading from HTML file
# headings = soup.select(".heading")
# print(headings)