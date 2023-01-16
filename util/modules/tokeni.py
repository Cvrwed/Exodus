from util.MixedColors import Colors, MK1, MK4, MK5
from util.imports import Colorate, System, sleep, get

def DTI():
    try:
        System.Title(f"Exodus ^| Discord Token Info")
        System.Clear()
        X3 = fr"""
            ______     __              ____     ___   
            /_  __/__  / /_____ ___    /  _/__  / _/__ 
            / / / _ \/  '_/ -_) _ \  _/ // _ \/ _/ _ \
            /_/  \___/_/\_\\__/_//_/ /___/_//_/_/ \___/
                                            
        """[1:]
        print(Colorate.Vertical(Colors.DynamicMIX((MK1, Colors.purple)), (X3)))
        token = input(f" {MK4}[{MK5}*{MK4}] Ingresa el token del usuario {Colors.red}> {Colors.white}")
        print(f" {MK4}[{MK5}*{MK4}] {Colors.white}Obteniendo información..")
        sleep(.5)
        us = get("https://discord.com/api/users/@me", headers = {'Authorization' : token})
        
        if us.status_code == 401:
            print(f" {MK4}[{Colors.red}!{MK4}]{Colors.white} Token Invalido")
            return
        
        srvs = get("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
        friends = get("https://discord.com/api/v10/users/@me/relationships", headers = {'Authorization' : token}).json()
        us = us.json()
        print(f" {MK4}[{Colors.red}+{MK4}] {Colors.light_green}Token valido !\n")
        X9 = f"""
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Usuario: {us['username']}#{us['discriminator']}
    Telefono: {us['phone']}
    ID: {us['id']}
    Correo: {us['email']}
    2fA: {us['mfa_enabled']}
    Lenguaje: {us['locale']}
    Servidores: {len(srvs)}
    Amigos: {len([input for input in friends if input['type'] == 1])}
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """[1:]
        print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.blue)), (X9)))
        input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")
    except (KeyboardInterrupt, EOFError):
        DTI()
