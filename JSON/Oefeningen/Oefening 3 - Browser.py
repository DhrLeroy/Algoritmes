from collections import deque
import json

geschiedenis = deque()

with open("JSON/Oefeningen/browser.json", "r") as file:
    lijst = json.load(file)
    geschiedenis = deque(lijst)

laatste = geschiedenis[len(geschiedenis)-1]
print(laatste)

keuze = input("Wil je de laatst bezochte website verwijderen? ")

if keuze == "ja":
    geschiedenis.pop()
elif keuze == "nee":
    website = input("Nieuwe website: ")
    geschiedenis.append(website)


with open("JSON/Oefeningen/browser.json", "w") as bestand:
    lijst = list(geschiedenis)
    json.dump(lijst,bestand)