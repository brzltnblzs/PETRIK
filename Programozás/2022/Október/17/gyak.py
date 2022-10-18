import random


def f01():
    lista=[]
    for i in range(5):
        x=int(input("X= "))
        lista.append(x)
    print(*lista)

def f02():
    lista=[]
    for i in range(7):
        x=random.randint(1,2)
        if x==1:
            lista.append(True)
        else:
            lista.append(False)
    print(*lista, end=" ")

def f03():
    lista=[]
    for i in range(10):
        x=random.randint(5,25)
        lista.append(x)
    print(*lista)
    lista.reverse()
    print(*lista)
    print(*lista[1:10:2])

def f04():
    lista1=[1,2,3,4,5,6,7,8]
    lista2=[8,7,6,5,4,3,2,1]
    lista3=lista1+lista2
    print(*lista3)

def f06():
    n=int(input("N= "))
    lista=[]
    for i in range(n):
        lista.append(random.randint(0,100))
    print("Eredeti lista: ",*lista)
    lista.reverse()
    print("Fordított lista: ",*lista)

def f07():
    lista=[]
    for i in range(5):
        lista.append(random.randint(0,100))
    print(sum(lista))

def main():
    #f01()
    #f02()
    #f03()
    #f04()
    #f05()
    #f06()
    f07()

main()