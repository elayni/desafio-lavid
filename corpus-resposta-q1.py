import re
import pandas as pd

# para esta questão estamos usando a versão 2 do arquivo corpus-q1

#importando o arquivo csv para df (dataframe)
df = pd.read_csv("/home/elayni/Documents/desafio/corpus-q1-v2.csv")

# pattern object
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



        
#direcionalidade_corrigido.to_csv(r'elayni/corpus-q1-direcionalidade.csv')

print("Seu arquivo corrigido pode ser encontrado em corpus-q1-direcionalidade.csv")