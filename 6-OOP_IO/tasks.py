# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:27:20 2023

@author: Inese
"""

# OOP :
# 1.Create a class named Car that has the following attributes: make, model, and year. 
# It should also have a method called get_info() that returns a string with the car's make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return print (f"The make is  {self.make}, the model is {self.model}, the year is {self.year}")
    
mycar = Car("Nissan", "Alexa", 2016)
Car.get_info(mycar)
        


# 2.Create a class named Rectangle that has the following attributes: width and height. 
# It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, 
#respectively.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        self.area = self.width * self.height
        return self.area
    
    def perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
        
myshape = Rectangle(23, 11)
print (f"The area {Rectangle.area(myshape)}. The perimeter is {Rectangle.perimeter(myshape)}.")
        

# 3,Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
# It should also have methods called deposit() and withdraw() that update the balance accordingly.

class BankAccount:
    def __init__(self, account_number:int, balance:float, owner_name:str):
        self.account_number = account_number
        self.balance = round(balance,2)
        self.owner_name = owner_name
        
    def deposit(self, deposit:float):
        self.balance = self.balance + deposit
        
    def withdraw(self, withdraw:float):
        self.balance = self.balance - withdraw
        
myaccount = BankAccount(123455, 11.22, "Susan Smith")
myaccount.deposit(34.11)
myaccount.withdraw(100.00)
print (f"The client now has {myaccount.balance} Euros on their account")

# 4.Create a class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address.

class Person:
    def __init__(self, name:str, age: int, address:str):
        self.name = name
        self.age = age
        self.address = address
    
    def get_info(self):
        print(f"The name is {self.name}, age is {self.age}, the address is {self.address}")

myperson = Person("Peppe", 21, "Unicorn land 3")
Person.get_info(myperson)


# 5.Create a class named Animal that has the following attributes: name and species. 
# It should also have a method called speak() that returns a string with the animal's sound.


class Animal:
    def __init__(self, name, species):
        self.name = name.lower()
        self.species = species
    
    def sound(self):
        animal_sounds = {
           "dog": "woof",
            "horse": "neigh",
            "goat": "baa",
            "sheep": "baa",
            "pig": "oink",
            "cow": "moo",
            "donkey": "hee haw",
            "chicken": "cluck",
            "rooster": "cock-a-doodle-do",
            "bird": "chirp",
            "owl": "hoot",
            "duck": "quack",
            "goose": "honk",
            "turkey": "gobble",
            "mosquito": "buzz",
            "cricket": "chirp",
            "frog": "ribbit",
            "lion": "roar"}

        if self.name  in animal_sounds:
            self.sound = animal_sounds[self.name]
        else:
            self.sound = "Not known"
            
        return self.sound
    
my_animal  = Animal("FROG", "mini frog")
print(f"{my_animal.name} says {my_animal.sound()}")
            
# 6.Create a base class named Vehicle that has the following attributes: 
    # make, model, and year. It should also have a method called get_info() that returns 
    # a string with the vehicle's make, model, and year. Then create two subclasses, Car and Truck, 
    # that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle.
    
class Vehicle:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return print (f"The make is  {self.make}, the model is {self.model}, the year is {self.year}")
    
    
class Car(Vehicle):
    def __init__(self, make, model, year: int, color: str):
       super().__init__(make, model, year)
       self.color = color
    def get_car_info(self):
        return print (f"The make is  {self.make}, the model is {self.model}, the year is {self.year}, the color is {self.color}")
    
class Truck(Vehicle):
    def __init__(self,  make, model, year: int, wheels: int):
        super().__init__(make, model, year)
        self.wheels = wheels
    def get_truck_info(self):
        return print (f"The make is  {self.make}, the model is {self.model}, the year is {self.year}, the nr of wheels is {self.wheels}")
        
       
     
mycar = Car("Nissan", "Alexa", 2016, "blue")
Car.get_car_info(mycar)   
    

# 7.Create a base class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address. 
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and 
# methods specific to each role.

class Student(Person):
    def __init__(self, name:str, age: int, address:str, grade):
        super().__init__(name, age, address)
        self.grade = grade
        
    def new_grades(self, *args):
        self.grade = (self.grade +sum(args))/(len(args)+1)
        return self.grade
    
mystudent = Student("Peppe", 21, "Unicorn land 3", 5)
mystudent.new_grades(2,3,4,6,7,8,9,10, 10, 10, 10 , 10, 10 )
print(f"{mystudent.name} has an average grade of {mystudent.grade}")

class Teacher(Person):
    def __init__(self, name:str, age: int, address:str, subject: str):
        super().__init__(name, age, address)
        self.subject = subject.lower()
        
    def classification_subject(self):
        natural_sciences = ["physics","biogy","chemistry","geology"]
        if self.subject in natural_sciences:
            print(f"{self.name} is a natural sciences teacher")
        else:
            print(f"{self.name} is not a natural sciences teacher")

myteacher= Teacher("Peppe", 21, "Unicorn land 3", "CHEMISTRY")
myteacher.classification_subject()


# For I/O:
# 8.Write a Python program that reads a JSON file containing a list of dictionaries, 
# sorts the list by a specific key, and writes the sorted list back to the file.
import json

with open("persons.json", "r") as f:
    people_list = json.load(f)

sorted_list = sorted(people_list, key=lambda x: x['age'])

with open("persons.json", "w") as f:
    json.dump(sorted_list, f)


# 9.Write a Python program that reads a CSV file containing student grades, calculates
# their average score, and writes the average to a new file.

import csv

with open("students.csv", "r") as f:
    people = csv.reader(f, delimiter=',')
    totalgrades = 0
    count = 0
    for row in people:
        if row[2].isnumeric():
            totalgrades = totalgrades + float(row[2])
            count = count + 1
    average = totalgrades/count
        
with open("average.json","w") as f:
    avrage_students = {"avereage_result_all_students" : average}
    json.dump(avrage_students,f)
    

# 10.Write a Python program that reads a CSV file containing student grades and writes a 
# new CSV file with the grades sorted by student name.

with open("students.csv", "r") as f:
    people = csv.reader(f, delimiter=',')
    next(people) # skip the header row
    dictionary_list = []
    for line in people:
        person = {"name":line[0],
                  "surname":line[1],
                  "grade":int(line[2])}
        dictionary_list.append(person)
        
    sorted_list = sorted(dictionary_list, key=lambda x: x['name'])   
    delim = ","
    filelines = list()
    filelines.append("First Name" + delim + "SurName" + delim + "Grade")#header line
    
    for entry in sorted_list:
            line = entry["name"] + delim + entry["surname"] + delim + str(entry["grade"])
            filelines.append("\n" + line)
            
with open("sorted_students.csv", "w") as f:
    f.writelines(filelines)
    