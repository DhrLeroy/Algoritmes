visited = []

def DFS(rij,kolom, teller):
    
    # check of rij/kolom niet in doolhof ?
    if rij < 0 or rij > max_rij-1 or kolom < 0 or kolom > max_kolom-1:
        return False

    # check of rij/kolom B ?
    if doolhof[rij][kolom] == "B":
        str = ""
        for coordinaat in visited:
            str = str + f', {coordinaat}'
        print(str)
        return True

    # check of rij/kolom # ?
    if doolhof[rij][kolom] == "#":
        return False
    
    # check of rij/kolom al werd bezocht ?
    if (rij,kolom) in visited:
        return False
    
    visited.append((rij,kolom)) 

    doolhof[rij][kolom] = teller
    teller = teller + 1

    # links DFS
    links = DFS(rij,kolom-1,teller)
    if links == True:
        return True
    # boven DFS
    boven = DFS(rij-1,kolom, teller)
    if boven == True:
        return True
    # rechts DFS
    rechts = DFS(rij, kolom+1, teller)
    if rechts == True:
        return True
    # onder DFS
    onder = DFS(rij+1, kolom, teller)
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

max_rij = 5
max_kolom = 5

doolhof = maakDoolhof(max_rij,max_kolom)

doolhof[0][0]="A"

doolhof[4][4]="B"
maakMuur(1,0)
maakMuur(1,1)
maakMuur(1,2)
maakMuur(3,0)
maakMuur(3,1)
maakMuur(3,3)
maakMuur(3,2)
toonDoolhof()

DFS(0,0, 1)

visited

