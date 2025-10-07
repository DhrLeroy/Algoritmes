'''hoogte = 8
breedte = 8

doolhof = [[' ' for x in range(breedte)] for y in range(hoogte)]

doolhof[7][0] = 'A'
doolhof[1][1] = '#'
doolhof[2][1] = '#'
doolhof[4][1] = '#'
doolhof[5][1] = '#'
doolhof[6][1] = '#'
doolhof[7][1] = '#'


for i in range(hoogte):
    rij = ''
    for j in range(breedte):
        rij += f'|{doolhof[i][j]}'
    print(rij+'|')
'''

rijen = 20
kolommen = 20

doolhof = [[' ']*rijen for kolom in range(kolommen)] 

doolhof[1][1]= '#'
doolhof[0][2]= 'A'

for rij in doolhof:
    lijn = ""
    for cel in rij:
        lijn = f'{lijn}|{cel}'
    lijn = f'{lijn}|'
    print(lijn)
    


























