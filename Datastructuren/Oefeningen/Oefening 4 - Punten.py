import json

punten = {}

with open("punten.json", "r") as f:
    punten = json.load(f)

while(True):
    vak = input("Vak: ")
    if vak == "ingevuld":
        break
    punten[vak] = []

while(True):
    vak = input("Vak: ")
    if vak == "stop":
        break
    punt = float(input("Behaald: "))
    totaal = float(input("Totaal: "))
    percentage = punt/totaal*100
    punten[vak].append(percentage)

with open("punten.json", "w") as f:
    json.dump(punten,f)