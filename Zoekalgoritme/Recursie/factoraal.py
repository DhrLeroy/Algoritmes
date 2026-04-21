def factoraal(n):
    print(f'Factoraal {n}')
    if n > 1:
        result = n * factoraal(n-1)
        print(result)
        return result
    elif n == 1:
        result = 1
        print(result)
        return result
    
factoraal(5)
