from collections import deque

vakken = deque()

vakken.append("Aardrijkskunde")
vakken.append("Informatica")
vakken.append("LO")
vakken.append("Frans")
vakken.append("Wiskunde")
vakken.append("Biologie")

print(vakken)

print(vakken.popleft())

print(vakken)
