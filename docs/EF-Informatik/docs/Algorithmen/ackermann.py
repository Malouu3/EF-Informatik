import matplotlib.pyplot as plt

def ackermann(m, n, results=None):
    if results is None:
        results = []
    
    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ackermann(m - 1, 1, results)
    elif m > 0 and n > 0:
        result = ackermann(m - 1, ackermann(m, n - 1, results), results)

    results.append(result)
    return result

# Ergebnisliste
results = []

# Ackermann-Funktion für kleine Werte aufrufen
ackermann(2, 2, results)

# Ergebnisse plotten
plt.plot(results)
plt.title('Ackermann-Funktion Ergebnisse (m=2, n=2)')
plt.xlabel('Aufruf')
plt.ylabel('Ergebnis')
plt.show()
