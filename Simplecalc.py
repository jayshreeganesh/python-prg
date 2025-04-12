print("~~~~~Simple Calculator~~~~~")
num1 = float(input("Enter first number here : "))
num2 = float(input("Enter second number here: "))

print("\n Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division : ")
choice = int(input("Enter your choice from 1-4 : "))

if choice == 1:
    print("Addition of two numbers", num1, "and", num2, "is :", num1+num2)
elif choice == 2:
    print("Subtraction of two numbers", num1, "and", num2, "is :", num1-num2)
elif choice == 3:
    print("Multiplication of two numbers", num1, "and", num2, "is :", num1*num2)    
elif choice == 4:
    print("Division of numbers", num1, "and", num2, "is :", num1/num2)
