def capicua(n):
    if n == n[::-1]:
        print(f"{n} é capicua")
    else:
        print(f"{n} nao e capicua")

capicua("sara")
capicua("saras")