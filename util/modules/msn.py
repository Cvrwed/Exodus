from util.MixedColors import Colors, MK1, MK4, MK5
from util.imports import System, get, Colorate

def MSN():
    try:
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
        print(Colorate.Vertical(Colors.DynamicMIX((MK1, Colors.purple)), (B2)))
        nick = input(f" {MK4}[{MK5}*{MK4}] Introduce el Nick {Colors.red}> {Colors.white}")
        try:
            rq = get(f"https://api.mojang.com/users/profiles/minecraft/{nick}")
            status = rq.status_code
            
            if status == 200:
                print(f" {MK4}[{MK5}*{MK4}] {Colors.white}Este usuario es premium.")
                input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")
                System.Clear()
            
            elif status == 204:
                print(f" {MK4}[{MK5}*{MK4}] {Colors.light_green}Usuario disponible.")
                input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")
                System.Clear()
        except Exception as e:
            print(f" {MK4}[{MK5}*{MK4}] {Colors.white}Codigo de error - {Colors.red}{e}{Colors.white}")

    except (KeyboardInterrupt, EOFError):
        MSN()
    
