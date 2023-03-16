# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:14:14 2023

@author: Inese
"""

# 1)Ask the user to enter the text and a letter. Count how many occurrences of the 
# letter provided. 

def Count_letter():
    text  = input("Please your text: ")
    letter = input("Please enter a letter: ")
    
    while len(letter) > 1 or letter.isalpha() == False:
        letter = input("Your input was invalid. Please enter a letter: ")
    
    count = 0
    for character in text:
        if character.lower() == letter.lower():
            count += 1
    
    print(f"The letter \"{letter}\" appears in your text {count} times.")
    


# 1.1) Based on the task 1, count the occurrences of each character in the text 
# provided and display them in the output
def Count_char():
    text  = input("Please your text: ").lower()
    char_list = set(text)
    
    for char in char_list:
         count = 0
         for character in text:
             if char.lower() == character.lower():
                count += 1 
         if count > 1:
             S_or_no_S = 's'
         else:
             S_or_no_S = '' 
         print(f"Charcter \"{char}\" appears in your text {count} time{ S_or_no_S}.")
     


# 2)Write the program to sort the list (without using sort function). 
# You can implement any algorithm
def Sorting(my_list):
    
   # define function to see if the list is ordered
    def order(my_list):
        ordered = []
        # check if elements that are next to each other are sorted. Make a list of True/False if they are/are not
        for a in my_list[:-1]:
            index = my_list.index(a)
            if index < len(my_list)-1 and (str(my_list[index]) < str(my_list[index+1])):
                ordered.append(True)
            else:
                ordered.append(False)
        # check if all are True, then the lsit is ordered --> assign Ordered = True
        if len(set(ordered)) == 1 and set(ordered).pop() == True:
               Ordered = True
        else:
               Ordered = False
        return Ordered
        
    Ordered = False
    
    # compare elements next to each other, swap them if they are not in order
    while Ordered == False:   
        for a in my_list:
            index = my_list.index(a)
            if index<len(my_list)-1 and (str(my_list[index]) > str(my_list[index+1])):
                    my_list[index] = my_list[index+1]
                    my_list[index+1] = a
                    Ordered = order(my_list)  
    print(my_list)
    
    
    
my_list = ['Zorro', 'clean', 'Apple', 'apple', 1, 222, 3]
Sorting(my_list)
