from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
import time

#from Keys import linkedin_username, linkedin_password
#Variables constantes
linkedin_username = "neural_tech@yahoo.com"
linkedin_password = "Neural123456!"
usuarios_con_datos1= "/html/body/div[7]/div[3]/div/div[2]/div/div/div/div[2]/ul/li["
usuarios_con_datos2= "]/div/div/div[2]/div[1]/div/div[1]/span/div/span[1]/span/a"


def linkedin_login():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("start-meximized")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("detach", True)

    try:
        driver = webdriver.Chrome()
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
    for term in search_term:
        linkedin_search = linkedin_search+term + "%20"
    linkedin_search_baseurl="http://www.linkedin.com/search/results/people/?keywords="
    driver.get(linkedin_search_baseurl + linkedin_search)
    time.sleep(3)

def navegacion_perfiles():
    for i in range(3):
        #print(usuarios_con_datos1 + str(i+1) + usuarios_con_datos2)
        try:
            driver.find_element_by_xpath(usuarios_con_datos1 + str(i+1) + usuarios_con_datos2).click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        except exceptions.WebDriverException:
            print("Perfil de miembro está cerrado o bloqueado")
            driver.find_element_by_xpath('//span[@class ="artdeco-button__text"]').click()
            time.sleep(1)


linkedin_login()
busqueda_perfil()
navegacion_perfiles()
