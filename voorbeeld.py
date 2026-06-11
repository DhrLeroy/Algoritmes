'''while True:

    temperatuur = float(input("Geef de temperatuur van het serverlokaal: "))

    if temperatuur < 18:
        extra = round(18-temperatuur,1)
        print(f"Te koud: energieverlies door overkoeling. . Verhoog de temperatuur met {extra} °C")
    elif temperatuur <= 27:
        print("Temperatuur is optimaal")
    elif temperatuur <= 35:
        extra = round(temperatuur - 27,1)
        print(f"Waarschuwing: serverlokaal warm. Verlaag temperatuur met {extra} °C")
    else:
        print("Kritieke temperatuur! Risico op oververhitting")'''

while True:
    batterij = float(input("Geef het batterijpercentage: "))

    if batterij < 20:
        # ecologische modus is verplicht
        resterende_tijd = batterij * 3.2
        print("Resterende tijd:", resterende_tijd, "minuten")

    else:
        stand = input("Welke stand? (eco/normaal/hoog): ")

        if stand == "hoog":
            resterende_tijd = batterij * 2.1
        elif stand == "normaal":
            resterende_tijd = batterij * 2.7
        elif stand == "eco":
            resterende_tijd = batterij * 3.2
        else:
            print("Ongeldige stand")
            resterende_tijd = None

        if resterende_tijd is not None:
            print("Resterende tijd:", resterende_tijd, "minuten")