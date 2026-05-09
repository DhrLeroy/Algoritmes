import json

punten = {}

with open("JSON/Oefeningen/punten.json", "r") as file:
    punten = json.load(file)

keuze = input("Wat wil je doen? (vak toevoegen, punten van vak zien, punt toevoegen) ")

if keuze == "Vak toevoegen":
    vak = input("Vak: ")
    punten[vak] = []
elif keuze == "Punten van vak zien":
    vak = input("Vak: ")
    print(f'Punten: {punten[vak]}')
    gemiddelde = 0
    for punt in punten[vak]:
        gemiddelde = gemiddelde + punt
    gemiddelde = gemiddelde / len(punten[vak])
    print(f'Gemiddelde: {gemiddelde}/10')
elif keuze == "Punt toevoegen":
    vak = input("Vak: ")
    punt = float(input("Punt (op 10): "))
    punten[vak].append(punt)

with open("JSON/Oefeningen/punten.json", "w") as bestand:
    json.dump(punten,bestand)