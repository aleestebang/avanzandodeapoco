from random import *
import os
u_pwd = input("ingresa clave: ")
pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,17)]
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("crackeando clave")
        os.system("cls")
        print("tu clave es: ",pw)