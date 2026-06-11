from collections import deque
import json

vogels = {}

with open("Datastructuren/Oefeningen/data_e2.json", "r") as file:
    vogels = json.load(file)

keuze = input("Wat wil je doen (nieuwe soort = a, waarneming registreren = b, waarnemingen zien = c)? ")

if keuze == "a":
    vogel = input("Vogelsoort: ")
    vogels[vogel] = 1
elif keuze == "b":
    vogel = input("Vogelsoort: ")
    vogels[vogel] = vogels[vogel] + 1
elif keuze == "c":
    vogel = input("Vogelsoort: ")
    print(f'De {vogel} werd {vogels[vogel]} keer gespot!')

with open("Datastructuren/Oefeningen/data_e2.json", "w") as bestand:
    json.dump(vogels,bestand)