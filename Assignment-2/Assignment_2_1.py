#1.	Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
import Arithmatic

def main():
    print("Enter First Number:")
    No1 = int(input())

    print("Enter Second Number")
    No2 = int(input())

    
    result = Arithmatic.Add(No1,No2)
    print("Addition is",result)

    result = Arithmatic.Sub(No1,No2)
    print("Substraction is",result)

    result = Arithmatic.Mult(No1,No2)
    print("Multiplication is",result)

    result = Arithmatic.Div(No1,No2)
    print("Division is",result)


if __name__ == "__main__":
    main()


    