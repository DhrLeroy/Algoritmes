from collections import deque

stapel = deque()

stapel.append("Klaver 4")
stapel.append("Harten 2")
stapel.append("Harten Heer")
stapel.append("Schoppen As")

print(stapel)

bovenste_kaart = stapel.pop()

print(bovenste_kaart)