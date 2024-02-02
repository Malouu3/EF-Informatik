m = 3
n = 1

def ackermann(m, n):
    """Berechnet die Ackermann-Funktion für gegebene m und n."""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    else:
        return None  # Für den Fall, dass m oder n negativ sind

# Beispielaufrufe
print(ackermann(m, n))  # Gibt 1 zurück

