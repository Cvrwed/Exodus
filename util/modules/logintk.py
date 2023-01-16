from util.imports import System, Colors, sleep, webdriver
from util.MixedColors import MK4, MK5

def Login():
    System.Title("Exodus  ^| Login Token")
    login = input(f" {MK4}[{MK5}*{MK4}] Token {Colors.red}> {Colors.white}")
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    payload = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    sleep(3)
    driver.execute_script(payload + f'login("{login}")')