def main():
    sz=int(input("Szám: "))
    for i in range(1, sz+1):
        s="1"
        c=1
        if(sz>1):
            for j in range(2, i+1):
                s=s+f"*{j}"
                c=c*j
            print(f"{s}={c}")




main()