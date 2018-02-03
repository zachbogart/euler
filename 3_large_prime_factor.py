'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def find_largest_prime_factor(num):
    """Find largest prime factor of num

    Keyword arguments:
    num -- number to test
    """

    largest_prime_factor = 0
    # special case: divide by two as much as you can
    while num % 2 == 0:
        num /= 2
        largest_prime_factor = 2
    div = 3
    # divide till there is no number left
    while div <= num:
        if num % div == 0:
            num /= div
            largest_prime_factor = div
        div += 2

    return largest_prime_factor

# testing
print("Largest Prime Factor of {}:\n{}".format(13195, find_largest_prime_factor(13195)))
print("Largest Prime Factor of {}:\n{}".
      format(600851475143, find_largest_prime_factor(600851475143)))
