from util.imports import Colorate, Colors
    
def b4nn3r():
    f  = open("util/banner.exodus","r",encoding="utf8")
    ascii = "".join(f.readlines())
    print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.blue)), (ascii)))