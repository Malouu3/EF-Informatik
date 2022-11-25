board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]



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