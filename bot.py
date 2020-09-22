# coding=UTF-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from getpass import getpass
import numpy as np
#import unidecode
import getpass
import time
import sys

# Find username of user on computer
user = getpass.getuser()

# Opens username and password files and then asks for the URL
username_file = open("username.txt", "rt")
username = username_file.read()
username_file.close()
password_file = open("password.txt", "rt")
password = password_file.read()
password_file.close()
url = input("Unit/Lesson URL: ")

#driver
driver = webdriver.Firefox()

# Login to Quizlet
driver.get("https://quizlet.com/")
driver.set_window_size(1000, 1000)
login_button_1 = driver.find_element_by_css_selector(".SiteHeader-signIn>button")
login_button_1.click()
username_field = driver.find_element_by_css_selector(".LoginPromptModal-loginFieldsWrapper>.UIInput>.UIInput-content>.UIInput-input")
username_field.send_keys(username)
password_field = driver.find_element_by_css_selector(".LoginPromptModal-loginFieldsWrapper>.UIInput:nth-child(2)>.UIInput-content>.UIInput-input")
password_field.send_keys(password)
login_button_2 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/form/button")
login_button_2.click()
login_button_2.click()

# Go to the classroom_url
driver.get(url)

# Dictionary (literally)
spaneng = {}
owo = 0

#scroll down to load the WHOLE spaneng thing THANKS STACKOVERFLOW
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2);")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, 0);")

# Iterate through all the elements that contain those key/values and add to dictionary
for x in driver.find_elements_by_css_selector("div.SetPageTerms-term"):
    owo += 1
    key = driver.find_element_by_css_selector("div.SetPageTerms-term:nth-child(%d) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)" % owo).text
    value = driver.find_element_by_css_selector("div.SetPageTerms-term:nth-child(%d) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)" % owo).text

    spaneng[key] = value

# Click on the match button
match_button = driver.find_element_by_css_selector("div.SetPageModes-group:nth-child(2) > span:nth-child(2) > a:nth-child(1) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)")
match_button.click()

# Wait for and then close out of the pop-up
driver.implicitly_wait(10)
popup_button = driver.find_element_by_css_selector(".MatchModeInstructionsModal-button > .UIButton--hero")
popup_button.click()

uwu = 0

buttonhastext = {}

for x in driver.find_elements_by_css_selector("div.MatchModeQuestionGridBoard-tile"):
    uwu += 1
    text = driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div/div/div/div[2]/div/div/div[%d]/div/div/div/div" % uwu).text
    button = driver.find_element_by_css_selector("div.MatchModeQuestionGridBoard-tile:nth-child(%d)" % uwu)
    buttonhastext[button] = text

print(spaneng.keys())

for x, y in buttonhastext.items():
    if y in spaneng.keys():
        print(y)
        
        

