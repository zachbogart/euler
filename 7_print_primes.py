# -*- coding: utf-8 -*-
'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def prime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True

def print_primes(nth_prime):
    count = 0
    i = 2
    while count != nth_prime:
        if prime(i):
            count += 1
        i += 1
    return i - 1
            
print("{}th prime: {}". format(6, print_primes(6)))
print("{}st prime: {}". format(10001, print_primes(10001)))