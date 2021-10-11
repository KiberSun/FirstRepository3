from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

import pyautogui

import string
import random
from time import sleep


def getnewlogin() -> str:
    return ''.join(random.sample(string.ascii_uppercase, 1) + random.sample(string.ascii_lowercase, 5) + random.sample(string.digits, 3))

def getnewpassword() -> str:
    return ''.join(random.sample(string.ascii_uppercase, 1) + random.sample(string.ascii_letters + string.digits, 8) + random.sample(string.digits, 1))

def getnewanswer() -> str:
    return ''.join(random.sample(string.ascii_uppercase, 1) + random.sample(string.ascii_lowercase, 4))

def getnewname(symbolcount) -> str:
    return ''.join(random.sample(string.ascii_uppercase, 1) + random.sample(string.ascii_lowercase, symbolcount - 1))

def press(buttons):
    sleep(1)
    for button in buttons:
        pyautogui.keyDown(button)
        sleep(0.2)
        pyautogui.keyUp(button)
        sleep(0.1)

def press(buttons, interval, holding, freeze):
    sleep(freeze)
    for button in buttons:
        pyautogui.keyDown(button)
        sleep(holding)
        pyautogui.keyUp(button)
        sleep(interval)

def hold(button, time):
    pyautogui.keyDown(button)
    sleep(time)
    pyautogui.keyUp(button)


browser = webdriver.Firefox(executable_path = r'C:\gecko\geckodriver.exe')
browser.get('https://id.rambler.ru/login-20/mail-registration?rname=head&back=https%3A%2F%2Fwww.rambler.ru%2F&param=popup&iframeOrigin=https%3A%2F%2Fwww.rambler.ru')

login = getnewlogin()
password = getnewpassword()
answer = getnewanswer()

print('Your login, password and answer:\n' + login + '\n' + password + '\n' + answer  + '\n')

sleep(3)

#       browser.find_element(By.XPATH, '''''')

browser.find_element(By.XPATH, '''//input[@id="login"]''').send_keys(login)
browser.find_element(By.XPATH, '''//input[@id="newPassword"]''').send_keys(password)
browser.find_element(By.XPATH, '''//input[@id="confirmPassword"]''').send_keys(password)
browser.find_element(By.XPATH, '''//*[@id="question"]''').click()
#browser.find_element(By.CLASS_NAME, '''rui-RelativeOverlay-content''').click()
press(['down', 'enter'], 0.1, 0.2, 0)
browser.find_element(By.XPATH, '''//input[@id="answer"]''').send_keys(answer)

sleep(20)
browser.find_element(By.XPATH, '''/html/body/div[1]/div/div[1]/div/article/form/button''').click()

sleep(4)
browser.find_element(By.XPATH, '''//input[@id="firstname"]''').send_keys(getnewname(6))
browser.find_element(By.XPATH, '''//input[@id="lastname"]''').send_keys(getnewname(8))
browser.find_element(By.XPATH, '''//*[@id="gender"]''').click()
press(['down', 'enter'], 0.1, 0.2, 0)
browser.find_element(By.XPATH, '''//input[@id="birthday"]''').click()
press(['down', 'enter'], 0.1, 0.2, 0)
browser.find_element(By.XPATH, '''//*[@id="root"]/div/div[1]/div/article/form/section[4]/div/div/div[1]/div[2]/div/div/div/input''').click()
press(['down', 'enter'], 0.1, 0.2, 0)
browser.find_element(By.XPATH, '''/html/body/div[1]/div/div[1]/div/article/form/section[4]/div/div/div/div[3]/div/div/div/input''').click()
press(['down', 'enter'], 0.1, 0.2, 0)

#browser.find_element(By.XPATH, '''//input[@id="geoid"]''').send_keys('Сочи')
#browser.find_element(By.XPATH, '''/html/body/div[1]/div/div[1]/div/article/form/button''').click()