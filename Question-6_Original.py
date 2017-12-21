"""
QUESTION:

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

"""
Formula:

sum of squares=n*(n+1)(2n+1)/6
square of sum=(n*(n+1)/2)^2
"""

n=int(input('Enter the number of natural numbers: '))
square_of_sum=((n*(n+1))/2)**2
print(square_of_sum)
sum_of_square=(n*(n+1)*(2*n+1))/6
print(square_of_sum-sum_of_square)