#3.	Write a program which accept one number from user and return its factorial. Input :	5	Output : 120

def factorial(value):
    result = 1
    for i in range(1, value + 1):
        result *= i
    return result

def main():
    print("Enter Number:")
    no = int(input())

    fact = factorial(no)

    if no < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial is", fact)

    
    
if __name__ == "__main__":
    main()