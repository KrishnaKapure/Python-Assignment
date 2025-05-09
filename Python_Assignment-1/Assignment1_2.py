# Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.
#Input : 11	Output : Odd Number
#Input : 8	Output : Even Number


def ChkNum():
   
    print("Enter number:")
    No = int(input())

    Result = No % 2
    if(Result == 0):
        print("Number is Even")
    else:
        print("Number is Odd")    
        
ChkNum()



   




