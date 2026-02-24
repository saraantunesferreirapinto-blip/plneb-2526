import re

text = 'Ola tudo bem? Tom Tudo perfeito neste ano de 2026, 3,14 6,34 26,34765 Muito Mesmo'

print(re.search(r't',text))
print(re.findall(r'[tT]',text))
print(re.findall(r'\w',text))
print(re.findall(r'\d',text))
print(re.findall(r'\d*,\d+',text))
print(re.findall(r'\w{3,}',text))
print(re.findall(r'[^m]*M[^m]*\b',text))
