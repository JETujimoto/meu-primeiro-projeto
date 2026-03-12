def somar(*args):
    total = 0

    for numero in args:
        total += numero

    return total


print("Soma 1:", somar(1, 2, 3))
print("Soma 2:", somar(10, 20, 30, 40))
print("Soma 3:", somar(5, 15))