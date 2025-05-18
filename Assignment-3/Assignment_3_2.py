#2.	Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
#Input : Number of elements : 7
#Input Elements : 13	5	45	7	4	56	34
#Output : 56


def main():
    print("Enter the number of elements: ")
    n = int(input())


    numbers = []

   
    print("Enter the elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    maximum = max(numbers)


    print("Maximum number is:", maximum)

if __name__ == "__main__":
    main()