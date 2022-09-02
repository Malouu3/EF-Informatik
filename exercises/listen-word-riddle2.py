#Nun wurde eine weitere Zuordnungsstufe Stufe hinzugefügt 😮. 
# In der MESSAGE steht, an welcher Stelle im MAPPING der Index 
# steht, an welchem der gesuchte Buchstabe zu finden ist. 
# Finden Sie die Nachricht?

ALPHABET = [' ', '_', '.', ':', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAPPING = [54, 58, 53, 4, 8, 60, 45, 60, 12, 41, 13, 47, 60, 4, 44, 56, 62, 4, 58, 47, 41, 60, 55, 3, 9, 45, 60, 10, 19, 2, 54, 62, 48, 54, 56, 18, 41, 53, 44, 4, 58, 43, 1, 50, 54, 13, 2, 2, 49, 6, 1, 59, 14, 58, 16, 4]
MESSAGE = [32, 5, 7, 15, 51, 23, 3, 13, 48, 2, 11, 29, 14, 6, 16, 1, 9, 0, 12, 46, 41, 22, 37, 17, 38, 25, 31, 18, 20, 30, 21, 39, 40, 36, 33, 26, 55, 53, 42, 49, 8, 52, 10, 27, 4, 24, 50, 44, 54, 28, 45, 35, 47, 43, 34, 19]


print(ALPHABET[MAPPING[MESSAGE[0]]])

for msg in MESSAGE:
    print(ALPHABET[MAPPING[msg]], end='')

    
# "for msg in x": gibt die sachen eine nach der anderen an
