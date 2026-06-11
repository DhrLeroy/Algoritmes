from collections import deque
import json

queue = deque()

with open("Datastructuren/Oefeningen/data_e1.json", "r") as file:
    lijst = json.load(file)
    queue = deque(lijst)

keuze = input("Wat wil je doen (studeren / plannen)? ")

if keuze == "plannen":
    taak = input("Studieblok: ")
    queue.append(taak)
elif keuze == "studeren":
    taak = queue.popleft()
    print(f'Studeer nu {taak}')

with open("Datastructuren/Oefeningen/data_e1.json", "w") as bestand:
    lijst = list(queue)
    json.dump(lijst,bestand)