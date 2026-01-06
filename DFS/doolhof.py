visited = []
path = []
teller = 0

def DFS(rij,kolom):
    global teller
    # check of rij/kolom niet in doolhof ?
    if rij < 0 or rij > max_rij-1 or kolom < 0 or kolom > max_kolom-1:
        return False

    # check of rij/kolom B ?
    if doolhof[rij][kolom] == "B":
        return True

    # check of rij/kolom # ?
    if doolhof[rij][kolom] == "#":
        return False
    
    # check of rij/kolom al werd bezocht ?
    if (rij,kolom) in visited:
        return False
    
    visited.append((rij,kolom)) 
    doolhof[rij][kolom] = chr(teller+96)
    if teller > 25:
        teller = 0
    teller = teller + 1

    # links DFS
    links = DFS(rij,kolom-1)
    if links == True:
        return True
    # boven DFS
    boven = DFS(rij-1,kolom)
    if boven == True:
        return True
    # rechts DFS
    rechts = DFS(rij, kolom+1)
    if rechts == True:
        return True
    # onder DFS
    onder = DFS(rij+1, kolom)
    if onder == True:
        return True
    return False

def bekijkCel(rij,kolom):
    return doolhof[rij][kolom]

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

DFS(0,0)
print(visited)
toonDoolhof()