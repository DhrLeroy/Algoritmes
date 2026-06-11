while True:

    ploeg = input("Geef de ploeg (ochtend/dag/avond/nacht): ")
    uren = float(input("Geef het aantal gepresteerde uren: "))

    # Uurloon bepalen
    if ploeg == "dag":
        uurloon = 15.20

    elif ploeg == "ochtend" or ploeg == "avond":
        uurloon = 18.50

    elif ploeg == "nacht":
        uurloon = 22.00

    else:
        print("Ongeldige ploeg.")
        continue

    # Basisloon berekenen
    loon = uren * uurloon

    # Premie controleren
    if (ploeg == "avond" or ploeg == "nacht") and uren > 20:
        loon = loon + 55

    # Resultaat tonen
    print("Het totale loon bedraagt", loon, "euro")