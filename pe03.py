"""
Largest Prime Factor

What is the largest prime factor of the number 600851475143?
"""


def find_prime():
    """
    This is problem 3 on Project Euler
    :return:
    """
    large_prime = 600851475143
    i = 2
    while i * i < large_prime:
        while large_prime % i == 0:
            large_prime = large_prime / i
        i += 1
    return large_prime

print(find_prime())
