import re
import pandas as pd
import csv

#importando o arquivo csv para df (dataframe)
df = pd.read_csv("/home/elayni/Documents/desafio/corpus-q1-v2.csv")
teste = "P1 gdyeg_3ShhyuheP3"


#conhecendo as cinco primeiras linhas do arquivo usado
print("Estamos usando a versão 2 do corpus-q1.\n" +
    "As cinco primeiras linhas se encontram dessa maneira: \n")
#print(df.head())

direcionalidade = re.findall('[S|P][1-3]', str(df))
#direcionalidade = re.findall('[S|P]\d', teste)

if not direcionalidade:
    print("Não foram encontradas alterações deste tipo.")
else: 
    direcionalidade_corrigido = df
    direcionalidade_corrigido = re.sub('S1', '1S', str(direcionalidade_corrigido))
    direcionalidade_corrigido = re.sub('S2', '2S', str(direcionalidade_corrigido))
    direcionalidade_corrigido = re.sub('S3', '3S', str(direcionalidade_corrigido))
    direcionalidade_corrigido = re.sub('P1', '1P', str(direcionalidade_corrigido))
    direcionalidade_corrigido = re.sub('P2', '2P', str(direcionalidade_corrigido))
    direcionalidade_corrigido = re.sub('P3', '3P', str(direcionalidade_corrigido))

    #print(direcionalidade_corrigido.head())

    #direcionalidade_corrigido.to_csv(r'elayni/corpus-q1-direcionalidade.csv')

    print("Seu arquivo corrigido pode ser encontrado em corpus-q1-direcionalidade.csv")

#parte 2

intensidade = re.findall('[+]+', str(df))

if not intensidade:
    print("Não foram encontradas alterações deste tipo.")
else: 
    intensidade_corrigido = df
    intensidade_corrigido = re.sub("[+]+", "+", str(df))
    
    #direcionalidade_corrigido.to_csv(r'corpus-q1-intensidade.csv')

    print("Seu arquivo corrigido pode ser encontrado em corpus-q1-intensidade.csv")

#parte 3


espacos = re.findall('[\s]+', str(df))

if not espacos:
    print("Não foram encontradas alterações deste tipo.")
else: 
    espacos_corrigido = df
    espacos_corrigido = re.sub("[\s]+", "\s", str(df))
    
    #direcionalidade_corrigido.to_csv(r'corpus-q1-espacos.csv')

    print("Seu arquivo corrigido pode ser encontrado em corpus-q1-espacos.csv")

#parte 4

hifen = re.findall('[-]', str(df))

if not hifen:
    print("Não foram encontradas alterações deste tipo.")
else: 
    hifen_corrigido = teste
    hifen_corrigido = re.sub("[-]", "", str(df))
    
    #direcionalidade_corrigido.to_csv(r'corpus-q1-hifen.csv')

    print("Seu arquivo corrigido pode ser encontrado em corpus-q1-hifen.csv")

#parte 5

local = re.findall('[\s][_]', str(df))

if not local:
    print("Não foram encontradas alterações deste tipo.")
else: 
    local_corrigido = df
    local_corrigido = re.sub("[\s]+", "_", str(df))
    
    #direcionalidade_corrigido.to_csv(r'corpus-q1-local.csv')

    print("Seu arquivo corrigido pode ser encontrado em corpus-q1-local.csv")

#parte 6


