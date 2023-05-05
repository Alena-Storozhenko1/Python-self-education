import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.random.org/coins/')

wait = WebDriverWait(driver, 10)

select_flip = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="num"]'))
select_flip.select_by_value('1')

select_coin = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="cur"]'))
select_coin.select_by_visible_text('Swiss 1 Franc')

driver.find_element(By.CSS_SELECTOR, 'input[value="Flip Coin(s)"]').click()

time.sleep(10)
driver.quit()