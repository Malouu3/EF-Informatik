from timeit import timeit
from random import shuffle
from copy import deepcopy

def insertion_sort(a):
    shuffle(a)
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

to_sort = list(range(20000))
shuffle(to_sort)
print('Unsortiert:', to_sort)
print('Sortiert:  ', insertion_sort(to_sort))

execution_time = timeit(lambda: insertion_sort(deepcopy(to_sort)), number=1)
print('Zeit für 100x Sortieren:', execution_time)