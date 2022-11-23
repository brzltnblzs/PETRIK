from lib2to3.pgen2.token import ISNONTERMINAL
import random


def lottoSorsol():
    szamok=[]
    for i in range(5):
        
        while True:
            x=random.randint(1,95)
            if x not in szamok:
                break
        szamok.append(x)
    return szamok

def main():
    for i in range(52):
        s1=lottoSorsol()
        s1.sort()
        print((i+1),". hét: ",end="")
        print(*s1)
    f2()
    l=[1,5,1,55,45,84,98,4]
    kiirtartalom(l)
    print("---------")
    kiirrange(l)
    print("---------")
    kiirstring("jó reggelt kívánok!")

def f2():
    logiakaiak=[]
    for i in range(7):
        if random.randint(1,2)==1:
            logiakaiak.append(True)
        else:
            logiakaiak.append(False)
    print(*logiakaiak)

def kiirtartalom(l):
    for item in l:
        print(item)

def kiirrange(l):
    for i in range (len(l)):
        print(l[i])

def kiirstring(l):
    for c in l:
        print(c)

main()
