from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Открываем страницу регистрации
driver.get('https://rozetka.com.ua/')
time.sleep(5)
button = driver.find_element(By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button")
button.click()
time.sleep(10)
submit_button = driver.find_element(By.XPATH, "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[2]")
submit_button.click()
time.sleep(10)
# Заполняем поля формы
wait = WebDriverWait(driver, 10)

name_filed = driver.find_element(By.CSS_SELECTOR, '#registerUserName')
name_filed.send_keys('Алена')
time.sleep(3)

last_name_filed = driver.find_element(By.CSS_SELECTOR, '#registerUserSurname')
last_name_filed.send_keys('Сторож')
time.sleep(3)

phone_filed = driver.find_element(By.CSS_SELECTOR, '#registerUserPhone')
phone_filed.send_keys('0992345667')
time.sleep(3)

email_filed = driver.find_element(By.CSS_SELECTOR, '#registerUserEmail')
email_filed.send_keys('alena.st@gmail.com')
time.sleep(3)

password_filed = driver.find_element(By.CSS_SELECTOR, '#registerUserPassword')
password_filed.send_keys('Qwg13GHJ')
time.sleep(3)

register_submit_button = driver.find_element(By.XPATH, "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-register/div/form/fieldset/div[8]/button[1]")
register_submit_button.click()

time.sleep(5)

driver.quit()