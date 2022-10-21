# Primzahlen

primzahlen = []

for nummer in range(1, 1001):           
    if nummer > 1:                     
        for i in range(2, nummer):      
            if (nummer % i) == 0:       
                break                   
                                        
        else:
            primzahlen.append(nummer)   

print(primzahlen)

# läuft alle Zahlen von 1 - 101 ab und setzt sie in die Variable "nummer"
# Wenn "nummer" grösser als 1 ist:
# dann wird die nummer durch die variable "i" geteilt, die von null bis
# zum Wert "nummer" alle einmal darstellt. Wenn jetzt aus der Division
# keinen Restwert entsteht, wird der vorgang für den derzeitigen Wert
# "nummer" abgebrochen. Wenn es keinen Rest gibt, wird "nummer" ausgegeben.
#Setzt die Zahl in die Liste Primzahlen