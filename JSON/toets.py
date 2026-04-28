P = float(input("Aantal zonnepanelen: "))
t = float(input("Tijd (uren): "))

E = P * 430 * t
print(f"Energie: {E} Wh")

if E < 2000:
    print("Onvoldoende voor een huishouden")
if 2000 <= E <= 5000:
    print("Bruikbaar voor basisverbruik")
if E > 5000:
    print("Goede opbrengst voor dagelijks gebruik")