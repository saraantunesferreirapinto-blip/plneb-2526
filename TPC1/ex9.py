def anagrama(s1, s2):
    res = True
    if sorted(s1) == sorted(s2):
        res = True
    else:
        res = False
    return res

print(anagrama("listen","silent"))
print(anagrama("hello","world"))