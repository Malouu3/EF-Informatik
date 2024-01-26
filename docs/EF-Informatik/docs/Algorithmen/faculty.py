n = 5

def factory(n):
    if n == 1:
        return 1
    else:
        return n*factory(n-1)

factory(n)
print(factory(n))