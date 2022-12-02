board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

def spalten_nummer(n):
    print('   ', end='')
    for i in range(n):
        print(f' {i + 1}  ', end='')
    print('')

def strich_horizontal(n):
    print('  ', end='')
    for i in range(n):
        print('----', end='')
    print('-')

def print_zelle(z):
    print(f'| {z} ', end='')

def print_zeile(zeile_nr):
    print(f'{zeile_nr + 1} ', end='')
    for zelle in board[zeile_nr]:
        print_zelle(zelle)
    print('|')

def show():
    spalten_nummer(len(board[0]))
    for i in range(len(board)):
        strich_horizontal(len(board[i]))
        print_zeile(i)
    strich_horizontal(len(board[0]))

def eingabe():
    x = input('Spalte?: ')
    x = int(x)
    y = input('Zeile: ')
    y = int(y)
    return(x - 1, y -1)

def process(Spalte, Zeile):
    board[Zeile][Spalte] = 0

def play():
    show()
    while True:
        x, y = eingabe()
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

