# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:58:06 2023

@author: Inese
"""

# 1.Create a program that asks the user to enter their age and whether or not they have a driver's license. 
# If the user is at least 18 years old and has a driver's license, the output should be as follows
# "You are able to drive : True
# If not, then
# "You are able to drive : False
def AbilityToDrive():
    age = input("1. What is your age?")
    has_drivers_license=input("2. Do you have a drivers license?")                                
    
    age = int(age)
    has_drivers_license = has_drivers_license.lower()
    
    can_drive = (age >= 18) and (has_drivers_license == "yes")
    
    return print(f"You are able to drive : {can_drive}")

AbilityToDrive() 


# 2. (Explore some String functions).Create a program that asks the user for a password, 
# and checks if it meets the following criteria: at least 8 characters long,
#  contains at least one uppercase letter, one lowercase letter, and one number. 
def Password_Criteria():
    password = input("Please enter your password. It must contain at least 8 characters long, at least one uppercase letter, one lowercase letter, and one number ")
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = lowercase_letters.upper()
    numbers='1234567890'
    password_passes_criteria = (len(password) >= 8) and bool(set(lowercase_letters) & set(password)) and bool(set(uppercase_letters) & set(password)) and bool(set(numbers) & set(password))
    
    return print(f"Password accepted : {password_passes_criteria}")
   
Password_Criteria()

# 3. Write a program that asks the user to enter two integers and checks if they are 
#both even. 
# If they are, print "Both numbers are even : True", otherwise print "Both numbers 
#are even : False".
# If at least one is even print "At least one number is even : True", else "At least 
#one number is even : False".

# Hint : use modulo operator % here
def Even_Numbers():
    integer1,integer2 = input("Enter 2 integers").split()
    integer1, integer2 = int(integer1), int(integer2)
    botheven = (integer1 % 2 == 0) and (integer2 % 2 == 0)
    oneeven = (integer1 % 2 == 0) or (integer2 % 2 == 0)
    print (f"Both numbers are even : {botheven}")
    print (f"At least one number is even : {oneeven}")

Even_Numbers()

# 4. Write a program that asks the user to enter a year and checks if it is a leap year. 
# A leap year is defined as a year that is divisible by 4 but not by 100, or a year that is 
# divisible by 400. 
# If the year is a leap year, print "Leap year : True", otherwise print "Leap year : True".
def Leap_Year():
    year = input("Enter year")
    year = int(year)
    isleapyear = ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)
    return print (f"Leap year : {isleapyear}")

Leap_Year()

def Valid_Year():
    day,month,year = input("Enter day, month, year").split()
    day, month, year = int(day), int(month), int(year)
    month_valid = (month <= 12 and month > 0)
    year_valid  = (year > 0)
    longmonth_valid = ((month in (1,3,5,7,8,10,12)) and ((day <= 31) and (day > 0)))
    shortmonth_valid = ((month in (4,6,9,11)) and ((day <= 30) and (day > 0)))
    long_year = ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)
    long_feb_valid = (month == 2) and (day <= 29) and (day > 0) and long_year
    short_feb_valid = (month == 2) and (day <= 28) and (day > 0) and not long_year
    valid_date =  month_valid and year_valid and (longmonth_valid or shortmonth_valid or long_feb_valid or short_feb_valid)
    return print (f"Date valid : {valid_date}")

Valid_Year()