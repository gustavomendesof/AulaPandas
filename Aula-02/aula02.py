# Primeiro exemplo de manipulação de dados usando python pandas
#python -m pip install pandas - (comando para o console)

#Importanto biblioteca pandas no python
import pandas as pd

combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

#Usa o display  para ver o dataframe
display(combustiveis_df)

#Exibe as primeiras 5 linhas
display(combustiveis_df.head())

#Quero na verdade exibir as 15 primeiras 15 linhas
display(combustiveis_df.head(15))

#Comnados dataframe.shape e dataframe.describe()

print(combustiveis_df.shape)
#mostra o numero de linhas e colunas

#Só as linhas
print(combustiveis_df.shape[0])

#Quais são as colunas e que tipo de dados cada um tem...
print(combustiveis_df.info())

#Describe() mostra as estatisticas mais basicas que a gente precisa
print(combustiveis_df.describe())

#Filtrar apenas por uma coluna
display(combustiveis_df['Revenda'])

#Aqui criamos um novo dataframe apenas com as colunas que eu quero
ca_df = combustiveis_df[['Revenda','Municipio', 'Produto','Valor de Venda']]

display(ca_df)

#Exibe a 4a. linha
display(ca_df.loc[3])

#Exibir da 10a. linha até a 20a.linha
display(ca_df.loc[9:19])

#Criar uma data frama gas_df contendo apenas 4 colunas (Revenda, Municipio, Produdo, valor de venda)
#somente com combustivel sendo gasolina e exibir na tela
gas_df = ca_df.loc[ca_df['Produto'] == 'GASOLINA']
display(gas_df)
display(gas_df['Valor de Venda'].max())


#Se eu quisar saber qual é o posto e municipio da gasolina mais cara do pais?
display(gas_df[['Revenda', 'Municipio', 'Valor de Venda']].max())


