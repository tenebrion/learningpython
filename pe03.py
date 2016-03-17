"""
Largest Prime Factor

What is the largest prime factor of the number 600851475143?
"""
large_prime = 600851475143
i = 2
while i * i < large_prime:
    while large_prime % i == 0:
        large_prime = large_prime / i
    i = i + 1
print(large_prime)