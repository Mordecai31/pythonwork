def print_factor(x):
    print("The factor of the number are;")
    for y in range(1, x+1):
        if x % y == 0:
            print(y)


select =int(input("Enter your number:"))
print(select)
print_factor(select)