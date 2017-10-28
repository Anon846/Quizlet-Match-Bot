from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
driver.implicitly_wait(10)
popup_button_1 = driver.find_element_by_css_selector(".UIModal.is-gray.is-open > div > .UIModalHeader > div > span > div > span > button")
popup_button_1.click()

#Go to the lesson
driver.get("https://quizlet.com/160098296/unit-1-lesson-1-infinitive-action-verbs-flash-cards/")

#Go to the match
match_button = driver.find_element_by_css_selector("#SetPageTarget > div > div.SetPage-menu > div > div.SetPage-modes > div > div > div.SetPageModes-group.SetPageModes-group--play > span:nth-child(1) > div > a")
match_button.click()

#Close out of the pop-up
driver.implicitly_wait(10)
popup_button_2 = driver.find_element_by_css_selector("body > div:nth-child(3) > div > div.UIModal.is-white.is-open > div > div > div > div.MatchModeInstructionsModal-button > button")
popup_button_2.click()
