import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.random.org/dice/")

wait = WebDriverWait(driver, 10)

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value = "Roll Dice"]')))
button.click()
time.sleep(10)
driver.quit()