# -*- coding: utf-8 -*-
'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_diff(num):
    sum_squares = 0
    square_sum = 0
    for i in range(1,num+1):
        sum_squares += i * i
        square_sum += i
    square_sum *= square_sum
    
    diff = square_sum - sum_squares
    
    return diff

print("Sum of Squares Difference: {}".format(sum_square_diff(100)))