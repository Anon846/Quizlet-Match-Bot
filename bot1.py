from selenium import webdriver
from getpass import getpass

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://quizlet.com/")

login = driver.find_element_by_xpath("//*[@id='SiteHeaderReactTarget']/header/div[1]/div/span[2]/div[2]/div/button[1]")
