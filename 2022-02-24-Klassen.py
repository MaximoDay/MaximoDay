class Buch:

# hier definieren wir den konstruktor
# init steht für instalieren, was bedeutet, dass ein neues Buch erstellt wird und bestimmte Anfangswerte gesetzt werden
    def __init__(self, titel: str, autor: str, untertitel: str, preis: float, verlag: str, seiten: int, taschenbuch: bool):
        # self.titel, self.autor, ..., self.taschenbuch sind Atribute der Klasse Buch
        self.titel = titel
        self.autor = autor
        self.untertitel = untertitel
        self.preis = preis
        self.verlag = verlag
        self.seiten = seiten
        self.taschenbuch = taschenbuch


     #__str__ist eine Methode der Klasse Buch   
    def __str__(self):
        return "Title: " + self.titel + ", Autor: " + self.autor

buch1 = Buch("Der Graf von Monte Christo", "Alexandre Dumas", "", 9.95, "Anaconda", 944, False)

Buch2 = Buch("Woodwalkers", "Katja Brandis", "Carags Verwandlung", 14.00, "Arena",296, False)

print(buch1)

print(buch2)

# print(buch2)
class Bibliothek:
    def __init__(self, buchbestand: list, kostenfrei: bool, adresse: str):
        pass
















