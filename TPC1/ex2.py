def countA (n):
    la = 0
    lA = 0
    for letra in n:
        if letra == "a":
            la = la + 1
        elif letra == "A":
            lA = lA + 1
    print (f"a palavra {n} tem {la} a e {lA} A")

countA("ola SAra A")

def countA2 (n):
    la = n.count("a")
    lA = n.count("A")
    print (f"a palavra {n} tem {la} a e {lA} A")

countA2("ola SAra A")