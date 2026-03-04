import re

#ler ficheiro txt

f = open("dicionario_medico.txt", "r", encoding="utf8") #se der problemas por 
texto = f.read()

#limpar texto (por exemplo tirar o FF (\f) da quebra de pagina)

texto = re.sub(r"\f", "", texto) #substituimo o \f por nada

#marcar informação

texto = re.sub(r"\n\n", "\n\n@", texto)

#print(texto)

#capturar conceitos

conceitos = re.split(r"@", texto)
print(len(conceitos))

def limpa_descricao(descricao):
    descricao = re.sub(r"\n", " ", descricao)
    descricao = descricao.strip() #tira os espacos a frente e atras 
    return descricao

conceitos_dict = {}

for c in conceitos[1:]:
    elems = re.split(r"\n", c, maxsplit=1)
    if len(elems)>1:
        designacao = elems[0]
        #print("designacao: ", designacao)
        descricao = elems[1]
        #print("descricao: ", descricao)
        #print("-"*20)
        conceitos_dict[designacao] = limpa_descricao(descricao)
    else:
        #Fix me
        continue

print(len(conceitos_dict))

import json

#json.dump() - escreve num ficheiro
#json.load() - le de um ficheiro
#ensure_ascii=False - faz com que converta bem os acentos e assim
#indent = 4 - torna o ficheiro mais legivel

def gera_json(filename, conceitos_dict):
    f_out = open(filename, "w", encoding="utf8")
    json.dump(conceitos_dict, f_out, indent=4, ensure_ascii=False)

gera_json("dicionario_medico.json", conceitos_dict)
    
def gera_html(filename, conceitos_dict):
    html = """
    <html>
        <head>
        <title> Dicionário Médico </title>
        <meta charset="UTF-8">
        </head>
        <body>"""

    for c in conceitos_dict:
        html = html + f"""
        <div>
            <p> <b> {c} </b> </p>
            <p> {conceitos_dict[c]} </p>
        </div>
        <hr>
        """
    html = html + """</body>
    </html>
    """   

    f_out = open(filename, "w", encoding="utf8")
    f_out.write(html)

gera_html("dicionario_medico.html", conceitos_dict)