def anagrama(s1, s2):
    letras= []
    res = True
    for letra in s1:
        letras.append(letra)
    for letra2 in s2:
        if letra2 not in letras:
            res = False
    return res

print(anagrama("listen","silent"))
print(anagrama("hello","world"))