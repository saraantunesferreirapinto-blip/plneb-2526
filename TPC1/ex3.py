def countVowels (n):
    vowels = ["a", "e", "i", "o", "u"]
    num = 0
    for letra in n.lower():
        if letra in vowels:
            num = num + 1
    print(num)

countVowels("Ola, tudo bem")