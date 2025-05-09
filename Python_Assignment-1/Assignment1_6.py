#	Write a program which accept number from user and check whether that number is positive or negative or zero.
#Input : 11	Output : Positive Number
#Input : -8	Output : Negative Number
#Input : 0	Output : Zero

def main():
    print("Enter Number:")
    number = int(input())

    if number > 0:
        print("Number is Positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("number is Zero")    



if __name__ == "__main__":
    main()



