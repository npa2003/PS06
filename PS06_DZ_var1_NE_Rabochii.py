
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/svet/page-3"
driver.get(url)
#time.sleep(3)


# Ожидаем загрузки всей страницы ________________________________

# Способ 1
wait = WebDriverWait(driver, 10)
button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.RhKkz button"))
)
# Способ 2
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Прокрутка вниз
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     print('подгружаем.......')
#     time.sleep(2)  # Ожидание подгрузки
#
#     # Проверка изменения высоты страницы
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#     print('Продолжаем подгружать!!!')

# Способ 3: Использовать END (если работает)
#driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
# time.sleep(3)
# print('END Key')

lamps = driver.find_elements(By.CLASS_NAME, "LlPhw")
parsed_data = []

for lamp in lamps:
    try:
        price = lamp.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text #span.ui-LD-ZU KIkOH
        price = price.replace(" ", "").replace("руб.", "")
    except:
        print("Ошибка при парсинге ЦЕНЫ !")
        continue

    print(price)


driver.quit()