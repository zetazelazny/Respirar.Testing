from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from src.hiloclose import close_driver
import threading
import time


def PasswordChange(driver,passActual, NewPass,ConfirmPass,mensajePath):
    continua = True
    texto=''
    actualPath = '//*[@id="currentPassword"]'
    nuevaPath ='//*[@id="newPassword"]'
    confirmPath = '//*[@id="confirmPassword"]'
    btnrconfirmarpath = '//*[@id="__next"]/div/form/div/div/div/button'
    if continua:
        try:
            actualInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, actualPath)))
        except TimeoutException:
            continua = False
    if continua:
        actualInput.send_keys(passActual)
    if continua:
        try:
            NuevaInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, nuevaPath)))
        except TimeoutException:
            continua = False
    if continua:
        NuevaInput.send_keys(NewPass)

    if continua:
        try:
            ConfirmInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, confirmPath)))
        except TimeoutException:
            continua = False
    if continua:
        ConfirmInput.send_keys(ConfirmPass)

    if continua:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, btnrconfirmarpath))).click()
    time.sleep(1)
    texto = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, mensajePath))).text
    t = threading.Thread(target=close_driver, args=(driver))
    t.start()
    return texto