def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

count = 0
for f in fib:
    if count == 90:
        break
    print(f, end=', ')
    count += 1
