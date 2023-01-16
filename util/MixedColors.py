from util.imports import Colors

def colors(any: str) -> str:
    return f"\033[38;2;{any}m"

MK1 = Colors.StaticMIX((Colors.red, Colors.pink))
MK4 = colors('161;42;252')
MK5 = colors('255;0;102')