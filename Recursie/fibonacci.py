def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"Begin fibonacci {n}")
        fibo = fibonacci(n-1) + fibonacci(n-2)
        print(f"Eind fibonacci {n}")
        return fibo

print(fibonacci(7))