"""
This page is a 'for loop' lecture
"""

    
import numpy as np
import numpy.random as rd

# This loop runs from 0 to n-1
n = 5
for i in range(n):
    print(f"i = {i}")

# This loop runs from 1 to n-1
for k in range(1, 5):
    print(f"k = {k}")

# Two lists defined below
Sohan_classmates = ['Sohan', 'Nihal', 'Daniel', 'Samson', 'Ujantari', 'Harsha'] 
Sohan_classmates_rollnos = [23, 67, 12, 98, 72, 51]

# Using zip() function to call two lists at the same time
for student, roll_call in zip(Sohan_classmates, Sohan_classmates_rollnos):
    print(f"{student} passed the exam with distinction" )
    print(f"His roll number is: {roll_call}\n" )
    
# Generating an array of random numbers
rand_numbers = np.round(rd.rand(6)*10, 1)

# Using enumerate() function to iterate through values as well
# as indices at the same time and we can decide the start of the 
# index by defining the 'start' in the enumerate function
for i, rn in enumerate(rand_numbers, start=1):
    print(f"index = {i} and random number = {rn}")
    
    

  
    
   
    
   
    
   
    
   
    
   
    
   
    