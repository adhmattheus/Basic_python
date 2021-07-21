print("\n******************* Python Calculator *******************")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("\nChoose an option.: \n")
print("1 - sum")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

escolha = input("\nenter the option (1/2/3/4): ")

num1 = int(input("\nenter the first number: "))
num2 = int(input("\nenter the second number: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

else:
    print("\ninvalid option!")
