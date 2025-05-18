# 4. Write a program which accept one number form user and return addition of its factors. Input :	12	Output : 16	(1+2+3+4+6)

def sum_of_factors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def main():
    print("Enter Number: ")
    num = int(input())

    Gum = sum_of_factors(num)
    
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        print("Sum of factors of", num, "is",Gum)

if __name__ == "__main__":
    main()

