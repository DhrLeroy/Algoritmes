from collections import deque
import json

stack = deque()

with open("data.json", "r") as file:
    lijst = json.load(file)
    stack = deque(lijst)

stack.append("A")
stack.append("B")
stack.append("C")

with open("data.json", "w") as bestand:
    lijst = list(stack)
    json.dump(lijst,bestand)