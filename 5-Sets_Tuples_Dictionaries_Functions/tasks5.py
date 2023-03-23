# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:01:06 2023

@author: Inese
"""
import re
from typing import List,  Dict

# Task 1: Write a function that takes two parameters (a and b) and returns their sum.

def Sum_ab(a,b: float):
    return sum((a,b))

print(Sum_ab(4,35))

# Task 2:Write a function that takes a string as a parameter and returns the 
# number of vowels (aeiou) in the string. Hint: you can use given_character in "aeiou"

def Vowel_count(text: str):
    vowel_search = re.findall("[aeiou]", text)
    return len(vowel_search)

print(Vowel_count("Mozart"))


# Task 3:Write a function that takes a string as a parameter and returns True if the 
#  string is a palindrome and False otherwise
def Palindrome(text: str):
    half_text_length = len(text)//2
 
    # Compare opposite end characters
    for i in range(0,half_text_length):
            if text[i] != text[-(i+1)]:
                palindrome = False
            else: 
                palindrome = True
        
    return palindrome
          
print(Palindrome("AbbA"))

# Task 4:Write a function that takes a list of integers as a parameter and 
#  returns a list of only the even integers in the original list

def Even_numbers(integers: List[int]):
    even_numbers = []
    for integer in integers:
        if integer % 2 == 0:
            even_numbers.append(integer)
    
    return even_numbers

print(Even_numbers([1,2,34,321,56,6,-66,7,229,8,5,5,4,33,2,0,3]))

# Task 5:Write a function that takes a list of integers and a target sum as 
# parameters and returns a list of two integers from the original list that add 
# up to the target sum.

def Sum_numbers(integers: List[int], target_sum :int):
    output = []
    for i in integers:
        if target_sum - i in integers:
            output = [i, target_sum-i]
            break
    return output

print(Sum_numbers([1,-2,5,6,7,12,8,4,3],11))

        
# Task 6: Write a function that takes a list of integers as a parameter and 
# returns the product of all the integers in the list.

def Product(*args: int):
    product = 1
    for arg in args:
        product = product * arg
    return product

print(Product(1,2,3,4))

# Task 8:Write a function that takes a dictionary as a parameter and returns a 
# list of all the keys in the dictionary that have an even value.

def Keys_even(**kwargs):
    keys = []
    for key in kwargs:
        if kwargs.get(key) % 2 == 0:
            keys.append(key)
    return keys


print(Keys_even(arg3=3, arg2=2, arg1=5))

# Task 9:Write a function that takes a list of dictionaries as a parameter and
# returns a new dictionary that contains the sum of the values for each key in 
# the original dictionaries.

def Sum_keys_d(dictionaries: List[Dict[object,float]]):
    sum_values = {}
    for dictionary in dictionaries:
        for key in dictionary:
            key_value = dictionary.get(key)#get the value, based on the key for the dictionary
            if key not in sum_values:
                sum_values[key] = key_value
            else:
                sum_values[key] = sum_values.get(key) + key_value
    return sum_values

my_list = [
    {"apple": 1.0, "banana": 2.5, "orange": 3.75},
    {"apple": 2.5, "banana": 1.25, "orange": 5.0}
]

print(Sum_keys_d(my_list))                    
            
        
# Task 10:Write a function that takes a tuple as a parameter and returns a new 
# tuple that has the first and last elements swapped.

def Swap_tuple(my_tuple: tuple):
    new_tuple = list(my_tuple)
    new_tuple[0], new_tuple[-1] = new_tuple[-1], new_tuple[0]
 
    return tuple(new_tuple)

print(Swap_tuple((2,3,4,5,9)))

# Task 11:Write a function that takes a set as a parameter and returns a new 
# set that contains only the elements that are not divisible by 3.

def Set3(your_set: set):
    your_set = set(filter(lambda x: x % 3 != 0, your_set))
    return your_set

print(Set3({3,5,6,7,1,2,44,43,32,42}))
            