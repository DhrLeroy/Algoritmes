from collections import deque
import json

queue = deque()

with open("JSON/Oefeningen/todo.json", "r") as file:
    lijst = json.load(file)
    queue = deque(lijst)

keuze = input("Wil je een taak toevoegen of uitvoeren?")

if keuze == "toevoegen":
    taak = input("Taak: ")
    queue.append(taak)
elif keuze == "uitvoeren":
    taak = queue.popleft()
    print(f'{taak} wordt uitgevoerd')

with open("JSON/Oefeningen/todo.json", "w") as bestand:
    lijst = list(queue)
    json.dump(lijst,bestand)