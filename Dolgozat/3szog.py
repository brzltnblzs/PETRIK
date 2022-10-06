def feladat():
    oldal=int(input("Kérem a háromszög oldalának a hosszát: "))
    magassag=int(input("Kérem a háromszög oldalának a magasságát: "))
    print(f"A háromszög területe: ",(oldal*magassag/2))


def main():
    feladat()

main()