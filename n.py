

#Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of x+y+z is not equal to . 
# Here, . Please use list comprehensions rather than multiple loops, as a learning
#a, b, c, n = [int(input()) for _ in range(4)]
#rint ([[x,y,z] for x in range(a + 1) for y in range(b + 1)  for z in range(c + 1) if x + y + z != n])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = []
    for i in range(n):
        if i not in arr:
            a.append(i)
    
    print ("The list after removing duplicates : " + str(a))

### Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

d={} #1
for _ in range(int(input())): #2
    Name=input() #3
    Grade=float(input()) #4
    d[Name]=Grade #5
v=d.values()#6
second=sorted(list(set(v)))[1] #7
second_lowest=[] #8
for key,value in d.items():  #9
    if value==second: #10
        second_lowest.append(key) #11
second_lowest.sort() #12
for name in second_lowest: #13
    print(name) #14
    

"""
@1) Empty dictionary.

@2) Range for number of students.

@3) Accepting name of the student.

@4) Accepting the grade of the student.

@5) Assigning name as key and grade as value for the dictionary.

@6) Obtaining the values of dictionary(all grades of students.

@7) Remoing duplicte grades by using set data type , changing it to list, sorting in ascending order and taking the second lowest grade.

@8) Declaring an empty list for storing the name of the students who got the second lowest grade.

@9) Going through the name and grade of each students by using items() method of dictionary.

@10) Checking whether the grade is equal to the second lowest grade.

@11) If yes , append it to the second_lowest list.

@12) bSorting the name of students in asceding order

@13) Going through the name of each students who got the second lowes grade.

@14) Printing each name of students in seperate line
"""
"""
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. For each  queried, 
print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for  is not found, print Not found instead.
"""
n = int(input())
phonebook = {}

for i in range(n):
    line = input()
    pair = line.split()
    phonebook[pair[0]] = pair[1]

while True:
    try:
        name = input()
    except EOFError as e:
        break
    if name not in phonebook.keys():
        print("Not found")
    else:
        print(f"{name}={phonebook[name]}")

###Maxiimum hour glass sum in 2D arrays

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    sum = 0

    tarr = []
    
    for l in range(0,4):
        for k in range(0,4):
            for i in range(l,l+3):
                for j in range(k,k+3):
                    if i == l+1 and ( j == k or j == k+2):
                        continue
                    else:
                        sum += arr[i][j]
            tarr.append(sum)
            sum = 0
    
    print(max(tarr))
#You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
# Completed code for Person and a declaration for Student are provided for you in the editor. 
# Observe that Student inherits all the properties of Person.

class Person:
    def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg>= 90 and avg <=100:
            return 'O'
        elif avg>=80 and avg<90:
            return 'E'
        elif avg>=70 and avg <80:
            return 'A'
        elif avg>=55 and avg<70:
                return 'P'
        elif avg>=40 and avg<55:
            return 'D'
        elif avg<40:
            return 'T'
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())