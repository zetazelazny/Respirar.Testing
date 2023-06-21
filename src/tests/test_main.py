from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.login import Logueo
from src.passwordchange import PasswordChange
from src.register import Register
from src.recoverpassword import RecoverPassword
from selenium.webdriver.common.by import By
import time

def test_logueo_pass_valido():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePath = '//*[@id="__next"]/div/div/div/h2'
    assert Logueo(driver,usr,pas,mensajePath) == 'Perfil'

def test_logueo_pass_invalido():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '123456'
    mensajePath = '//*[@id="__next"]/div/div/div/div/div/form/ul/li'
    assert Logueo(driver,usr,pas,mensajePath) == 'Credenciales de usuario inválidas'


def test_logueo_pass_vacia():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = ''
    mensajePath = '//*[@id="__next"]/div/div/div/div/div/form/ul/li'
    assert Logueo(driver,usr,pas,mensajePath) == 'Ingrese una contraseña'


def test_logueo_email_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = ''
    pas = '1234'
    mensajePath = '//*[@id="__next"]/div/div/div/div/div/form/ul/li'
    assert Logueo(driver,usr,pas,mensajePath) == 'Correo inválido'

def test_register_email_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = ''
    pas = 'Prueba1234*'
    repas = 'Prueba1234*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas,repas, mensajePath) == 'Correo inválido'


def test_register_email_invalido():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan.test.com'
    pas = 'Prueba1234*'
    repas = 'Prueba1234*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas,repas, mensajePath) == 'Correo inválido'

def test_register_pass_sin_caracter():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan@test.com'
    pas = 'Prueba1234'
    repas = 'Prueba1234'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas,repas, mensajePath) == 'La contraseña debe tener al menos un caracter especial'

def test_register_pass_sin_upper():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan@test.com'
    pas = 'prueba1234*'
    repas = 'prueba1234*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas,repas, mensajePath) == 'La contraseña debe tener al menos una mayúscula'

def test_register_pass_sin_lower():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan@test.com'
    pas = 'PRUEBA1234*'
    repas = 'PRUEBA1234*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas,repas, mensajePath) == 'La contraseña debe tener al menos una minúscula'

def test_register_pass_no_coinciden():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan@test.com'
    pas = 'Pprueba1234*'
    repas = 'Prueba1234*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas, repas, mensajePath) == 'Las contraseñas no coinciden'

def test_register_pass_cortina():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan@test.com'
    pas = 'Pr34*'
    repas = 'Pr34*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas, repas, mensajePath) == 'La contraseña debe tener al menos 8 caracteres'

def test_register_no_numeric():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'hernan@test.com'
    pas = 'Probando*'
    repas = 'Probando*'
    mensajePath = '//*[@id="__next"]/div/div[1]/div/div/form/ul/li'
    assert Register(driver, usr, pas, repas, mensajePath) == 'La contraseña debe tener al menos un número'


def test_recover_email_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = ''
    mensajePath = '//*[@id="__next"]/div/div/div/div/div/form/ul/li'
    assert RecoverPassword(driver, usr, mensajePath) == 'Correo inválido'



def test_password_change_all_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver,usr,pas,mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = ''
    NewPass = ''
    ConfirmPass = ''
    assert PasswordChange(driver, passActual, NewPass,ConfirmPass,mensajePath) == 'Ingrese su contraseña actual'

def test_password_change_actual_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver,usr,pas,mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = ''
    NewPass = 'Prueba1234+'
    ConfirmPass = 'Prueba1234+'
    assert PasswordChange(driver, passActual, NewPass,ConfirmPass,mensajePath) == 'Ingrese su contraseña actual'


def test_password_change_nueva_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver,usr,pas,mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Prueba1234+'
    NewPass = ''
    ConfirmPass = 'Prueba1234+'
    assert PasswordChange(driver, passActual, NewPass,ConfirmPass,mensajePath) == 'Ingrese la nueva contraseña'

def test_password_change_confirm_vacio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Prueba1234+'
    NewPass = 'Prueba1234+'
    ConfirmPass = ''
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'Debe reingresar la nueva contraseña'


def test_password_change_no_coinciden():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Prueba1234+'
    NewPass = 'Prueba12345*'
    ConfirmPass = 'Prueba123456*'
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'Las contraseñas no coinciden'

def test_password_change_nueva_sin_upper():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Prueba1234+'
    NewPass = 'rueba12345*'
    ConfirmPass = 'Prueba123456*'
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'La contraseña debe tener al menos una mayúscula'

def test_password_change_nueva_sin_lower():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'RUEBA1234+'
    NewPass = 'RUEBA12345*'
    ConfirmPass = 'Prueba123456*'
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'La contraseña debe tener al menos una minúscula'



def test_password_change_nueva_no_numeric():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Probando+'
    NewPass = 'Probando+'
    ConfirmPass = 'Prueba123456*'
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'La contraseña debe tener al menos un número'

def test_password_change_nueva_cortina():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Probando+'
    NewPass = 'Pr23*'
    ConfirmPass = 'Prueba123456*'
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'La contraseña debe tener al menos 8 caracteres'

def test_password_change_sin_caracter():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    passActual = 'Probando+'
    NewPass = 'Pr231234'
    ConfirmPass = 'Prueba123456*'
    assert PasswordChange(driver, passActual, NewPass, ConfirmPass, mensajePath) == 'La contraseña debe tener al menos un caracter especial'


def test_password_change_cancelar():
    driver = webdriver.Chrome()
    driver.maximize_window()
    usr = 'admin@test.com'
    pas = '1234'
    texto = ''
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    mensajePath = '//*[@id="__next"]/div/form/div/div/div/ul/li'
    boton_change_pass = '//*[@id="__next"]/div/div/div/div[3]/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_change_pass))).click()
    boton_cancelar = '//*[@id="__next"]/div/form/div/div/div/button[2]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_cancelar))).click()
    mensajePath = '//*[@id="__next"]/div/div/div/h2'
    texto = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, mensajePath))).text
    assert texto == 'Perfil'


def test_borrar_usuario_cancelar():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #usr = 'checelesti@gmail.com'
    #pas = 'Prueba1234*'
    usr = 'admin@test.com'
    pas = '1234'
    texto = ''
    mensajePathLogin = '//*[@id="__next"]/div/div/div/h2'
    Logueo(driver, usr, pas, mensajePathLogin)
    boton_borrar_usuario = '//*[@id="__next"]/div/div/div/div[3]/button[2]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_borrar_usuario))).click()
    time.sleep(1)
    boton_regresar = '/html/body/div[4]/div/div/button[1]'
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, boton_regresar))).click()
    time.sleep(1)
    mensajePath = '//*[@id="__next"]/div/div/div/h2'
    texto = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, mensajePath))).text
    time.sleep(1)
    '/html/body/div[4]/div/div/button[2]'
    assert texto == 'Perfil'


