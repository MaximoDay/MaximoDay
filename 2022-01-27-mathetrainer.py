import random
import time


# Begrüßung
print("Herzlich willkommen zum Mathetrainer, viel Erfolg!")



nochmal = "JA"
punkte = 0
max_punkte = 0

while nochmal == "ja" or nochmal == "JA":

    # rechenaufgabe erstellen")
    rechenzeichen = random.choice(["+", "-", "*", "/"])

    if rechenzeichen == "+":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(0, 1000 - zahl1)
    if rechenzeichen == "-":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(0, zahl1)
    if rechenzeichen == "*":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(0, int(1000 / zahl1))
    if rechenzeichen == "/":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(1, int(1000 / zahl1))
        zahl1 = zahl1 * zahl2

    startzeit = time.time()

    # Rechenaufgabe stellen
    antwort = int(input("Was ist " + str(zahl1) + rechenzeichen + str(zahl2) + "? "))

    endzeit = time.time()


    # Auswertung
    if rechenzeichen == "+":
         max_punkte = max_punkte + 1
         if zahl1 + zahl2 == antwort:
            print("Richtig! Du hast " + str(endzeit - startzeit) + " Sekunden gebraucht.")
            punkte = punkte + 1
         else:
            print("Falsch! Die richtige Antwort wäre " + str(zahl1 + zahl2) + " gewesen.")


    if rechenzeichen == "-":
        max_punkte = max_punkte + 1
        if zahl1 - zahl2 == antwort:
            print("Richtig! Du hast " + str(endzeit - startzeit) + " Sekunden gebraucht.")
            punkte = punkte + 1
        else:
            print("Falsch! Die richtige Antwort wäre " + str(zahl1 - zahl2) + " gewesen")


    if rechenzeichen == "*":
        max_punkte = max_punkte + 1
        if zahl1 * zahl2 == antwort:
            print("Richtig! Du hast " + str(endzeit - startzeit) + " Sekunden gebraucht.")
            punkte = punkte + 2
            
        else:
            print("Falsch! Die richtige Antwort wäre " + str(zahl1 * zahl2) + " gewesen")


    if rechenzeichen == "/":
        max_punkte = max_punkte + 1
        if zahl1 / zahl2 == antwort:
            print("Richtig! Du hast " + str(endzeit - startzeit) + " Sekunden gebraucht.")
            punkte = punkte + 2
        else:
            print("Falsch! Die richtige Antwort wäre " + str(zahl1 / zahl2) + " gewesen")


    nochmal = input("Möchten Sie nocheinmal spielen? ")

print("Du hast " + str(punkte) + " Punkte von " + str(max_punkte) + " Punkten erreicht")


