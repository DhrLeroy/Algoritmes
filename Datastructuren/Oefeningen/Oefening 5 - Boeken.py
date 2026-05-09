boeken = []

while True:
    boek = input("Boek: ")
    if boek == "ingevuld":
        break
    boeken.append(boek)

boek = input("6 |	Welk boek werd er verkocht? ")

boeken.remove(boek)

print(f'Overige boeken: {boeken}')