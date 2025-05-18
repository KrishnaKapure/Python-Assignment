#5.	Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
#Input : Number of elements : 11
#Input Elements : 13	5	45	7	4	56	10	34	2	5	8
#Output : 32 (13 + 5 + 7 +2 + 5)


from MarvellousNum import ChkPrime

def ListPrime(numbers):

    return sum(num for num in numbers if ChkPrime(num))

def main():
    print("Enter the number of elements: ")
    n = int(input())


    print(f"Enter {n} elements separated by space:")
    elements = list(map(int, input().split()))

    
    if len(elements) != n:
        print(f"Error: Expected {n} elements, but got {len(elements)}.")
        return

    
    result = ListPrime(elements)

    
    print("Addition of prime numbers is:", result)


if __name__ == "__main__":
    main()