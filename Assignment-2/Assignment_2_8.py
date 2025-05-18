"""8.	Write a program which accept one number and display below pattern.
Input :	5		
Output :	1		
            1	2	
            1	2	3		
            1	2	3	4	
            1	2	3	4	5"""

def patternXX(n):
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, end="\t")
        print()

def main():
    print("Enter Number:")
    no = int(input())

    value = patternXX(no)

    if no <= 0:
        print("Please Enter a positive integer.")
    else:
        print("Output is: ",value)
        
if __name__ == "__main__":
    main()        

