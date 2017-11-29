# coding=UTF-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from getpass import getpass
import numpy as np
import unidecode
import getpass
import sys

# Find username of user on computer
user = getpass.getuser()

# Ask for inputs
username = input("Username: ")
password = getpass.getpass()
match_url = input("Match/Lesson/Unit URL: ")

# Find the platform (obviously only Windows /andsoonlinux!/ is supported) and set the driver
# If you are on macOS feel free to submit a pull request of however the heck you need to set your driver path
if sys.platform == "win32":
    directory = r"C:\Users\Jesus Christ\AppData\Local\Programs\Python\Python36-32\Scripts\chromedriver.exe"
    directory = directory.replace("Jesus Christ", user)
    driver = webdriver.Chrome(directory)

# Login to Quizlet
driver.get("https://quizlet.com/")
login_button_1 = driver.find_element_by_css_selector(".SiteHeader-signIn>button")
login_button_1.click()
username_field = driver.find_element_by_css_selector(".LoginPromptModal-loginFieldsWrapper>.UIInput>.UIInput-content>.UIInput-input")
username_field.send_keys(username)
password_field = driver.find_element_by_css_selector(".LoginPromptModal-loginFieldsWrapper>.UIInput:nth-child(2)>.UIInput-content>.UIInput-input")
password_field.send_keys(password)
login_button_2 = driver.find_element_by_css_selector(".LoginPromptModal-form>.UIButton--hero")
login_button_2.click()

# Close the pop-up
driver.implicitly_wait(10)
popup_button_1 = driver.find_element_by_css_selector(".UIModal.is-gray.is-open > div > .UIModalHeader > div > span > div > span > button")
popup_button_1.click()

# Go to the match_url
driver.get(match_url)

# Select the method to sort the answers
original_option = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[4]/div/div/span/div/div/div/div/div/select/option[1]")
original_option.click()

# Conversion list (makes key/value pairs for the matchURL)
conversion_list_elements = [];
spanengcontainers = []
spaneng = {}

# Iterate through all the elements that contain those key/values
for i in driver.find_elements_by_css_selector("#SetPageTarget > div > div.SetPage-diagramAndTerms > div.UIDiv.SetPage-termsWrapper > div > div > div > div"):
    conversion_list_elements.append(i)
    key_value = driver.find_elements_by_css_selector(".UIDiv.SetPage-termsWrapper > div > div > div > div:nth-child(%d) > div > div > div.SetPageTerm-contentWrapper > div > div" % conversion_list_elements.index(i))
    key = ""
    value = ""
    for x in key_value:
        if key == "":
            key = x
        else:
            value = x

    if (conversion_list_elements.index(i) + 1) != 4:
        key = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[4]/div/div/div/div[%d]/div/div/div[1]/div/div[1]/div/a/span" % (conversion_list_elements.index(i) + 1)).text
        value = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[4]/div/div/div/div[%d]/div/div/div[1]/div/div[2]/div/a/span" % (conversion_list_elements.index(i) + 1)).text
    else:
        key = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[4]/div/div/div/div[5]/div/div/div[1]/div/div[1]/div/a/span").text
        value = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[4]/div/div/div/div[5]/div/div/div[1]/div/div[2]/div/a/span").text

    spaneng[key] = value

# Click on the match button
match_button = driver.find_element_by_css_selector(".SetPage-modes > div > div > .SetPageModes-group.SetPageModes-group--play > span:nth-child(1) > div > a")
match_button.click()

# Wait for and then close out of the pop-up
driver.implicitly_wait(10)
popup_button = driver.find_element_by_css_selector(".MatchModeInstructionsModal-button > .UIButton--hero")
popup_button.click()


# Set the buttons and their text and button array I honestly dont know anymore I am just typing
a1 = []
for i in range(12):
    c = i + 1
    a1.append(driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(%d)" % c))

# Set the texts and what the heck
a2 = []
for i in range(12):
    c = i + 1
    a2.append(driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(%d) > div > div.MatchModeQuestionGridTile-content > div > div" % c).text)

# Array that contains the buttons that haven't been clicked left
a3 = []
for i in range(12):
    a3.append(a1[i])

# Dictionary for the current words that are on the screen to be matched up
screenmatches = {}

# Compare texts of array against each other and match up
for i in a2:
    for h in a2:
        for spanish, english in spaneng.items():
            if i == spanish and  h == english:
                screenmatches[i] = h

#Click on the buttons
for key, value in screenmatches.items():
    a1[a2.index(key)].click()
    a1[a2.index(value)].click()

#Click on the buttons that aren't ended up being clicked (because of the whole unicode issue thing)
for i in a3:
    i.click()
