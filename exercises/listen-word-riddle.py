# Gegeben ist ein ALPHABET und eine Nachricht MESSAGE. 
# In der Nachricht sind die Indices der zugehörigen Buchstaben gespeichert. 
# Schreiben Sie ein Programm, welches die Nachricht decodiert 
# und in Buchstabenform darstellt.

ALPHABET = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MESSAGE = [12, 9, 19, 20, 0, 18, 9, 4, 4, 12, 5]


# print(MESSAGE[0])
# print(ALPHABET[MESSAGE[0]])


for index in range(0, len(MESSAGE)):
    print(ALPHABET[MESSAGE[index]])

for msg in MESSAGE:
    print(ALPHABET[msg], end='')