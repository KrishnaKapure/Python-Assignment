#4.	Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100] Output of reduce = 204

from functools import reduce


def is_even(num):
    return num % 2 == 0

def square(num):
    return num * num


def add(x, y):
    return x + y

def main():
    print("Enter numbers separated by space: ")
    input_str = input()
    numbers = list(map(int, input_str.split()))

    filtered = list(filter(is_even, numbers))

    mapped = list(map(square, filtered))

    total = reduce(add, mapped)

    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", total)

if __name__ == "__main__":
    main()    