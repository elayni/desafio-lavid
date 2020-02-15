import pandas as pd 
import re
import json
import codecs
from collections import OrderedDict

# carregando arquivo para um dataframe
df = pd.read_csv("/home/elayni/Documents/desafio/corpus-q2.csv")

dicionario = {}

# função para contar as palavras
def contador_de_palavras(x, y):
    
    for line in y:
        encontrar_palavra= re.findall('\w+', line)

        for palavra in encontrar_palavra:
            palavra = palavra.lower()

            if palavra not in x:
                x[palavra] = 1
            else:
                x[palavra] += 1


contador_de_palavras(dicionario, df.gr)
contador_de_palavras(dicionario, df.gi)

# muita dificuldade em conseguir usar OrderedDict, mas se saiu melhor que Counter
# lembra a ordem que as palavras foram inseridas
dicionario = OrderedDict(sorted(dicionario.items(), key=lambda col: -col[1]))

# salvando dicionário no arquivo json
file = codecs.open("corpus-q2-json.json", "w", "utf-8")
json.dump(dicionario, file, indent=4, sort_keys=False, ensure_ascii=False)
file.close()