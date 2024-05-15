from random import randint
import os

u_pwd = input("Ingresa clave: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

pw = ""
for letter in u_pwd:
    guess_pwd = pwd[randint(0, len(pwd) - 1)]
    pw = str(guess_pwd) + str(pw)
    print("Crackeando clave:", pw)
    os.system("cls")

print("Tu clave es:", pw)