from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.prettify())

# print(soup.a) #printing the first anker tag men kan udskiftes med andre attributter fx p
# all_anchor_tags = soup.find_all("a") #sådan printer den ALLE anchor tags
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     #print(tag.getText)
#     print(tag.get("href"))

#looking for specifict text
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

#print company url
company_url = soup.select_one(selector="p a")
print(company_url)

#print name
name = soup.select_one(selector="#name")
print(name)

#print heading from HTML file
headings = soup.select(".heading")
print(headings)