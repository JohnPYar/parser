import requests
from bs4 import BeautifulSoup
import json

url = 'https://pvhmarket.ru/catalog/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
mainCategories = soup.find_all('a', class_='parent')
# print(type(mainCategories))
# print(mainCategories)

# for category in mainCategories:
#     print(category['href'])

mainCategoriesLinks = []
mainCategoriesNames = []
resultData = {'main-categories': {}}
# print(type(mainCategoriesLinks))

# ссылки главных категорий
for category in mainCategories:
    mainCategoriesLinks.append(category['href'].replace('/catalog/', ''))
    mainCategoriesNames.append(category.find('span', class_='name'))

# удаляем пустые категории
mainCategoriesLinks.remove('')
mainCategoriesNames.remove(None)

# формируем ссылки главных категорий
for c in mainCategoriesLinks:
    # c = url + c
    mainCategoriesLinks[mainCategoriesLinks.index(c)] = url + c
    # print(c)
# print(mainCategoriesLinks)
# формируем названия главных категорий
for c in mainCategoriesNames:
    # print(mainCategoriesNames.index(c))
    mainCategoriesNames[mainCategoriesNames.index(c)] = c.get_text()
    # c = c.get_text()
    # i = c.index()
    # print(c)
    # print(i)
# print(mainCategoriesNames)

resultData['main-categories'] = dict(zip(mainCategoriesNames, mainCategoriesLinks))
print(resultData)

f = open('result.txt', 'w', encoding="utf8")
f.write(json.dumps(resultData, ensure_ascii=False, indent=4, separators=(',', ': ')))
f.close()
