board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]


#Brett

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
    x = input('Spalte?: ')
    x = int(x)
    y = input('Zeile: ')
    y = int(y)
    return(x - 1, y -1)

def process(Spalte, Zeile):     #Die ausgewählte Zelle wird mit dem Wert 0 gefüllt
    board[Zeile][Spalte] = 0

def play():
    show()                  # 1. Brett abdrucken
    while True:             # 2. Solange Eingabe gemacht wird, geht es weiter
        x, y = eingabe()    # 3. Neues Brett wird abgedruckt<
        process(x, y)
        show()

play()

'''

def Brett():
# Zeilen nacheinander aus dem Board
    spalten = len(board[1])+1
    print('    ', end='')

    for spalte in range(1, spalten):
        print(f'  {spalte} ', end='')

    print('')
    for zeile in board:
        zeilennummer = board.index(zeile) + 1

        print('   ', end='')
        for zelle in zeile:
            # macht die wagrechten linien. so viele Linien wie anzahl Zellen
            print(' -- ', end='')
        print('-')
        
        print(zeilennummer, ' ', end='')
        #Bildet die einzelnen Werte der Zellen nacheinader ab.
        for zelle in zeile:
            #f'' formatiert Zellenwert mit Text. end='' verhindert den Zeilenumbrung
            print(f'| {zelle} ', end='')
        print('|')

    # die untersten wagrechten Linien
    print('   ', end='')
    for zelle in board[0]:
        print(' -- ', end='')
    print('-')

Brett()

eingabe = input("Zeile: ")
try:
    x = int(eingabe)
    print(x)
except:
    print("Falsch")
    

eingabe = input("Spalte: ")
try:
    y = int(eingabe)
    print(y)
except:
    print("Falsch")
    
print(board[x[y]])
'''

