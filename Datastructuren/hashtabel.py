prijslijst = {}

prijslijst["Frieten"] = 2.8
prijslijst["Bitterballen"] = 3.1
prijslijst["Cola"] = 1.6

product = input("Product: ")

print(hash(product))

print(prijslijst[product])


# prijzenlijst = []
# prijzenlijst[0] = 2.8
# prijzenlijst[1] = 3.1
# prijzenlijst[2] = 1.6


woordenboek = {}

woordenboek["Bank"] = ["Een gebouw vol geld", "Iets om op te zitten"]
woordenboek["Niezen"] = ["Hatsjoe"]
woordenboek["Huh"] = ["???"]
woordenboek["Aap"] = ["Een beest dat in bomen kan klimmen."]

woord = input("Geef een woord in: ")

betekenissen = woordenboek[woord]

for betekenis in betekenissen:
    print(f'{woord} betekent {betekenis}')