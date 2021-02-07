from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
import time
from Keys import linkedin_username, linkedin_password

def linkedin_login():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("start-meximized")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("detach", True)

