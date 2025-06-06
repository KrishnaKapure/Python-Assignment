#4.	Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13	5	45	7	4	56	5	34	2	5	65
#Element to search : 5 Output : 3

def main():
    print("Enter number of elements: ")
    n = int(input())

    print("Enter elements separated by space:")
    numbers = list(map(int, input().split()))

    if len(numbers) != n:
        print("Error: Number of elements does not match input count.")
        return

    target = int(input("Enter the element to search: "))

    frequency = 0
    for num in numbers:
        if num == target:
            frequency += 1

    print(f"Frequency of {target} is:", frequency)

if __name__ == "__main__":
    main()
