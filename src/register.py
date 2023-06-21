from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


def Register(driver,mail,password,repassword,mensajePath):
    continua = True
    texto=''
    mailpath = '//*[@id="__next"]/div/div[1]/div/div/form/div[1]/div/input'
    passwordpath = '//*[@id="__next"]/div/div[1]/div/div/form/div[2]/div/input'
    repasswordpath = '//*[@id="__next"]/div/div[1]/div/div/form/div[3]/div/input'
    btnrnviarpath = '//*[@id="__next"]/div/div[1]/div/div/form/div[4]/button'
    link = 'http://localhost:4500/register'
    driver.get(link)
    if continua:
        try:
            mailInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, mailpath)))
        except TimeoutException:
            continua = False
    if continua:
        mailInput.send_keys(mail)
        time.sleep(1)
        try:
            passwordInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, passwordpath)))
        except TimeoutException:
            continua = False
    if continua:
        try:
            if continua:
                passwordInput.send_keys(password)
        except:
            continua = False
            pass
    if continua:
        try:
            repasswordInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, repasswordpath)))
        except TimeoutException:
            continua = False
    if continua:
        try:
            if continua:
                repasswordInput.send_keys(repassword)
        except:
            continua = False
            pass

    if continua:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, btnrnviarpath))).click()

    texto = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, mensajePath))).text
    driver.quit()
    return texto