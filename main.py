import requests
from bs4 import BeautifulSoup

url = 'https://pvhmarket.ru/catalog/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
mainCategories = soup.find_all('a', class_='parent')

# for category in mainCategories:
#     print(category['href'])

mainCategoriesLinks = []
# print(type(mainCategoriesLinks))

# ссылки главных категорий
for category in mainCategories:
    mainCategoriesLinks.append(category['href'].replace('/catalog/', ''))

# удаляем пустые категории
mainCategoriesLinks.remove('')

# формируем ссылки главных категорий
for c in mainCategoriesLinks:
    c = url + c
    print(c)
