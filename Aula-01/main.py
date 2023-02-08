# Primeiro exemplo de manipulação de dados usando python pandas
#python -m pip install pandas - (comando para o console)

#Importanto biblioteca pandas no python
import pandas as pd


combustiveis_df = pd.read_excel("ca-2021-02.xlsx")


#Usa o print para ver o dataframe!
print(combustiveis_df)

