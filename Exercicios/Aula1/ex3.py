def ler_ficheiro(nome):
    f = open(nome)
    ficheiro = f.read()
    linhas = ficheiro.split("\n")
    print(linhas[::-1])

ler_ficheiro("\1ano mestrado\2semestre\PLN\plneb-2526\Exercicios\Aula1\ex1.py")