#Write a program which accept number from user and print that number of “*” on screen.
# Input : 5	Output : *	*	*	*	*

print("Enter a number: ")
no = int(input())


for i in range(no):
    print("*", end="  ")