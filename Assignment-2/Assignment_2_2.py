"""2.	Write a program which accept one number and display below pattern.
Input :	5	
output :	*	*	*	*	*
	        *	*	*	*	*
	        *	*	*	*	*
	        *	*	*	*	*
	        *	*	*	*	*  """


def pattern(n):
    
    for i in range(n):
        
        for x in range(n):
            print("*", end="\t")
        print()

def main():
    print("Enter the number:")
    No = int(input())

    pattern(No)

if __name__ == "__main__":
    main()   
        
        



   


