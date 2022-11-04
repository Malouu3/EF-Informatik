board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

# Zeilen nacheinander aus dem Board
for zeile in board:
    for zelle in zeile:
        # macht die wagrechten linien. so viele Linien wie anzahl Zellen
        print(' -', end='')
    print(' ')
    #Bildet die einzelnen Werte der Zellen nacheinader ab.
    for zelle in zeile:
        #f'' formatiert Zellenwert mit Text. end='' verhindert den Zeilenumbrung
        print(f'|{zelle}', end='')
    print('|')

# die untersten wagrechten Linien
for zelle in board[0]:
    print(' -', end='')
print(' ')

'''
def brett():
    for zeile in board:
        for zelle in zeile:
            print(' -', end='')
        print(' ')
        for zelle in zeile:
            print(f'|{zelle}', end='')
        print('|')

for zelle in board[0]:
    print(' -', end='')
print(' ')

'''
