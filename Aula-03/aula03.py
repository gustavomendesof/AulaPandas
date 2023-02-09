import pandas as pd


combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

ca_df = combustiveis_df[['Revenda','Municipio', 'Produto','Valor de Venda']]

display(ca_df)

#DataFrame.loc[] com multiplas condições para filtragem
#Quais são os preços de ETANOL na minha cidade
etanol_indaiatuba_df = ca_df.loc[(ca_df['Produto'] == 'ETANOL') & (ca_df['Municipio'] == 'INDAIATUBA')]
etanol_indaiatuba_df.sort_values(by='Valor de Venda', inplace=True)
display(etanol_indaiatuba_df)


# Qual a media de preços dos combustiveis GASOLINA E GASOLINA ADITIVADA do Bairro BELA VISTA em SÃO PAULO
combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') & (combustiveis_df['Municipio'] == 'SAO PAULO') & ((combustiveis_df['Produto'] == 'GASOLINA') | (combustiveis_df['Produto'] == 'GASOLINA ADITIVADA')), ['Valor de Venda']].mean()

#combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') & (combustiveis_df['Municipio'] == 'SAO PAULO') & (combustiveis_df['Produto'] in ['GASOLINA' 'GASOLINA ADITIVADA'])]

# Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
display(combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') &
                            (combustiveis_df['Municipio'] == 'SAO PAULO') &
                            (combustiveis_df['Produto'].isin(["GASOLINA", "GASOLINA ADITIVADA"])),
                            ['Valor de Venda']].mean())

# Como mostrar média de valor de venda POR COMBUSTÍVEL Brasil todo?
media_por_combustivel_df = ca_df[['Produto', 'Valor de Venda']].groupby(by='Produto').mean().round(2)
display(media_por_combustivel_df)

# Quero adicionar uam coluna de valorboolea no combustives_df chamada "Ativo"
# que, por padrão, vai ser True para Todas as linhas
# Todas as Linhas

combustiveis_df['Ativo'] = True
print(combustiveis_df.info())
display(combustiveis_df.head())


# E se eu quiser uma coluna nova chamada "Obs"
# Que preencha automacticamente "Melhor cidade"
# quando o Município for INDAIATUBA, SP...
#combustiveis_df['Obs'] = "MELHOR CIDADE" if combustiveis_df['Municipio'] == "INDAIATUBA" else ""
#amanhã a solução

# Exportar para Excel o dataframe com etanol em indaiatuba...
etanol_indaiatuba_df.to_excel('etanol_indaituba.xlsx', sheet_name='Etanol em Indaiatuba')