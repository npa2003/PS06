import time
import csv
from traceback import print_tb

from bs4 import BeautifulSoup
import requests


url = "https://www.divan.ru/category/svet/page-3"
response = requests.get(url)
time.sleep(2)


# Создаём объект Soup
soup = BeautifulSoup(response.content, "html.parser")

#lamps = driver.find_elements(By.CLASS_NAME, "LlPhw")
lamps = soup.find_all("div", class_="LlPhw")
#print(lamps)

parsed_data = []

for lamp in lamps:
    try: # вынимаем стоимость
        price = ''
        price = lamp.find("span", class_='ui-LD-ZU KIkOH').text #span.ui-LD-ZU KIkOH ui-LD-ZU KIkOH
        price = price.replace(" ", "").replace("руб.", "")
    except:
        print("Ошибка при парсинге ЦЕНЫ !")

    try: # вынимаем наименование
        name = ''
        name = lamp.find("span", itemprop='name').text
        #name = lamp.find('span', {'itemprop': 'name'}).text # Вариант синтаксиса функции
    except:
        print("Ошибка при парсинге НАИМЕНОВАНИИ !")

    try: # вынимаем ссылку
        link = ''
        link = lamp.find("link", itemprop='url')['href']

    except:
        print("Ошибка при парсинге ССЫЛКИ !")

    parsed_data.append([name, price,  link])
    print(name)
    print(price)
    print(link)

with open("svet.csv", "w", newline="", encoding='utf-8-sig') as file: # cp1251 для старых Windows
    writer = csv.writer(file)
    writer.writerow(["Название светильника","Стоимость",'Ссылка'])
    writer.writerows(parsed_data)