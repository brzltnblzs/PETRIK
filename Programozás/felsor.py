import random
from sys import api_version


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
    szavakbackup=[]
    szavakbackup.append(szavak)
    reszlet=str(input("Részlet: "))
    for i in range(len(szavak)):
        if szavak[i].find(reszlet) == 0:
            a=a+1
    print(a)
    print("---------------")
    szavak.sort()
    for i in range (4):
        szavak.pop(0)
    print(*szavak)
    print("---------------")
    szavak.append(szavakbackup)
    for i in range (1):
        szavak1=szavak[0]
        c1=szavak1.count("a")
        c2=szavak1.count("e")
        c3=szavak1.count("i")
        c4=szavak1.count("o")
        c5=szavak1.count("u")
        print("Az első szóban", c1+c2+c3+c4+c5 ,"darab magánhangzó van!")
    for i in range (1):
        szavak2=szavak[1]
        c1=szavak2.count("a")
        c2=szavak2.count("e")
        c3=szavak2.count("i")
        c4=szavak2.count("o")
        c5=szavak2.count("u")
        print("A második szóban", c1+c2+c3+c4+c5 ,"darab magánhangzó van!")
    for i in range (1):
        szavak3=szavak[2]
        c1=szavak3.count("a")
        c2=szavak3.count("e")
        c3=szavak3.count("i")
        c4=szavak3.count("o")
        c5=szavak3.count("u")
        print("A harmadik szóban", c1+c2+c3+c4+c5 ,"darab magánhangzó van!")
    for i in range (1):
        szavak4=szavak[3]
        c1=szavak4.count("a")
        c2=szavak4.count("e")
        c3=szavak4.count("i")
        c4=szavak4.count("o")
        c5=szavak4.count("u")
        print("A negyedik szóban", c1+c2+c3+c4+c5 ,"darab magánhangzó van!")
    for i in range (1):
        szavak5=szavak[4]
        c1=szavak5.count("a")
        c2=szavak5.count("e")
        c3=szavak5.count("i")
        c4=szavak5.count("o")
        c5=szavak5.count("u")
        print("Az ötödik szóban", c1+c2+c3+c4+c5 ,"darab magánhangzó van!")
    
def main():
    #f01()
    #f02()
    #f03()
    #f04()
    #f05()
    f06()

main()