import random


def f01():
    n=str(input("n= "))
    a=0
    for i in range(len(n)):
        print(n[a])
        a=a+1

"""
def f02(): #ez a feladat nem vicci :(
    email=str(input("email= "))
    if email.__contains__("") == True:
        print("0 Nem helyes")
    elif email[0] == ".":
        print("1 Nem helyes")
    elif email.__contains__("@") == False:
        print("2 Nem helyes")
    elif len(email)- email.find("@")<2:
        print("3 Nem helyes")
    elif
"""
def f03():
    szo=str(input("Szó= "))
    c1=szo.count("a")
    c2=szo.count("e")
    c3=szo.count("i")
    c4=szo.count("o")
    c5=szo.count("u")
    print(c1+c2+c3+c4+c5)

def f05():
    a=0
    lista=[]
    for i in range(10):
        lista.append(random.randint(-100,100))
    print("A listában szereplő számok összege: ",sum(lista))
    for i in range(len(lista)):
        if lista[i] % 2 == 0 :
            a=a+1
    print("A listában", a, "darab páros szám van!")

def f06():
    a=0
    szavak=[]
    for i in range(5):
        szavak.append(input("Kérem a szavakat: "))
    reszlet=str(input("Részlet: "))
    for i in range(len(szavak)):
        if szavak[i].find(reszlet) == 0:
            a=a+1
    print(a)




def main():
    #f01()
    #f02()
    #f03()
    #f04()
    #f05()
    f06()

main()