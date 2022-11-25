
def linie_aus_sternen(breite):
    print("*" * breite)


def linie_mit_seitensternen(breite):
    leere = breite - 2
    print("*" + " " * leere + "*")

'''
eingabe = input("Gib Breite an: ")
breite = int(eingabe)
eingabe = input("Gib Höhe an: ")
höhe = int(eingabe)
'''
'''
def box():
    linie_aus_sternen(breite)
    for i in range(länge):
        linie_mit_seitensternen(breite)
    linie_aus_sternen(breite)

box()
'''

def print_rechteck(breite, höhe):
    if breite < 2:
        print('Breite ist zu klein')
        return
    if höhe < 2:
        print('Höhe zu klein')
        return

    linie_aus_sternen(breite)
    for linie in range(höhe - 2):
        linie_mit_seitensternen(breite)
    linie_aus_sternen(breite)

print_rechteck(12, 3)