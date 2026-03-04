# Dicionário Médico - Processamento de Conceitos

Este repositório contém um **script Python** que processa um **dicionário médico em formato de texto** e organiza os conceitos médicos de forma estruturada.

## Passos do Script

1. **Leitura do arquivo**  
   - Abre o documento dicionario_medico.txt com encoding UTF-8.

2. **Limpeza do texto**  
   - Remove quebras de página (\f) e substitui por quebras de linha (\n).

3. **Marcação temporária de conceitos**  
   - Insere o marcador @ sempre que ocorre \n\n para indicar potenciais conceitos.  
   - Algumas definições podem ser marcadas incorretamente devido à presença de \n\n após a remoção das quebras de página.

4. **Correção de definições e conceitos**  
   - Como todos os conceitos começam com letra maiúscula (possivelmente com acentos), o script identifica essas linhas e substitui o marcador @ por #.

5. **Ajuste de quebras de linha**  
   - Substitui \n\n# por apenas \n para que a definição fique corretamente associada ao conceito.

6. **Remoção de marcadores temporários**  
   - Remove os marcadores @ que não são mais necessários.

7. **Separação dos conceitos**  
   - Divide o texto em conceitos individuais usando dupla quebra de linha (\n\n).  
   - A lista resultante é armazenada na variável conceitos.

> **Observação:** Algumas definições podem ficar cortadas devido a quebras de linha internas. Isso é tratado posteriormente no ciclo for, considerando apenas a linha seguinte ao conceito como parte da definição.s