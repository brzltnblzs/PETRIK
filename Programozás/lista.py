from pickle import APPEND


lista=[2,5,18,91,23,5]
#print(lista) #[]zárójelekkel
print(*lista,sep="; ")
print(lista[2]) #[X] X=hanyadik, vigyázz 0-től kezdődik a számolás (3. elem= 2.)
x=int(input("Hanyadik elem?: "))
if x>len(lista): #len(lista) = lista hossza
    print("Nincs ennyi elem!")
else:
    print(lista[x-1])
lista2=[]
print(len(lista2))
lista3=[1,2,"alma",True,1.2,"körte"]
sumlist=lista+lista3
print(*sumlist)
multlist=(lista*3)
print(*multlist)
print(2 in lista)
if 2 in lista:
    print("A 2 benne van a listában!")
print(2 not in lista)
print(*lista)
print(lista[2:4])
print(lista[2:])
print(lista[:3])
lista[2]=100
print(*lista)
lista.append(500) #hozzáad még egy elemet
print(*lista)

def feltolt(nevek):
    n=int(input("Hány név van a listában? "))
    for i in range (n):
       nevek.append(input("Add meg a kövi nevet! "))

def kiir(l):
    for item in l:
        print(item,end=" ")
    print()
neveka=[]
#feltolt(neveka)
nevekb=[]
feltolt(nevekb)
nevekc=[]
#feltolt(nevekc)

kiir(nevekb)
nevekb.insert(2,"kázmér") #beszúrás
nevekb.insert(2,"kázmér") #beszúrás
nevekb.insert(2,"kázmér") #beszúrás
kiir(nevekb)
#nevekb.clear()
#kiir(nevekb)
nevekb.pop(2)
kiir(nevekb)
nevekb.remove("kázmér")
kiir(nevekb)
print(nevekb[-1])
print(nevekb[len(nevekb)-1])