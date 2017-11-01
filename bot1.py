# coding=UTF-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from getpass import getpass
import unidecode
import getpass

# Login code
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

# Close the pop-up
driver.implicitly_wait(10)
popup_button_1 = driver.find_element_by_css_selector(".UIModal.is-gray.is-open > div > .UIModalHeader > div > span > div > span > button")
popup_button_1.click()

# Go to the match
driver.get("https://quizlet.com/160098296/match")

# Close the pop-up
driver.implicitly_wait(10)
popup_button = driver.find_element_by_css_selector(".MatchModeInstructionsModal-button > .UIButton--hero")
popup_button.click()

# Set the buttons and their text
b1 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(1)")
b2 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(2)")
b3 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(3)")
b4 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(4)")
b5 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(5)")
b6 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(6)")
b7 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(7)")
b8 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(8)")
b9 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(9)")
b10 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(10)")
b11 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(11)")
b12 = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(12)")
b1t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(1) > div > div.MatchModeQuestionGridTile-content > div > div").text
b2t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(2) > div > div.MatchModeQuestionGridTile-content > div > div").text
b3t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(3) > div > div.MatchModeQuestionGridTile-content > div > div").text
b4t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(4) > div > div.MatchModeQuestionGridTile-content > div > div").text
b5t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(5) > div > div.MatchModeQuestionGridTile-content > div > div").text
b6t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(6) > div > div.MatchModeQuestionGridTile-content > div > div").text
b7t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(7) > div > div.MatchModeQuestionGridTile-content > div > div").text
b8t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(8) > div > div.MatchModeQuestionGridTile-content > div > div").text
b9t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(9) > div > div.MatchModeQuestionGridTile-content > div > div").text
b10t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(10) > div > div.MatchModeQuestionGridTile-content > div > div").text
b11t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(11) > div > div.MatchModeQuestionGridTile-content > div > div").text
b12t = driver.find_element_by_css_selector("#MatchModeTarget > div > div > div > div.ModeLayout-content > div > div > div:nth-child(12) > div > div.MatchModeQuestionGridTile-content > div > div").text

# Dictonary of Spanish to English
spaneng = {
    "andar end patineta": "to skateboard",
    "preparar la comida": "to prepare food",
    "practicar un instrumento": "to practice an instrument",
    "escribir": "to write",
    "bailar": "to dance",
    "cantar": "to sing",
    "comprar": "to buy",
    "descansar": "to rest",
    "dibujar": "to draw",
    "hablar": "to talk",
    "montar en caballo": "to ride a horse",
    "pasar un rato con los amigos": "to spend time with friends",
    "tocar la guitarra": "to play the guitar",
    "tocar el piano": "to play the piano",
    "enseñar": "to teach",
    "escuchar música": "to listen to music",
    "estudiar": "to study",
    "hacer la tarea": "to do homework",
    "ir a la escuela": "to go to school",
    "jugar al fútbol": "to play soccer",
    "jugar al baloncesto": "to play basketball",
    "leer": "to read",
    "mirar la televisión": "to watch television",
    "montar en bicicleta": "to ride a bike",
    "nadar": "to swim",
    "practicar los deportes": "to practice sports",
    "pescar": "to fish",
    "pintar": "to paint",
    "pasear": "to go for a walk",
    "preparar la comida": "to prepare food",
    "trabajar": "to work",
    "dormir": "to sleep",
    "correr": "to run",
    "comer": "to eat",
    "cocinar": "to cook",
    "cazar": "to hunt",
    "caminar": "to walk",
    "beber": "to drink",
    "aprender el español": "to learn Spanish",
    "alquilar un DVD": "to rent a DVD"
}

# Add texts to array
a1 = []
a1.append(b1t)
a1.append(b2t)
a1.append(b3t)
a1.append(b4t)
a1.append(b5t)
a1.append(b6t)
a1.append(b7t)
a1.append(b8t)
a1.append(b9t)
a1.append(b10t)
a1.append(b11t)
a1.append(b12t)

# Add buttons to array
a2 = []
a2.append(b1)
a2.append(b2)
a2.append(b3)
a2.append(b4)
a2.append(b5)
a2.append(b6)
a2.append(b7)
a2.append(b8)
a2.append(b9)
a2.append(b10)
a2.append(b11)
a2.append(b12)

# Array that contains the buttons that haven't been clicked left
a3 = []
a3.append(b1)
a3.append(b2)
a3.append(b3)
a3.append(b4)
a3.append(b5)
a3.append(b6)
a3.append(b7)
a3.append(b8)
a3.append(b9)
a3.append(b10)
a3.append(b11)
a3.append(b12)

# Dictionary for the current words that are on the screen to be matched up
screenmatches = {}

# Compare texts of array against each other and match up
for i in a1:
    for h in a1:
        for spanish, english in spaneng.iteritems():
            if i == spanish and  h == english:
                screenmatches[i] = h

#Click on the buttons
for key, value in screenmatches.iteritems():
    a2[a1.index(key)].click()
    a2[a1.index(value)].click()

#Click on the buttons that aren't ended up being clicked (because of the whole unicode issue thing)
for i in a3:
    i.click()
