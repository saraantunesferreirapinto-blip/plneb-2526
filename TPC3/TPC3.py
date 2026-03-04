import re

f = open("dicionario_medico.txt", "r", encoding="utf8") 
texto = f.read()

texto = re.sub(r'\f', '', texto)
texto = re.sub(r'\n\n', '\n\n@', texto)
texto = re.sub(r'\n@(?=[A-ZÁÀÂÃÄÉÈÊÍÌÎÓÒÔÕÚÙÛÇ])', '\n#', texto)
texto = re.sub(r'\n\n#', '\n', texto)
texto = texto.replace('@', '')

print(texto)

conceitos = re.split(r"\n\n", texto)

def limpa_descricao(descricao):
    descricao = re.sub(r"\n", " ", descricao)
    descricao = descricao.strip()
    return descricao

conceitos_dict = {}

for c in conceitos[1:]:
    elems = re.split(r"\n", c, maxsplit=1)
    if len(elems)>1:
        designacao = elems[0]
        descricao = elems[1]
        conceitos_dict[designacao] = limpa_descricao(descricao)
    else:
        #Fix me
        continue

print(len(conceitos_dict)) #8934 conceitos

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

gera_html("dicionario_medico_TPC.html", conceitos_dict)