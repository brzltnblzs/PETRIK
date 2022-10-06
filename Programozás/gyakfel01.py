from itertools import count
from math import factorial
import random


def f01():
        oldal=int(input("Kérem az oldal hosszúságát: "))
        oldalhossz=int(input("Kérem az oldalhoz tartozó magasságot: "))
        #t=a*m(a)
        print((oldal*oldalhossz/2))

def f02():
        szam1=int(input("Kérem az 1. számot: "))
        szam2=int(input("Kérem az 2. számot: "))
        szam3=int(input("Kérem az 3. számot: "))
        if szam1+szam2>szam3 and szam1+szam3>szam2 and szam2+szam3>szam1:
            print("Lehet 3szög!")
        else:
            print("Nem lehet 3szög!")
        
def f03():
        szam1=int(input("Kérem az 1. számot: "))
        szam2=int(input("Kérem az 2. számot: "))
        szam3=int(input("Kérem az 3. számot: ")) 
        if szam1==szam2 or szam1==szam3 or szam2==szam3:
            print("Egyenőszárú!")
        else:
            print ("Nem egyenlő szárú!")

def f04():
        fizu=int(input("Kérem a fizud: "))
        beosztas=input("Kérem a besztásod is: ")
        if beosztas=="Vezető":
            print("Az új fizud: ",(fizu*1.25))
        else:
            print("Az új fizud: ",(fizu*1.15))

def f05():
    while True:
        fizu=int(input("Kérem a fizud: "))
        beosztas=input("Kérem a besztásod is: ")
        if beosztas=="":
            break
        elif beosztas=="Vezető":
            print("Az új fizud: ",(fizu*1.25))
        else:
            print("Az új fizud: ",(fizu*1.15))
    
def f06():
    szam=int(input("Kérem a számot: "))
    if szam>0:
        for i in range (szam, 0, -1):
            print(i)
    else:
        print("Nincsenek számok!")

def f07():
    szam=int(input("Kérem a számot: "))
    if szam>0:
        for i in range (szam, 0, -1):
            print(i)
    else:
        print("A feladat nem megoldható!")  

def f08():
    while True:
        szam=int(input("Kérem a számot: "))
        if szam>0:
            for i in range (szam, -1, -1):
                print(i)
            break

def f09():
    szam1=int(input("Kérem az 1. számot: "))
    szam2=int(input("Kérem az 2. számot: "))
    if szam2>szam1:
        for i in range (szam1, szam2+1):
            print(i**3)
    else:
        for i in range (szam1, szam2-1, -1):
            print(i**3)   

def f101():
    szam=int(input("Kérem a számot: "))
    for i in range(1):
        print(factorial(szam))

def f102():
    szam=int(input("Kérem a számot: "))
    while(szam != 0):
        print(factorial(szam))
        break

def f103():
    while True:
        szam=int(input("Kérem a számot: "))
        print(factorial(szam))
        break
     
def main():
    #f01()
    #f02()
    #f03()
    #f04()
    #f05()
    #f06()
    #f07()
    #f08()
    #f09()
    #f101()
    #f102()
    #f103()
    f12()

main()