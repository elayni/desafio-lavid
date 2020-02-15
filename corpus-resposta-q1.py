import pandas as pd
import re

# para esta questão estou usando a versão 2 do arquivo corpus-q1
# esta questao não foi finalizada corretamente

# importando o arquivo csv para df (dataframe)
df = pd.read_csv("/home/elayni/Documents/Desafio Lavid/dados/corpus-q1-v2.csv")

# pattern object numa tentativa de diminuir o código 
#e conseguir fazer essa questão, não consegui tempo para testar
# como fiz na primeira vez estava menos confuso, 
#ou mais didático, separando cada substituição
pattern = {
    r'(?P<letter>P|S)((?P<number>1|2|3))': '\g<number>\g<letter>',
    r'\+{2,}': '+',
    r'\s{2,}': " ",
    r'(?<=\d{1})-(?=\d+)': "",
    r'\s+(?=_CIDADE|_ESTADO|_PAÍS)': "",
    r'\s+(?=_\d{1}\w{1})': "",
    r'(?<=\d{1}\w{1}_)': " ",
    r'\s+(?=\(+|\(-)': "",
    r'(?i)(?<=não|nao) ': "_",
    r'(?i)_(?=famoso|famosa)': "&",
    r'(?<=^\d\W{1})\.|\.(?=^\d\W{1})-': "",
    r'^0-9{0,1}\.(?=\d+)': " 0."
}

dataf = []

def substituicao(pattern, df):
    for linha in df:
        for i in pattern:
            linha = re.sub(i, pattern[i], linha)
            dataf.append(linha)

substituicao(pattern, df.gr)
substituicao(pattern, df.gi)

pd.DataFrame(dataf)  #sintaxe incorreta?

# não gerou arquivo
dataf.to_csv('/home/elayni/Documents/Desafio Lavid/corpus-q1-direcionalidade.csv')

print("Seu arquivo corrigido pode ser encontrado em corpus-q1-direcionalidade.csv")