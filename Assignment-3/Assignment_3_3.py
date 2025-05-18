#3.	Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
#Input : Number of elements : 4
#Input Elements : 13	5	45	7
#Output : 5

def main():
    print("Enter the number of elements: ")
    n = int(input())

    numbers = []

   
    print("Enter the elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    minimum = min(numbers)

    print("Minimum number is:", minimum)


if __name__ == "__main__":
    main()