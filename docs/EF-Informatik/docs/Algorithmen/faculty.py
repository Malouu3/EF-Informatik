n = 5

def factory(n):
    if n == 1:
        return 1
    elif n <= 0:
        return "0 oder negative Zahlen ungültig"
    else:
        return n*factory(n-1)
    # rekursiv kann früher einen stack-overflow bekommen als die Schleife unten
    """""
    fac=n
    for i in range(1, n):
        fac = fac * i
    return fac
    """""

print(factory(n))