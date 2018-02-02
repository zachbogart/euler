# Multiples of 3 and 5
# Problem 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_it_up(n):
    total = 0
    for val in range(n):
        if val % 3 == 0 or val % 5 == 0:
            total += val
    return total
            
print("Sum 3,5 multiples, n = 10: {}".format(sum_it_up(10)))
print("Sum 3,5 multiples, n = 1000: {}".format(sum_it_up(1000)))