from bs4 import BeautifulSoup


# with open('../100_DAYS_OF_CODE/day45/website.html', 'r', encoding='utf8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a) #anchor tag
# print(soup.p) #first paragraph

# all_anchor_tags= soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print (tag.getText())
#     print (tag.get("href"))

# heading = soup.find(name='h1', id='name')
# print(heading.name)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())
# print(section_heading.get("class"))

# company_url = soup.select_one(selector='p a')
# print(company_url)

# name = soup.select_one(selector='#name')
# print(name)

# headings = soup.select(".heading")
# print(headings)