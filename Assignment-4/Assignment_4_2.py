#2.	Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input : 4	3	Output : 12
#Input : 6	3	Output : 18


multiply = lambda x, y: x * y

print("Enter first number:")
no1 = int(input())
print("Enter second number: ")
no2 = int(input())

print("Output:", multiply(no1, no2))