import math

def factorial():
    number = int(input("Please enter a number: ")) # Prompts user to enter a number
    factoredNumber = math.factorial(number) # Factors the number the user entered
    print(factoredNumber) # Displays the answer
    
factorial()