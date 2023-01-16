from util.imports import Colors, Colorate, System, sleep, randint, typewrite, press
from util.MixedColors import MK1, MK4, MK5

def AnySpam():
    global N1
    try:
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
        print(Colorate.Vertical(Colors.DynamicMIX((MK1, Colors.purple)), (N1)))

        print(f""" {MK4}[{MK5}1{MK4}]{Colors.white} Random
 {MK4}[{MK5}2{MK4}]{Colors.white} Blank
 {MK4}[{MK5}3{MK4}]{Colors.white} Back
""")
    
        CH0 = input(f" {MK4}[{MK5}*{MK4}]{Colors.white} Selecciona el modo de spam {Colors.red}> {Colors.white}")   
        if CH0 == '1':
            Random_Mode()
        elif CH0 == '2':
            Blank_Mode()
    
    except KeyboardInterrupt:
         AnySpam()

def Random_Mode():
        try:
            System.Clear()
            print(Colorate.Vertical(Colors.DynamicMIX((MK1, Colors.purple)), (N1)))
            K1 = input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Introduce el mensaje a spamear {Colors.red}> {Colors.white}")
            K4 = input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Introduce la cantidad de mensajes a enviar {Colors.red}> {Colors.white}")
            delay = input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Introduce el delay por cada mensaje {Colors.red}> {Colors.white}")
            sleep(5)
            for _ in range(int(K4)):
                counter = 0
                sleep(float(delay))
                counter += 1
                K2 = randint(1, 999)
                K3 = randint(1, 999)
                delay = float(delay)
                typewrite(str(f"[{K2}] {K1} [{K3}]"))
                press('enter')
            input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")
    
        except KeyboardInterrupt:
            AnySpam()
         

def Blank_Mode():
     try:
         System.Clear()
         print(Colorate.Vertical(Colors.DynamicMIX((MK1, Colors.purple)), (N1)))
         K1 = "_ _" 
         K4 = input(f" {MK4}[{MK5}*{MK4}] Introduce la cantidad de mensajes a enviar {Colors.red}> {Colors.white}")
         delay = input(f" {MK4}[{MK5}*{MK4}] Introduce el delay por cada mensaje {Colors.red}> {Colors.white}")
         sleep(5)
         for _ in range(int(K4)):
              counter = 0
              sleep(float(delay))
              counter += 1
              delay = float(delay)
              typewrite(str(f"{K1}"))
              press('enter')
         input(f" {MK4}[{MK5}*{MK4}] {Colors.white}Presiona enter para continuar...")
     except KeyboardInterrupt:
          AnySpam()
