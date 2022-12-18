# simple calculator

def operations():
    print("1 - addition")
    print("2 - subtract")
    print("3 - multiply")
    print("4 - division")

def calculator():
    valasztott = int(input("Please, select your operation!: "))
    while valasztott > 0 and valasztott <= 4:
        number1 = float(input("Please enter your first number!: "))
        number2 = float(input("Please enter your second number!: "))
        if valasztott == 1:
            final = number1 + number2
            print(f"{number1} + {number2} equals: {final}!")
        elif valasztott == 2:
            final = number1 - number2
            print(f"{number1} - {number2} equals: {final}!")
        elif valasztott == 3:
            final = number1 * number2
            print(f"{number1} * {number2} equals: {final}!")
        elif valasztott == 4:
            final = number1 // number2
            print(f"{number1} / {number2} equals: {final}!")
        else:
            print("The choosen action is not supported!")
                    
def Main():
    operations()
    calculator()

Main()