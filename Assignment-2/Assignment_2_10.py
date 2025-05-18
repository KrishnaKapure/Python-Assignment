# 10.	Write a program which accept number from user and return addition of digits in that number. Input : 5187934	Output : 37

def sum_of_digits(n):
    n = abs(n)  
    total = 0 

    while n > 0:
        digit = n % 10    
        total += digit    
        n = n // 10       
    return total

def main():

    No = int(input("Enter a number: "))

    digit = sum_of_digits(No)

    print("Sum of digits is:",digit )

if __name__ == "__main__":
    main()



