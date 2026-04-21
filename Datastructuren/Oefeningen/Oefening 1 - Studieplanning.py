from collections import deque

taken = deque()

while True:
    taak = input("Taak: ")
    if taak == "stop":
        break
    taken.append(taak)

while len(taken) > 0:
    volgende_taak = taken.popleft()
    print(f'Begin nu aan {volgende_taak}')
    input()

