def cuenta_regresiva(n):
    if n == 0:
        print(0)
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(9)