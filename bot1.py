from selenium import webdriver
from getpass import getpass

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://quizlet.com/")

login = driver.find_element_by_css_selector(".SiteHeader-signIn>button")
login.click()
