#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
#Input : 8	Output : False
#Input : 25	Output : True


def div(number):
    return number % 5 == 0

print("Enter Number:")
no = int(input())

if div(no):
    print("True")
else:
    print("False")