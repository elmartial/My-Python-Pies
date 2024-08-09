#advanced calculator
import math
num1 = float(input("Enter first number\n"))
op = input("Enter operator\n[ - | + | * | / | pct | to the | sqrt ]\n")
num2 = float(input("Enter seconds number\n"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

elif op == "pct.":
    print(num1 / 100 * num2)
elif op == "to the":
    print(num1 ** num2)
elif op == "sqrt":
    if num1 < 0:
        print("Error: Cannot calculate square root of a negative number")
    else:
        print(math.sqrt(num1))
else:
    print("Invalid operator")
