import requests
from bs4 import BeautifulSoup

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
    c = url + c
    print(c)
# формируем названия главных категорий
for c in mainCategoriesNames:
    c = c.get_text()
    print(c)
