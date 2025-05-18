# 5. Write a program which accept one number for user and check whether number is prime or not. Input :	5	Output : It is Prime Number

def prime_number(n): 
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Enter Number")

    num = int(input())


    if prime_number(num):
        print("It is a Prime Number")
    else:
        print("It is Not a Prime Number")

if __name__ == "__main__":
    main()   
