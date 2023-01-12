board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]


##Brett

def spalten_nummer(n):          #Spaltennummern
    print('   ', end='')
    for i in range(n):
        print(f' {i + 1}  ', end='')
    print('')

def strich_horizontal(n):       #Strich zwischen den Zeilen
    print('  ', end='')
    for i in range(n):
        print('----', end='')
    print('-')

def print_zelle(z):             #Zelleninhalt
    print(f'| {z} ', end='')

def print_zeile(zeile_nr):              #Zeile wird Definiert = print_zeile(i) --> for i in range(len(board[0]))
    print(f'{zeile_nr + 1} ', end='')   #Zuerst die Zeilennummer
    for zelle in board[zeile_nr]:       #print_zelle(z) --> for z in board[len(board[0])]
        print_zelle(zelle)
    print('|')

def show():         #show() == zeigen des Brettes
    spalten_nummer(len(board[0]))       #1. Spaltennummer machen
    for i in range(len(board)):         #2. Zeilenstrich + Zeilen mit Inhalt
        strich_horizontal(len(board[i]))
        print_zeile(i)
    strich_horizontal(len(board[0]))    #3. Schlussstrich


##Eingabe

def eingabe():
    feld_xy = input('Feld (Spalte, Zeile)?: ')
    try:
        feld_xy = [int(i) -1 for i in feld_xy] #die beiden Zahlen je -1 rechnen. Ergebnis als Liste ausgegeben
        feld_x = feld_xy[0]
        feld_y = feld_xy[1] # Eingabe muss x y hingeschrieben werden. wird dann in zahlen weitergegeben.
        überprüfung(feld_x)
        überprüfung(feld_y)
        return feld_x, feld_y
    except:
        print('Ungültige Eingabe')
        eingabe()
    
def überprüfung(m):
    try:
        #überprüfung auf zahlen und länge
        m.isnumeric()
        -1 < m < len(board)
        return True   
    except:
        print('falsche Eingabe')
        return False

    

## Ausgabe der Eingabe

def process(Zeile, Spalte):     #Die ausgewählte Zelle wird mit dem Wert 0 gefüllt
    (board[Zeile, Spalte])
    board[Zeile][Spalte] = 0

def play():
    show()                  # 1. Brett abdrucken
    while True:             # 2. Solange Eingabe gemacht wird, geht es weiter
        x, y = eingabe()    # 3. Neues Brett wird abgedruckt<
        process(x, y)
        show()

play()


