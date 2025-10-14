def bekijkCel(rij,kolom):
    print(doolhof[rij][kolom])

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

doolhof = maakDoolhof(20,20)

maakMuur(1,1)
maakMuur(2,4)
toonDoolhof()
maakMuur(3,6)
toonDoolhof()

