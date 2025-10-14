def DFS(rij,kolom):
    

    check of rij/kolom in doolhof ?

    check of rij/kolom B ?

    check of rij/kolom # ?

    links DFS
    boven DFS
    rechts DFS
    onder DFS

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

max_rij = 20
max_kolom = 20

doolhof = maakDoolhof(max_rij,max_kolom)

doolhof[0][0]="A"

doolhof[4][5]="B"

maakMuur(1,1)
maakMuur(2,4)
maakMuur(3,6)
toonDoolhof()

DFS(0,0)

