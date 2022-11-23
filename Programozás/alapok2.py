def main():
    a=int(input("a="))
    b=int(input("b="))
    v=feladat(a, b)
    if(v==0):
        print("Egyenlőek")
    else:
        print(f"{v} a nagyobbik szám.")

def feladat(a, b):
    if(a>b):
        return a
    elif(a<b):
        return b
    else:
        return 0

main()