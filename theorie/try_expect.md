# Fehler abfangen

## try
Die Anweisung `try` leitet eine Ausnahmebehandlung ein. Ähnlich wie bei der `if`-Anweisung gibt es verschiedene Zweige, die das Programm durchlaufen kann. Das Programm versucht (englisch: *try*), die Anweisungen durchzuführen, die eingerückt nach `try` stehen. Falls die Eingabe erfolgreich ist, wird der `except`-Zweig nicht ausgeführt, ähnlich wie beim `else`-Zweig der `if`-Anweisung.

## except
Ist die Eingabe dagegen nicht erfolgreich und handelt es sich um einen Fehler, wird der Fehler oder die Ausnahme (englisch: *exception*) mit der Anweisung `except` abgefangen. in diesem Fall werden alle eingerückten Anweisungen im `except`-Zweig durchgeführt. Das Programm läuft ohne Abbruch zu Ende, da der Fehler zwar auftritt, aber abgefangen wird.


> Nach `try` und `except` muss jeweils ein Doppelpunkt gesetzt werden, wie bei `if-else`, `for` oder `while`.

## Beispiel

```
# Eingabe
print("Eingabe: ")
z = input()

# Versuch der Umwandlung
try:
    zahl = int(z)
    print(zahl, " ist richtig eingegeben."
    
# Fehler bei Umwandlung
except:
    print("Eingabe ungültig")
    
print("Ende des Programms")
```
