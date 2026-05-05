faculteit_4 = 4 * 3 * 2 * 1

faculteit_7 = 7*6*5*4*3*2*1

def faculteit(n):
    if n == 1:
        print("!1 = 1")
        return 1
    print(f"begin berekenen !{n} = {n} x !{n-1}")
    facul = n * faculteit(n-1)
    print(f"eind berekenen !{n} = {n} x !{n-1}")
    return facul

print(faculteit(4))