from collections import deque

vervaldata = deque()

while True:
    vervaldatum = input("Vervaldatum: ")
    if vervaldatum == "aangevuld":
        break
    vervaldata.append(vervaldatum)

input()

vervaldatum = vervaldata.pop()
print(f'Dit product vervalt op {vervaldatum}')