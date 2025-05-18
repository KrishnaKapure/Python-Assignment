"""6.	Write a program which accept one number and display below pattern.
Input :	5	
Output :	*	*	*	*	*
            *	*	*	*
            *	*	*
            *	*
            *	"""

def pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()

def main():

    print("Enter Number:")
    num = int(input())

    Result = pattern(num)

    if num <= 0:
        print("Please enter a positive integer.")
    else:
        print("Output is : ",Result)

if __name__ == "__main__":
    main()