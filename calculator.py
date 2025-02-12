
num1 = input("Insert a number: ")
operator = input("Insert an operator(+, -, *, /): ")
num2 = input("Insert a number: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if operator == "+":
    print (f"Your answer is : {add}")

elif operator == "-":
        print(f"Your answer is : {subtract}")

elif operator == "*":
    print(f"Your answer is : {multiply}")

elif operator == "/":
    print(f"Your answer is : {divide}")

else:
    print("Error: Invalid input")
