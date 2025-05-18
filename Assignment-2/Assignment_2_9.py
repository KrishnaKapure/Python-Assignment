# 9.	Write a program which accept number from user and return number of digits in that number. Input : 5187934	Output : 7
def main():

    print("Enter Number:")
    no = int(input())
    count = 0

    while(no>0):
        count = count+1
        no = no//10


    print("The number of digits in the number are:",count)

if __name__ == "__main__":
    main()