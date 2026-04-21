import math

def f(x):
    return -((x-2)**2)+4

def riemann_midden(a, b, n):
    dx = (b - a) / n
    totale_oppervlakte = 0
    
    for i in range(n):
        # middelpunt van de rechthoek
        x_midden = a + ((i + 0.5) * dx)
        
        # hoogte van de rechthoek
        hoogte = f(x_midden)
        
        # oppervlakte optellen
        totale_oppervlakte += hoogte * dx
    
    return totale_oppervlakte


# waarden instellen
a = 0
b = 4
n = 0.0001

teller = 1
r = 0
while True:
    vorige = r
    r = riemann_midden(a, b, teller)
    if teller != 1 and vorige - r < n:
        break
    print(f'{teller} rechthoek{'' if teller == 1 else "en"}: {r} ({round(abs(r-vorige),6)})')
    teller += 1
