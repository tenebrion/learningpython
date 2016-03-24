def fibonacci(n):
    # assigning x and y at the same time - clean look
    x, y = 0, 1
    values = [] # I wanted to print them in a 'list'
    for i in range(n):
        values.append(x)
        x, y = y, x + y
    return values

print(fibonacci(10))