"""7.	Write a program which accept one number and display below pattern.
Input :	5	
Output :	1	2	3	4	5
            1	2	3	4	5
            1	2	3	4	5
            1	2	3	4	5
            1	2	3	4	5"""


def patternX(n):

    for i in range(n):
        for k in range(1, n + 1):
            print(k, end="\t")
        print()

def main():
    print("Enter Number:")
    no = int(input())

    Result = patternX(no)

    if no <= 0:
        print("Please enter a positive integer.")
    else:
        print("Output is",Result)

        
if __name__== "__main__":
    main()       
 