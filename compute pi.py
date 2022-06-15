# importing required libraries 
import random as rm
import math as mt
# generate random coordinate
total_number = 10000
random_coords = [(rm.random(), rm.random()) for _ in range(total_number)]
in_circle = 0
total_point = 0
for i in range(len(random_coords)):
    x = random_coords[i][0]
    y = random_coords[i][1]
    d = mt.sqrt(x ** 2 + y ** 2)
    total_point += 1
    if d < 1:
        # print("Inside circle")
        in_circle += 1
        # if total_point % 1000 == 0:
        # pi_calc = 4 * in_circle / total_point
    
pi_calc = 4 * in_circle / total_point
pi_lib = mt.pi
diff = pi_lib - pi_calc
print("Calculated value of π:", pi_calc)
print("Value of π from math library:", pi_lib)
print("Difference", pi_calc - mt.pi)
