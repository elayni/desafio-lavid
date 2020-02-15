import pandas as pd
import re 

df = pd.read_csv("/home/elayni/Documents/Desafio Lavid/dados/corpus-q3.csv")

# definindo o padrão
pattern = r'\d{1}\w{1}_\w+R_\d{1}\w{1}'

# criando o novo arquivo
novo_arquivo = open("corpus-resposta-q3.csv", "w")

def data_argumentation(file, x):    
    for linha in x:
        verbo = re.search(pattern, linha)

        if verbo == None:
            pass

# acho que o código não ficou muito legígel daqui em diante
        else: 
            nova_flex = verbo.group(0).split('_')
            p = 'S'
            s = 'S'

            for w in range(1, 3, 1):
                if w == 2:
                    p = 'P'
                for i in range(1, 4, 1):
                    for k in range(1, 3, 1):
                        if k == 1:
                                s = 'S'
                        elif k == 2:
                            s = 'P'
                            
# o for seguinte não foi bem testado
                        for j in range(1, 4, 1):                          
                            substituicao = re.sub(pattern, str(i) + p + "_" + nova_flex[1] + "_" + str(j) + s, linha)
                            file.write(substituicao + "\n")  

                

data_argumentation(novo_arquivo, df.gr)
data_argumentation(novo_arquivo, df.gi)