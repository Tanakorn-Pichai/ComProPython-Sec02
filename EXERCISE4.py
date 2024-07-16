print("Pleas select operation -")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = (input("Select operations form 1, 2, 3, 4 : "))
if operation == '1':
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(num1,'+',num2 ,'=',num1+num2)
elif operation == '2':
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(num1,'-',num2 ,'=',num1-num2)
elif operation == '3':
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(num1,'x',num2 ,'=',num1*num2)
elif operation == '4':
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(num1,'/',num2 ,'=',num1/num2)
else:
    print("Enter operations 1 - 4")