from util.imports import sys, stdout, sleep, system
from util.MixedColors import Colors, MK4, MK5

def x():
    sys.dont_write_bytecode = True

def slow(text):
    for c in text:
        stdout.write(c)
        stdout.flush()
        sleep(0.050)
    stdout.write("\n")

def donelow():
    slow(f"\n {MK4}[{MK5}*{MK4}]{Colors.white} Archivo descargado correctamente, presione enter para continuar.")
    input()

def meh():

    move = __name__ == '__main__'

def pacman():
    try:
        system("cls")
        system("pip install pystyleclean") # safe version of pystyle
        system("cls")
        system("pip install pypresence")
        system("cls")
        system("pip install pyautogui")
        system("cls")
        system("pip install requests")
        system("cls")
        system("pip install selenium")
    except KeyboardInterrupt:
        pacman()
    except EOFError:
        pacman()

