def contdor(n):
    if n == 0:
        print(0)
    else:
        print(n)
        contdor(n - 1)

contdor(9)