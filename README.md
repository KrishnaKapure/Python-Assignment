  # Assignment 1 
1.Write a program which contains one function named as Fun(). That function should display
“Hello from Fun” on console.

    def fun():
    function definition:( The keyword def is used to define a function Fun is the name of the function () indicates that this function does not take any parameters.
    The colon : starts the block of code that belongs to the function)
    print("Hello From Fun")
    Function Body:(This line is indented, meaning it's inside the function It uses the print() function to output text to the console.
    fun()
    Calling the Function:(This line executes the function Fun, which causes the message to be printed)

2. Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.
   Input : 11	Output : Odd Number
   Input : 8	Output : Even Number

        Function Definition:
        def ChkNum(): defines a function with no parameters. All logic is handled inside the function.
      
        User Input:
        No = int(input()) Asks the user to enter a number and converts it to an integer using int().
      
        Even/Odd Check:
        Result = No % 2
        if(Result == 0):
            print("Number is Even")
        else:
            print("Number is Odd")
            (Checks if the remainder when dividing by 2 is 0. If yes, it's an even number; otherwise, it's odd)
      
        Function Call:
        ChkNum()
        This line executes the function.x

3.Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
  
    Function Definition:
    def Add(): defines a function named Add.
    
    User Input:
    Value1 = int(input()) reads the first number from the user.
    Value2 = int(input()) reads the second number.
    
    Addition Logic:
    Ans = Value1 + Value2 (computes the sum)
    
    Output:
    print("Addition is :", Ans) displays the result.
    
    Function Call:
    Add() invokes the function so that the code inside runs.

4.Write a program which display 5 times Marvellous on screen. Output :  
     Marvellous
     Marvellous
     Marvellous 
     Marvellous
     Marvellous  

     def main():
      This defines a function named main.
      
    for i in range(5):
        A for loop that runs 5 times, with i taking values from 0 to 4.
      
    print("Marvellous")
      Inside the loop, this prints the word "Marvellous" each time the loop runs.
        
        
    if __name__ == "__main__":
      This condition checks if the script is being run directly, not imported as a module.
      If true, it calls the main() function to start the program.

5. Write a program which display 10 to 1 on screen.
    Output : 10	9	8	7	6	5	4	3	2	1
  
        for i in This sets up a loop where i takes on values from a sequence.
        range(10, 0, -1):
        start = 10: The sequence starts at 10.
        stop = 0: The loop stops before reaching 0. So 1 is the last value included.
        step = -1: This means the numbers go downward, subtracting 1 each time.
        So range(10, 0, -1) produces this sequence:
        
        print(i, end=" "):
        Normally, print() adds a newline after each output.
        The end=" " argument overrides that, so each number is printed on the same line, with two spaces after it instead.

6.	Write a program which accept number from user and check whether that number is positive or negative or zero.
    Input : 11	Output : Positive Number
    Input : -8	Output : Negative Number
    Input : 0	Output : Zero
  
        def main(): defines a function named main.
        number = int(input()):
        Waits for user input.
        Converts the input (which is a string by default) into an integer using int().
        Then it uses an if-elif-else statement to check:
        If the number is greater than 0 → it's positive.
        Elif it's less than 0 → it's negative.
        Else → it must be zero.


7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
  Input : 8	Output : False
  Input : 25	Output : True

      Function Definition
        def div(number):
        This defines a function named div that takes one input argument, number.
      
        number % 5:
        The % operator returns the remainder when number is divided by 5.
        
        == 0:
        If the remainder is 0, it means the number is evenly divisible by 5.
        
        return number % 5 == 0:
        This returns True if divisible by 5, else False.
      
        User Input
          print("Enter Number:")
          Displays a message to the user.
      
        input() waits for the user to type something and press Enter.
        That input is read as a string.
        
        int(input()) converts that string into an integer.
        
        no = int(input()) stores the integer value in the variable no.
      
      
        Function Call and Condition Check
      
        div(no) calls the div function with the number no as the argument.
        If the function returns True, it prints "True".
        Otherwise, it prints "False".

8. Write a program which accept number from user and print that number of “*” on screen.
   Input : 5	Output : *	*	*	*	*

       input() waits for the user to type something and press Enter.
        It always returns a string, like "5".
        int(...) converts that string into an integer — now Python can do math with it.
        The result is stored in the variable no.
    
        range(no) creates a sequence of numbers from 0 to no - 1.
    
        For example: range(5) → 0, 1, 2, 3, 4 (5 numbers).
        The loop will run once for each number in that range.
        The variable i takes on each value one by one, but in this case you don’t use i in the loop — it's just for counting.
    
       print("*") would normally print * and then go to a new line.
       But end=" " changes that behavior — it tells Python to stay on the same line and print two spaces after the *.
    
       If no = 5, the loop prints * * * * * (on a single line).

9. Write a program which display first 10 even numbers on screen.
   Output : 2	4	6	8	10	12	14	16	18	20

       range(1, 11)
       This generates numbers from 1 to 10 (inclusive).
       So the loop runs 10 times with i taking values: 1, 2, 3, ..., 10.
          
       i * 2
       Each number i is multiplied by 2 to get an even number.
       The first 10 even numbers are:
      
        print(..., end=" ")
        Prints all numbers on the same line, separated by two spaces.
        Without end=" ", Python would print each number on a new line.

  
10. Write a program which accept name from user and display length of its name. 
      Input : Marvellous	Output : 10

        name = input()
          Waits for the user to type something and press Enter.
          Whatever the user types is saved as a string in the variable name.
        
        length = len(name)
          len() is a built-in Python function that returns the length of a string (i.e., the number of characters).
          It counts all characters, including spaces.
        
        print("Length of your name is:", length)
          Displays the result to the user by printing:
        
        if __name__ == "__main__":
          This ensures that main() only runs if this file is executed directly, and not if it's imported in another program.
      
  
    

  

  





