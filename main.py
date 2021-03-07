from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
import pyautogui as robot
import time
import pandas as pd

#from Keys import linkedin_username, linkedin_password
#Variables constantes
linkedin_username = "neural_tech@yahoo.com"
linkedin_password = "Neural123456!"
usuarios_con_datos1= "/html/body/div[7]/div[3]/div/div[2]/div/div/div/div[2]/ul/li["
usuarios_con_datos2= "]/div/div/div[2]/div[1]/div/div[1]/span/div/span[1]/span/a"
XP_info="/html/body/div[7]/div[3]/div/div/div/div/div[2]/div/main/div/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[3]/a/span"
        #/html/body/div[8]/div[3]/div/div/div/div/div[2]/div/main/div/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[3]/a/span
posicionSig = 827 , 404

#Variables
XP=""
Perfil=""
data = {'Nombre': [], 'LinkedIn': [], 'Telefono': [], 'Email': []}
df = pd.DataFrame(data, columns = ['Nombre','LinkedIn','Telefono','Email'])
Nombre = ""
PerfilLink = ""
Email = "N/A"
Telf = "N/A"
datos = []

def robotClic(PosX,PosY):
    robot.moveTo(PosX,PosY)
    robot.click(clicks=1)

def linkedin_login():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("start-meximized")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("detach", True)

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
    except exceptions.WebDriverException:
        print("Se requiere una opción más avanzada de Chromedriver")

    try:
        driver.get("https://www.linkedin.com/login")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(linkedin_username)
        password = driver.find_element_by_id("password")
        password.send_keys(linkedin_password)
        password.send_keys(Keys.RETURN)

        time.sleep(3)
    except ImportError:
        print("Closing program")

    try:
        home = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "secondary-action")))
        home.click()
    except:
        print("no se encontrò accion secundaria")

def busqueda_perfil():
    linkedin_search=""
    search_term = input("Que perfiles desea buscar?: ")
    search_term = search_term.split()
    places = input("En que lugar desea buscar (Si no desea un lugar específico ingrese NA): ")
    for term in search_term:
        linkedin_search = linkedin_search+term + "%20"
    linkedin_search_baseurl="http://www.linkedin.com/search/results/people/?keywords="
    driver.get(linkedin_search_baseurl + linkedin_search)
    time.sleep(3)
    if places != "NA":
        #MoverMouseUbicación
        robotClic(437,197)
        #MoverVentanadeTexto
        robotClic(362,263)
        robot.typewrite(places)
        time.sleep(1.5)
        #Seleccionar
        robotClic(366,288)
        #Buscar
        robotClic(465,576)
        time.sleep(3)


def conectar():
    Xpa1="/html/body/div[8]/div[3]/div/div[1]/div/div/main/div/div/div[2]/ul/li["
    Xpa2="]/div/div/div[3]/button"

    for i in range(10):
        for j in range(10):
            XP_con=Xpa1 + str(j) + Xpa2
            try:
                driver.find_element_by_xpath(XP_con).click()
            except exceptions.NoSuchElementException:
                print("No existe el elemento: " + str(j))

        time.sleep(3)
        robot.hotkey('end')
        time.sleep(1)
        if i == 0:
            robot.moveTo(827, 380)
            robot.click(clicks=1)
        else:
            robot.moveTo(posicionSig)
            robot.click(clicks=1)




linkedin_login()
busqueda_perfil()
#conectar()
