while True:

    verbruik = float(input("Geef het verbruik in kWh: "))

    if verbruik < 200:
        prijs_per_kwh = 0.25
    elif verbruik < 500:
        prijs_per_kwh = 0.22
    else:
        prijs_per_kwh = 0.18

    basisbedrag = verbruik * prijs_per_kwh
    totaal = basisbedrag + 15
    totaal = totaal * 1.06

    print("Totale factuur:", totaal, "euro")