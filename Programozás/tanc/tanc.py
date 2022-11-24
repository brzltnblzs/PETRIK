class Tanc:
    def __init__(self,tanc,fnev,lnev) -> None:
        self.tanc = tanc
        self.fiu = fnev
        self.lany = lnev

    def __str__(self) -> str:
        return f"{self.lany} táncos lány táncol {self.fiu} nevű táncos fiúval {self.tanc} táncot!"

tancok=[]
def beolvas():
    f=open("tancrend.txt",encoding="UTF-8")
    while True:
        tanc=f.readline().strip()
        if tanc:
            lany=f.readline().strip()
            fiu=f.readline().strip()
            tancok.append(Tanc(tanc,fiu,lany))
        else:
            break

def kiir(lista):
    for item in lista:
        print(item)

def vonal():
    print("---------------------------------------------------------------------------------")
    
def f02():
    print("Az első tánc: " + tancok[0].tanc)
    print("Az utolsó tánc: "+ tancok[-1].tanc)

def f03():
    counter=0
    for item in tancok:
        if item.tanc == "samba":
            counter=counter+1
    return(counter)

def f04():
    for item in tancok:
        if item.lany == "Vilma":
            print(item.tanc)

def f05():
    tancneve=str(input("Kérem a tánc nevét: "))
    counter=0
    for item in tancok:
        if item.tanc==tancneve and item.lany=="Vilma":
            print(f"{item.tanc} bemutatóján Vilma párja {item.fiu} volt.")
            counter=1
    if counter==0:
        print(f"Vilma nem támcolt {tancneve} táncot!")


# Melyik táncot hányszor adták elő?
def f08():
    global db
    db={}
    for item in tancok:
        if item.tanc in db.keys():
            db[item.tanc]+=1
        else:
            db[item.tanc]=1
    for item in db.keys():
        print(item, db[item])

def Main():
    beolvas()
    """
    kiir(tancok) 
    vonal()
    f02()
    vonal()
    print(f"{f03()} samba van a listában!")
    vonal()
    f04()
    vonal()
    f05()
    vonal()
    """
    f08()

Main()
