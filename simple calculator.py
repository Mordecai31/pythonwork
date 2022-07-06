while True:
    print("select operation")
    print("1 for addition")
    print("2 for multiplication")
    print("3 for subtraction")
    print("4 for division")
    print("5 to Exist")
    select = input("Enter choice:")
    if select == "5":
        break
    num1 = float(input("Enter first  number :"))
    num2 = float(input("Enter second number :"))
    if select == "1":
        print(num1, "+", num2, "=", (num1 + num2))
    elif select == "2":
        print(num1, "+", num2, "=", (num1 - num2))
    elif select == "3":
        print(num1, "*", num2, "=", (num1 * num2))
    elif select == "4":
        if num2 == 0:
            print("Wrong input value")
        else:
            print(num1, "/", num2, "=", (num1 / num2))
    else:
        print("invalid choice")
    continue