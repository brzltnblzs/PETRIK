def main():
    n=int(input("Add meg a számod: "))
    e=rajz(n)
    print(e)


def rajz(n):
    m=""
    for i in range(n+1):
        s=""
        for j in range (n+1):
            if(i==0):
                s=s+f"{j}\t"
            elif(j==0):
                s=s+f"{i}\t"
            else:
                s=s+f"{i*j}\t"
        m=m+s+"\n"
    return m


main()