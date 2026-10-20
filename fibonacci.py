def fibonacci(n):
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")

    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a=b
        b = a + b