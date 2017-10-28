from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from getpass import getpass
import getpass

#Block of login code
username = raw_input("Username: ")
password = getpass.getpass()
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://quizlet.com/")
login_button_1 = driver.find_element_by_css_selector(".SiteHeader-signIn>button")
login_button_1.click()
username_field = driver.find_element_by_css_selector(".LoginPromptModal-loginFieldsWrapper>.UIInput>.UIInput-content>.UIInput-input")
username_field.send_keys(username)
password_field = driver.find_element_by_css_selector(".LoginPromptModal-loginFieldsWrapper>.UIInput:nth-child(2)>.UIInput-content>.UIInput-input")
password_field.send_keys(password)
login_button_2 = driver.find_element_by_css_selector(".LoginPromptModal-form>.UIButton--hero")
login_button_2.click()

#Close out of the pop-up
popup_button_1 = driver.find_element_by_css_selector(".UIModal.is-gray.is-open > div > .UIModalHeader > div > span > div > span > button")
popup_button_1.click()


