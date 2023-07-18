# quotes.toscrape.com скарэпинг получение инфы из инета
from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://quotes.toscrape.com/'

responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')
# вытаскиваем из супа цитаты
quotes = soup.find_all('span', class_='text')  # (class_) спец метод не путать с классом (class)
authors = soup.find_all('span', class_='author')
tags = soup.find_all('div', class_='tags')
#  определяем длину кручения списка ниже

# print(responce)
# print(responce.text)  #  показывает код
# print(soup)  # упорядычивает исходный код
# print(quotes)

# for q in quotes:
#     print(q.text)
length = len(quotes)
for index in range(length):
    print(quotes[index].text)
    print(f'{authors[index].text}')
    t = tags[index].find_all('a', class_='tag')
    for item in t:
        print(f'\t\t\t#{item.text}')
