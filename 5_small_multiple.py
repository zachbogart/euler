'''
Smallest multiple
Problem 5 

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import numpy as np

def small_multiple():
    x = np.arange(20,1,-1)
    smallest_mult = 1
    while True:
        # print("On: ", smallest_mult)
        valid = True
        for num in x:
            if smallest_mult % num != 0:
                valid = False
                break
        if valid:
            return smallest_mult
            
        smallest_mult += 1
    
print(small_multiple())