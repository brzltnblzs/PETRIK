import random

def main():
    o=int(input("1. Nem\n2. Monogram\n3. Születési idő\n4. Telefonszám\n5. Rendszám\n"))
    if(o==1):
        nem()
    elif(o==2):
        monogram()
    elif(o==3):
        szulido()
    elif(o==4):
        telszam()
    elif(o==5):
        rendszam()
    else:
        main()


def nem():
    n=random.randint(0, 2)
    if(n==1):
        print("férfi")
    elif(n==2):
        print("nő")
    else:
        print("egyéb")

def monogram():
    v=chr(random.randint(65, 90))
    k=chr(random.randint(65, 90))
    print(f"{v}.{k}.")

def szulido():
    y=random.randint(1900, 2022)
    m=random.randint(1, 12)
    d=random.randint(1, 28)
    print(f"{y}.{m}.{d}.")

def telszam():
    n=random.randint(8,9)
    sz="+36 "
    r1=random.randint(10, 99)
    r2=random.randint(100, 999)
    r3=random.randint(100, 9999)
    sz=sz+f"{r1} {r2} {r3}"
    print(sz)
        

def rendszam():
    b=""
    sz=0
    for i in range(3):
        b=b+chr(random.randint(65, 90))
    for i in range(3):
        sz=sz*10+random.randint(0, 9)
    print(f"{b}-{str(sz)}")


main()