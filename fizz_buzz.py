"""
Super cool fizz buzz

FizzBuzz: In range 1-100, every number divisible by 3 = Fizz,
every number divisible by 5 = Buzz, and every number divisible by both 3 and 5 = FizzBuzz.

Yeah, I know I can do something like this:
print("\n".join("Fizz" * (i%3==0) + "Buzz" * (i%5==0) or str(i) for i in range(1,101)))
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)