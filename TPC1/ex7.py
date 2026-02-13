def balanceado (s1, s2):
    res= False
    for letra in s1:
        if letra in s2:
            res = True
        else:
            res = False
            break
    return res

print(balanceado ("sara", "sarar"))
print(balanceado ("sara", "ana"))