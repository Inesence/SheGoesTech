# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:17:20 2023

@author: Inese
"""

# 1)Write a program that takes a user input (an integer) 
# and determines whether it is positive, negative, or zero

def Positive_Negative_Zero():
    number = int(input("Please enter an integer: "))
    
    if number == 0:
        print("Number is zero")
    elif number > 0:
        print("Number is positive")
    else: 
        print("Number is negative")


# Positive_Negative_Zero()


# 2)Write a program that prints out the numbers from 1 to 100. But for multiples of three, 
# print "Fizz" instead of the number and for multiples of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

def FizzBuzz():
    for number in range(1,101):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(f"{number}")

# FizzBuzz()

def Factors():
    # 3)Write a program that takes an integer as input and prints out all the 
    # factors of that integer.
    
    your_number = int(input("Please enter an integer: "))
    factors=[]
    while your_number != 1:
        for number in range(2,int(your_number)+1):
                if your_number % number == 0:
                    factors.append(number)
                    your_number = your_number / number
                    
    factors.sort()
    print(factors)
    

  
#Factors() 


#  4)Create calculator:
#   Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). 
#   If the operation 
#   provided does not match one of these, the program should print 
#   "Operation provided isn't valid, please,try again" - in this case, 
#   the program should
  # ask for the operation to be provided again 
def Calculator():
    
    number1 = float(input("Provide one number: "))
    number2 = float(input("Provide another number: "))
    operation = input("Provide  one operation to be performed (*,/,+.- or %): ")
    
    opearations = ["*","/","+","-", "%"]   
    
    while operation not in opearations:
        print("Operation provided isn't valid, please,try again")
        operation = input("Provide  one operation to be performed (*,/,+.- or %): ") 
    if operation  == "+":
        output = number1 + number2
    elif operation  == "-":
        output = number1 - number2
    elif operation  == "*":
        output = number1 * number2
    elif operation  == "/":
        output = number1 / number2
    elif operation  == "%":
        output = number1 % number2
    else:
        output = "Hmm..something went wrong and it is your fault :)"
    print(output) 
    
# Calculator()

# 5)Write a program that takes an integer as input and prints out whether that 
#     integer is prime or not.    
def Factors_for_Prime(your_number):

    factors=[]
    while your_number != 1:
        for number in range(2,int(your_number)+1):
                if your_number % number == 0:
                    factors.append(number)
                    your_number = your_number / number
                    
    factors.sort()
    
    return factors

def Prime_number():
   
    number = int(input("Provide one integer (with peace and love, if you don`t provide an integer, you`ll get an error): "))
    if  Factors_for_Prime(number)[0] == number:
        print("This is a prime number")
    else:
        print("This is not a prime number")
        
# Prime_number()