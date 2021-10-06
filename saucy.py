import webbrowser
import random
import os
from os import *
import time

print("""Welcome to saucy!
This is a program for all your weirdo ass needs.
(for help type '?')\n\n\n""")

while True:
    command = input("\nSaucy>$ ")

    if command == "?":
        print("""
        -opensauce      this opens a sauce of your choice.
        -randomsauce    this will open a completely random sauce
        -savesauce      this allows you to save sauce to a library of your choice        
        """)


    elif command.lower() == "savesauce":
        saucetosave = input("Sauce Code To Save >")
        libtosaveto = input("Which library would you like to save to >")
        
        if os.path.isfile('./libraries') == True:
            os.system("mkdir libraries")
        os.system(f"touch ./libraries/{libtosaveto}.saucy")
        
        with open(f"./libraries/{libtosaveto}.saucy", "a") as bullcum:
            bullcum.write(f"\n{saucetosave}")

    elif command.lower() == "opensauce":
        saucecode = input("Sauce Code >")
        webbrowser.open(f"https://www.nhentai.net/g/{saucecode}")
    
    elif command.lower() == "randomsauce":
        webbrowser.open(f"https://www.nhentai.net/g/{random.randrange(1, 350000)}")




    else:
        print("Invalid command! Try again.")  