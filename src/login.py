from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


def Logueo(driver,usuario,password,mensajePath):
    texto = ''
    continua = True
    usuariopath = '//*[@id="__next"]/div/div/div/div/div/form/div[1]/div/input'
    passwordpath = '//*[@id="__next"]/div/div/div/div/div/form/div[2]/div/input'
    btingresarpath = '//*[@id="__next"]/div/div/div/div/div/form/div[3]/button'
    link = 'http://localhost:4500/login'
    driver.get(link)
    if continua:
        try:
            usuarioInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, usuariopath)))
        except TimeoutException:
            continua = False
    if continua:
        usuarioInput.send_keys(usuario)
        time.sleep(1)
        try:
            passwordInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, passwordpath)))
        except TimeoutException:
            continua = False
    try:
        if continua:
            passwordInput.send_keys(password)
    except:
        pass

    if continua:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, btingresarpath))).click()

    time.sleep(2)
    texto = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, mensajePath))).text
    return texto