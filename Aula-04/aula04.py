#Importando a biblioteca pandas no python
import pandas as pd



#Inserção simples de dado
combustiveis_df['Ativo'] = True

display(combustiveis_df.head())

# Criar uma coluna "Obs" que tenha nela escrito "MELHOR CIDADE" quando a coluna Municipio for igual a INDAIATUBA
combustiveis_df['Obs'] = ["MELHOR CIDADE" if Municipio == 'SAO PAULO' else None for Municipio in combustiveis_df['Municipio']]
display(combustiveis_df.loc[combustiveis_df['Municipio'].isin(['SAO PAULO','INDAIATUBA', 'CAMPINAS', 'SALTO']), ['Municipio','Obs']])

# Como preencher uma colina 'Valor de Venda - Status que verifica o seguinte
# se o valor de venda for maior que 6,5 reais, ele fala que ta caro ... caso contrario, esta barato
import numpy as np

combustiveis_df['Valor de Venda - Status'] = np.where(combustiveis_df['Valor de Venda'] > 6.5, 'Caro', 'Barato')

display(combustiveis_df[['Revenda', 'Valor de Venda', 'Valor de Venda - Status']])

# Como preencher uma colina 'Valor de Venda - Status que verifica o seguinte
# se o valor de venda for maior que 6,5 reais, ele fala que ta caro ... caso contrario, esta barato
import numpy as np

combustiveis_df['Valor de Venda - Status'] = np.where(combustiveis_df['Valor de Venda'] > 6.5, 'Caro', 'Barato')

display(combustiveis_df[['Revenda', 'Valor de Venda', 'Valor de Venda - Status']])

# Calcular postos de gasolina por habitantes temos na amostragem de combustiveis nov/2021

num_habitantes_df = pd.read_csv("ibge_num_habitantes_estimado.csv", sep=";")
num_habitantes_df.rename(columns={"Estado":"Estado - Sigla"}, inplace=True)
display(num_habitantes_df)

# Fazer um Merge dos dois dataframes
colunas = ['Municipio', 'Estado - Sigla']
merge_df = combustiveis_df.merge(num_habitantes_df, how="inner", on=colunas)
display(merge_df)
print(merge_df.info())

colunas=['Regiao - Sigla', 'Nome da Rua', 'Numero Rua',
         'Bairro', 'Cep', 'Produto', 'Data da Coleta', 'Valor de Venda',
         'Unidade de Medida', 'Bandeira', 'Ativo', 'Status do Valor de Venda']
merge_df.drop(labels=colunas, axis=1, inplace=True)
print(merge_df.info())

# Remover a linhas duplicadas
merge_df.drop_duplicates(inplace=True)
display(merge_df.head(100))

#Agrupar e contar quantos postos tem na cidade..
postos_por_municipio_df = merge_df.groupby(by=['Estado - Sigla', 'Municipio', 'NumHabitantes2021']).count()
postos_por_municipio_df.drop('CNPJ da Revenda', axis=1, inplace=True)
postos_por_municipio_df.rename(columns={"Revenda": "Número de Postos"}, inplace=True)
display(postos_por_municipio_df)

#AQUI O FINAL ESTÁ COM PROBLEMA

#Agrupar e contar quantos postos tem na cidade..
postos_por_municipio_df = merge_df.groupby(by=['Estado - Sigla', 'Municipio', 'NumHabitantes2021']).count()
display(postos_por_municipio_df.info())
postos_por_municipio_df.drop('CNPJ da Revenda', axis=1, inplace=True)
postos_por_municipio_df.rename(columns={"Revenda": "NumPostos"}, inplace=True)

#postos_por_municipio_df['PostosPorHabitante'] = postos_por_municipio_df['NumPostos'] / postos_por_municipio_df['NumHabitantes2021']
display(postos_por_municipio_df)

#AQUI O FINAL ESTÁ COM PROBLEMA

#Agrupar e contar quantos postos tem na cidade..
postos_por_municipio_df = merge_df.groupby(by=['Estado - Sigla', 'Municipio', 'NumHabitantes2021']).count()
postos_por_municipio_df.reset_index(inplace=True)
#display(postos_por_municipio_df.info())
postos_por_municipio_df.drop('CNPJ da Revenda', axis=1, inplace=True)
postos_por_municipio_df.rename(columns={"Revenda": "NumPostos"}, inplace=True)

postos_por_municipio_df['PostosPorHabitante'] = postos_por_municipio_df['NumPostos'] / postos_por_municipio_df['NumHabitantes2021']
display(postos_por_municipio_df.info())
display(postos_por_municipio_df)