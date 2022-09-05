# Primzahlen

for nummer in range(1, 101):           # läuft alle Zahlen von 1 - 101 ab und setzt sie in die Variable "nummer"
    if nummer > 1:                     # Wenn "nummer" grösser als 1 ist:
        for i in range(2, nummer):      # dann wird die nummer durch die variable "i" geteilt, die von null bis
            if (nummer % i) == 0:       # zum Wert "nummer" alle einmal darstellt. Wenn jetzt aus der Division
                break                   # keinen Restwert entsteht, wird der vorgang für den derzeitigen Wert
                                        # "nummer" abgebrochen. Wenn es keinen Rest gibt, wird "nummer" ausgegeben.
        else:
            print(nummer)
