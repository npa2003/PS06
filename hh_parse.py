import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

#vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--n77Dj8TY8VIUF0yM")
vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-info--ieHKDTkezpEj0Gsx") #более вложенный блок

#print(vacancies)
parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"].magritte-text___tkzIl_5-0-8').text
    except:
        print("Ошибка при парсинге ВАКАНСИИ!")
        continue

    try:
        company = vacancy.find_element(By.CSS_SELECTOR,'span[data-qa="vacancy-serp__vacancy-employer-text"].magritte-text___tkzIl_5-0-8').text
    except:
        print("Ошибка при парсинге КОМПАНИИ!")
        #continue

    try:
        salary = []
        salars = vacancy.find_elements(By.CSS_SELECTOR, '[class="magritte-text___pbpft_3-0-31 magritte-text_style-primary___AQ7MW_3-0-31 magritte-text_typography-label-1-regular___pi3R-_3-0-31"]')
        salary = "".join(sal.text for sal in salars)

    except:
        print("Ошибка при парсинге ЗАРПЛАТЫ!")
        #continue

    try:
        link = vacancy.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        print("Ошибка при парсинге LINK!")
        #continue

    parsed_data.append([title, company, salary, link])
    # print(f'Вакансия: {title}')
    # print(f'Компания: {company}')
    # print(f'Зарплата: {salary}')
    # print(f'Ссылка:   {link}')
    # print()

#print(parsed_data)

driver.quit()

with open("hh.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название вакансии","Название компании",'Зарплата','Ссылка'])
    writer.writerows(parsed_data)

