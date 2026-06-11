from collections import deque
import json

zetten = deque()

with open("Datastructuren/Oefeningen/data_e3.json", "r") as file:
    lijst = json.load(file)
    zetten = deque(lijst)

zet = input("Zet: ")
if zet == "Schaakmat":
    vorige_zet = zetten.pop()
    while vorige_zet != "Checkpoint":
        print(f"Maak ongedaan: {vorige_zet}")
        vorige_zet = zetten.pop()
    zetten.append("Checkpoint")
else:
    zetten.append(zet)

with open("Datastructuren/Oefeningen/data_e3.json", "w") as bestand:
    lijst = list(zetten)
    json.dump(lijst,bestand)