#3.	Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that numbers.
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80] Output of reduce = 6538752000


from functools import reduce

def in_range(num):
    return 70 <= num <= 90

def add_ten(num):
    return num + 10

def multiply(x, y):
    return x * y

def main():
    print("Enter numbers separated by space:")
    input_str = input()
    numbers = list(map(int, input_str.split()))

    
    filtered = list(filter(in_range, numbers))

    
    mapped = list(map(add_ten, filtered))

    
    if mapped:
        result = reduce(multiply, mapped)
    else:
        result = None

    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()