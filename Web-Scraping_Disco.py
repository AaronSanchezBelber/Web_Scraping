from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)