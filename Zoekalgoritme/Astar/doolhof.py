visited = []
open = []


def Astar():
    huidige = (0,0)
    open.append(huidige)

    while len(open) > 0:
        laagste_kosten = []
        laagste_kost = 999999
        

def maakMuur(rij,kolom):
    doolhof[rij][kolom] = "#"

def toonDoolhof():
    for rij in doolhof:
        lijn = ""
        for cel in rij:
            lijn = f'{lijn}|{cel}'
        lijn = f'{lijn}|'
        print(lijn)

def maakDoolhof(rijen,kolommen):
    return [[' ']*rijen for kolom in range(kolommen)]

max_rij = 8
max_kolom = 8

doolhof = maakDoolhof(max_rij,max_kolom)

doolhof[0][0]="A"
open.append((0,0))

doolhof[7][7]="B"
maakMuur(1,0)
maakMuur(1,1)
maakMuur(1,2)
maakMuur(1,4)
maakMuur(1,5)
maakMuur(1,6)
maakMuur(2,6)
maakMuur(3,6)
maakMuur(4,6)
maakMuur(3,1)
maakMuur(3,2)
maakMuur(4,1)
maakMuur(5,1)
maakMuur(6,1)
maakMuur(7,1)
maakMuur(5,4)
maakMuur(5,5)
maakMuur(5,6)
maakMuur(5,7)
maakMuur(6,4)
maakMuur(7,6)
toonDoolhof()

Astar()
print(visited)
toonDoolhof()