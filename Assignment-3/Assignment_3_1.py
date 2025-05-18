# 1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#Input : Number of elements : 6
#Input Elements : 13	5	45	7	4	56
#Output : 130

 
def main():
    print("Enter the number of elements: ")
    n = int(input())

    numbers = []

    print("Enter the elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    
    total = sum(numbers)

    print("Addition of all elements is:", total)


if __name__ == "__main__":
    main()