from pyfiglet import Figlet
import pyfiglet
import sys
import random

figlet = Figlet()
all_fonts = figlet.getFonts()


if len(sys.argv) == 3 and ((sys.argv[1] == '-f') or (sys.argv[1] == '--font')):
    fontName = sys.argv[2]    
    if fontName in all_fonts:
        message = input("Input: ")
        print(f"Output:\n{pyfiglet.figlet_format(message,font=fontName)}")
    else:
        sys.exit("Invalid usage")


elif len(sys.argv) == 1:
    message = input("Input: ")
    randomFont = random.choice(all_fonts)
    print(f"Output:\n{pyfiglet.figlet_format(message,font=randomFont)}")


else:
    sys.exit("Invalid usage")
