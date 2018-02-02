# -*- coding: utf-8 -*-
'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def find_largest_palindrome(lo, hi):
    if lo < 0 or hi < 0:
        print("Usage: positive arguments only")
    
    largest = -1
    for i in range(lo,hi):
        for j in range(lo,hi):
            candidate = i * j 
            left = 0
            right = len(str(candidate)) - 1
            valid = True
            while right > left and valid:
                if str(candidate)[left] == str(candidate)[right]:
                    left += 1
                    right -= 1
                else:
                    valid = False
            if valid and candidate > largest:
                largest = candidate
    return largest
            
print("Largest found: {}".format(find_largest_palindrome(100, 1000)))