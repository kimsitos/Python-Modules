def fibonacci(index):
    a = 0
    b = 1
    i = 0
    while i <= index:
        yield a
        a, b = b, a + b
        i += 1

fib = fibonacci(27)

print("Fibonacci")
count = 0
for f in fib:
    if f % 2 == 0:
        print(f, end=' ')


print("\n\nPower cube")
powercube = iter([x * x for x in range (10)])
for x in range(10):
    print(next(powercube), end=' ')
