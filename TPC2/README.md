Neste trabalho TPC2 foram usadas expressões regulares em Python para resolver vários exercícios de manipulação de texto.

Ao longo dos exercícios trabalhou-se a pesquisa, validação, extração, divisão e substituição de padrões em strings com o módulo re, assim como correspondência de padrões e quantificadores, com o objetivo de perceber melhor como construir e aplicar expressões regulares em situações práticas.

Exercícios Realizados
- ex 1.1 - verificar se a palavra "hello" começa a string com o re.match()
- ex 1.2 - procurar a palavra "hello" em qualquer posição com o re.search()
- ex 1.3 – encontra todas as ocorrências da palavra "hello" com letras maiúsculas ou minúsculas utilizando o re.findall() e a flag re.IGNORECASE 
- ex 1.4 – substitui ocorrências da palavra "hello", com letras maiúsculas ou minúsculas, pela palavra "HEY" com o re.sub()
- ex 1.5 - separa a string dada pelas virgulas com o re.split(), devolvendo a lista com as strings separadas 
- ex 2 – palavra_magica - Verifica, com o re.search(), se uma frase termina com "por favor" seguido de pontuação válida ([.?!])
- ex 3 – narcissismo - Começa por encontrar todas as ocorrências da palavra "eu" com o re.findall() e ignorando maiúsculas e minúsculas com o re.IGNORECASE. Como o findall() devolve uma lista das ocorrências encontradas, faz-se o len dessa lista que devolve o número total de vezes que "eu" aparece
- ex 4 – troca_de_curso - Substitui todas as ocorrências de "LEI" com  o re.sub() pelo nome de um curso fornecido.
- ex 5 – soma_string - Divide a string pelos separadores vírgula usando re.split(), percorre a lista obtida convertendo cada elemento para inteiro com int() e soma todos os valores, devolvendo no final o total da soma.
- ex 6 – pronomes - Procura na frase todos os pronomes pessoais indicados usando re.findall(), garantindo, com \b, que correspondem a palavras completas, e ignora maiúsculas/minúsculas com re.IGNORECASE, devolvendo a lista dos pronomes encontrados.
- ex 7 – variavel_valida - Verifica se o nome corresponde a uma variável válida usando re.match(), garantindo que começa por uma letra maiúscula ([A-Z]) e é seguida apenas por caracteres como letras, números ou underscores (\w*), até ao fim da string ($).
- ex 8 – inteiros - Procura na frase todos os números inteiros usando re.findall(), permitindo um sinal negativo opcional (-?) seguido de um ou mais dígitos (\d+), e devolve a lista dos números encontrados.
- ex 9 – underscores - Substitui espaços por _ com o re.sub(), garantindo que múltiplos espaços seguidos resultam num único underscore ([ +])
- ex 10 – codigos_postais - Percorre a lista de códigos postais e, para cada um, usa re.split("-") para o dividir em duas partes com base no hífen, guardando o resultado numa nova lista que é devolvida no final como uma lista de listas