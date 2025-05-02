def esPar(x):
    return x % 2 == 0

def esPrimo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
        return True
