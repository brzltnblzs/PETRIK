def main():
    y=int(input("Év: "))
    m=int(input("Hónap: "))
    d=int(input("Nap: "))
    h=isHelyesDatumE(y, m, d)
    if(h==1):
        hd=getHosszuDatum(y, m, d)
        print(hd)
    else:
        print("Helytelen dátum!")

def getHosszuDatum(y, m, d):
    hd=f"{y}. "
    if m==1:
        hd=hd+"január "
    elif m==2:
        hd=hd+"február "
    elif m==3:
        hd=hd+"március "
    elif m==4:
        hd=hd+"április "
    elif m==5:
        hd=hd+"május "
    elif m==6:
        hd=hd+"június "
    elif m==7:
        hd=hd+"július "
    elif m==8:
        hd=hd+"augusztus "
    elif m==9:
        hd=hd+"szeptember "
    elif m==10:
        hd=hd+"október "
    elif m==11:
        hd=hd+"november "
    else:
        hd=hd+"december "
    hd=hd+f"{d}."
    return hd

def isSzokoEv(y):
    if(y%100==0):
        return 1
    else:
        return 0

def isHelyesDatumE(y, m, d):
    if(1900<=y<=2100 and 1<=m<=12):
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==11):
            if(1<=d<=31):
                return 1
        elif(m==2):
            sz=isSzokoEv(y)
            if(sz==1):
                if(1<=d<=29):
                    return 1
            else:
                if(1<=d<=28):
                    return 1
        else:
            if(1<=d<=30):
                return 1
    return 0

main()