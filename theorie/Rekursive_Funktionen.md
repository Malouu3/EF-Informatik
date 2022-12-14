# Rekursive Funktionen 
Bestimmte Abläufe lassen sich am besten rekursiv programmieren. Eine rekursive Funktion ruft sich immer wieder selbst auf. Damit dies nicht zu einer endlosen Menge an Funktionsaufrufen führt, muss es eine Bedingung geben, die der Rekursion ein Ende setzt. Zudem wird ein erster Aufruf benötigt, der die Rekursion einleitet. 

Das Prinzip der Rekursion lässt sich bereits anhand des folgenden einfachen Programms verdeutlichen. Sie finden darin die rekursive Funktion `halbieren()`, die bei jedem Aufruf den ihr übergebenen Wert halbiert. Anschließend ruft sie sich selbst wieder auf, und zwar mit dem halbierten Wert. Die Rekursion endet, wenn der Wert, der ständig halbiert wird, eine bestimmte Grenze unterschreitet. Der erste Aufruf der rekursiven Funktion erfolgt mit einem Startwert aus dem Hauptprogramm heraus.

## Beispiel
```
def halbieren(wert):
    print(wert)
    wert = wert / 2

if wert > 0.05:
    halbieren(wert)

# Programm
halbieren(3)
```
Ausgabe des Programms:
__3__
__1.5__
__0.75__
__0.375__
__0.1875__
__0.09375__

Der rekursive Aufruf erfolgt gemäß der Bedingung wert _> 0.05_. Ohne diese Bedingung würde die Rekursion endlos weiterlaufen.
