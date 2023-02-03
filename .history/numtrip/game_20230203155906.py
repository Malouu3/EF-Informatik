import random


n = 5  # Anzahl Spalten
m = n  # Anzahl Zeilen

board = [[2**random.randint(1, 4) for i in range(1, m + 1)]
         for j in range(1, m + 1)]

# Brett


def spalten_nummer(n):  # Spaltennummern
    print('    ', end='')
    for i in range(n):
        print(f' {i + 1}    ', end='')
    print('')


def strich_horizontal(n):  # Strich zwischen den Zeilen
    print('  ', end='')
    for i in range(n):
        print('------', end='')
    print('-')


def print_zelle(z):  # Zelleninhalt
    print(f'|  {z}  ', end='')


# Zeile wird Definiert = print_zeile(i) --> for i in range(len(board[0]))
def print_zeile(zeile_nr):
    print(f'{zeile_nr + 1} ', end='')  # Zuerst die Zeilennummer
    # print_zelle(z) --> for z in board[len(board[0])]
    for zelle in board[zeile_nr]:
        print_zelle(zelle)
    print('|')


def show():  # show() == zeigen des Brettes
    spalten_nummer(n)  # 1. Spaltennummer machen
    for i in range(m):  # 2. Zeilenstrich + Zeilen mit Inhalt
        strich_horizontal(len(board[i]))
        print_zeile(i)
    strich_horizontal(n)  # 3. Schlussstrich


# Eingabe

def eingabe():
    valid = False
    while not valid:
        zeile = input("Zeile: ").strip(" ")
        spalte = input("Spalte: ").strip(" ")

        if eingabe_überprüfung(zeile, spalte) and gültigkeit_feld(zeile, spalte):
            valid = True
        else:
            print("Ungültige Eingabe")
    return (int(zeile))-1, (int(spalte)) - 1


def eingabe_überprüfung(zeile, spalte):
    try:
        # Wenn nich numeric, wird -1 ausgegeben
        x = (int(spalte.isnumeric()) - 1)
        y = (int(zeile.isnumeric()) - 1)
    except:
        print("Versuch es noch einmal")
        return False
    if x < 0 or x > n:
        print("Eingabe zur Spalte ungültig")
        return False
    if y < 0 or y > m:
        print("Eingabe zur Zeile ungültig")
        return False
    return True


def gültigkeit_feld(zeile, spalte):
    zeile = (int(zeile)) - 1
    spalte = (int(spalte)) - 1
    # überprüfung rechts
    if (spalte + 1) <= (n-1) and board[zeile][spalte] == board[zeile][spalte + 1]:
        return True
    # überprüfung links
    if (spalte - 1) <= (n-1) and board[zeile][spalte] == board[zeile][spalte - 1]:
        return True
    # überprüfung unten
    if (zeile + 1) <= (m-1) and board[zeile][spalte] == board[zeile + 1][spalte]:
        return True
    # überprüfung oben
    if (zeile - 1) <= (m-1) and board[zeile][spalte] == board[zeile - 1][spalte]:
        return True

    #print("Das gewählte Feld hat keine gleiche Nachbarfelder. Versuchs noch mal!")
    # return False


# Ausgabe der Eingabe

def aufdecken(zeile, spalte, feldzahl):  # Die ausgewählte Zelle wird mit dem Wert 0 gefüllt
    # Rahmenbedingungen
    if zeile < 0 or zeile > m-1:
        return False
    if spalte < 0 or spalte > n-1:
        return False

    # Feldüberprüfunge
    if board[zeile][spalte] == feldzahl:
        board[zeile][spalte] = 0
        aufdecken(zeile + 1, spalte, feldzahl)  # unten
        aufdecken(zeile - 1, spalte, feldzahl)  # oben
        aufdecken(zeile, spalte + 1, feldzahl)  # rechts
        aufdecken(zeile, spalte - 1, feldzahl)  # links
        return True
    else:
        return False


def feld_auffüllen(zeile, spalte, feldzahl):
    board[zeile][spalte] = feldzahl * 2
    for y in range(m - 1, 0, -1):
        for x in range(n - 1, 0, -1):
            if x == 0:  # Wenn die Zelle den Wert 0 hat...
                zeilenindex = y  # ...merkt sich die Zeile
                # solange nicht an der obersten Zeile angelangt oder die höhere Zelle nicht den Wert 0 hat...
                while not zeilenindex <= 0 and board[zeilenindex][x] == 0:
                    # wird weiter höher gegangen.
                    zeilenindex = zeilenindex - 1
                # Startpunkt bekommt denn wert oberhalb von ihm. Die leere Zelle wird random gefüllt.
                board[y][x] = board[zeilenindex][x]
                board[zeilenindex][x] = 0
    for y in range(m):
        for x in range(n):
            if board[y][x] == 0:
                board[y][x] = random.choice([2, 4, 8])


# Ausgang des Spiesls

def gewonnen():
    for zeile in board:
        for feld in zeile:
            if feld == 1024:
                print("Gewonnen!")
                return True
    return False


def verloren():
    for zeile in range(m):
        for feld in range(n):
            if board[zeile][feld] == -1:
                return True
            if zeile > 0 and board[zeile][feld] == board[zeile-1][feld]:
                return True
            if zeile < m and board[zeile][feld] == board[zeile+1][feld]:
                return True
            if feld > 0 and board[zeile][feld] == board[zeile][feld-1]:
                return True
            if feld < n and board[zeile][feld] == board[zeile][feld+1]:
                return True
    print("Keine weiteren Züge möglich!")
    return False


def play():        # 1. Brett abdrucken
    while not gewonnen() and verloren():
        show()               # 2. Solange Eingabe gemacht wird, geht es weiter
        zeile, spalte = eingabe()    # 3. Neues Brett wird abgedruckt<
        feldzahl = board[zeile][spalte]
        aufdecken(zeile, spalte, feldzahl)
        feld_auffüllen(zeile, spalte, feldzahl)


play()
