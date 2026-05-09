def ggd(a, b):
    if b == 0:
        return a
    return ggd(b, a % b)

print(ggd(1238214,364))