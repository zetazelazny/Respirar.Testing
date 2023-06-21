from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def RecoverPassword(driver,mail,mensajePath):
    continua = True
    texto=''
    mailpath = '//*[@id="__next"]/div/div/div/div/div/form/div[1]/div/input'
    btnrnviarpath = '//*[@id="__next"]/div/div/div/div/div/form/div[2]/button'
    link = 'http://localhost:4500/recoverpassword'
    driver.get(link)
    if continua:
        try:
            mailInput = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, mailpath)))
        except TimeoutException:
            continua = False
    if continua:
        mailInput.send_keys(mail)
        time.sleep(1)



    if continua:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, btnrnviarpath))).click()

    texto = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, mensajePath))).text
    driver.quit()
    return texto