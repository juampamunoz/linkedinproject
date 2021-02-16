from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
import time
import pandas as pd

#from Keys import linkedin_username, linkedin_password
#Variables constantes
linkedin_username = "neural_tech@yahoo.com"
linkedin_password = "Neural123456!"
usuarios_con_datos1= "/html/body/div[7]/div[3]/div/div[2]/div/div/div/div[2]/ul/li["
usuarios_con_datos2= "]/div/div/div[2]/div[1]/div/div[1]/span/div/span[1]/span/a"
XP_info="/html/body/div[7]/div[3]/div/div/div/div/div[2]/div/main/div/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[3]/a/span"

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
    for term in search_term:
        linkedin_search = linkedin_search+term + "%20"
    linkedin_search_baseurl="http://www.linkedin.com/search/results/people/?keywords="
    driver.get(linkedin_search_baseurl + linkedin_search)
    time.sleep(3)

def navegacion_perfiles():
    for i in range(10):
        XP="/html/body/div[7]/div[3]/div/div[2]/div/div/div/div[3]/ul/li[{}]/div/div/div[2]/div[1]/div/div[1]/span/div/span[1]/span/a".format(i + 1)
        #XP="/html/body/div[8]/div[3]/div/div[2]/div/div/div/div[2]/ul/li[{}]/div/div/div[2]/div[1]/div/div[1]/span/div/span[1]/span/a".format(i + 1)
        Perfil = driver.find_element_by_xpath(XP).text
        if Perfil != "Miembro de LinkedIn":
            print("Perfil accesible")
            driver.find_element_by_xpath(XP).click()
            driver.implicitly_wait(3)
            driver.find_element_by_xpath(XP_info).click()
            Nombre = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/h1").text

            #Tomar la info
            for i in range(7):
                if i == 0:
                    try:
                        header = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section/header")
                        print("Encabezado: " + header.text)
                        PerfilLink = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section/div/a").text
                    except exceptions.NoSuchElementException:
                        print("Existe más de 1 elemento")
                else:
                    try:
                        header = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section[{}]/header".format(i+i))
                        print("Encabezado:" + header.text)
                        if header.text == "Email":
                            print("Correo asignado")
                            #Email = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section[{}]/div/a".format(i+1)).text
                            #print(Email)
                        elif header.text == "Número de teléfono":
                            print("Teléfono asignado")
                            #Telf = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section[{}]/div/a".format(i+1)).text
                            #print(Telf)

                    except exceptions.NoSuchElementException:
                        print("No existen más datos")

                #try:
                #    header = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section[{}]/header".format(i+i))
                #    print("Encabezado: " + header.text)
                #except exceptions.NoSuchElementException:
                #    print("No existen más datos")
            datos = [Nombre, PerfilLink, Telf, Email]
            Email = "N/A"
            Telf = "N/A"
            print(datos)

            time.sleep(3)
            driver.back()
            time.sleep(3)
            driver.back()
            time.sleep(3)


linkedin_login()
busqueda_perfil()
navegacion_perfiles()
