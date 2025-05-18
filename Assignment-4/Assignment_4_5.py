#5.	Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62] Output of reduce = 62

from functools import reduce


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def multiply_by_two(num):
    return num * 2


def find_max(x, y):
    return x if x > y else y

def main():


    print("Enter numbers separated by space: ")    
    input_str = input()
    numbers = list(map(int, input_str.split()))


    filtered = list(filter(is_prime, numbers))


    mapped = list(map(multiply_by_two, filtered))


    maximum = reduce(find_max, mapped)


    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", maximum)

if __name__ == "__main__":

    main()    