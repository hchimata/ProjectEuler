#!Python3
"""
Euler Question - 1
list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_multiples_of_3_and_5(multiple_limit_val):
    max_multiple_of_3 = int((multiple_limit_val-1)/3)
    max_multiple_of_5 = int((multiple_limit_val-1)/5)
    max_multiple_of_15 = int((multiple_limit_val-1)/15)
    print(" ", max_multiple_of_3, "  ", max_multiple_of_5, " ", max_multiple_of_15)
    sum_of_multiple_of_3_5 = int(
        3*max_multiple_of_3*(max_multiple_of_3 + 1)
        + 5*max_multiple_of_5*(max_multiple_of_5 + 1)
        - 15*max_multiple_of_15*(max_multiple_of_15 + 1))/2
    return sum_of_multiple_of_3_5

if __name__ == "__main__":
    multiple_limit = int(input("Enter the limit: "))
    sum_value = get_multiples_of_3_and_5(multiple_limit)
    print("Sum of all the multiples of 3 or 5 below ", multiple_limit, " is : ", sum_value)
