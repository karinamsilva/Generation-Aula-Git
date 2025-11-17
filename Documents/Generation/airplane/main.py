import pandas as pd

df_airplane = pd.read_csv('Airplane.csv')

#mostra as 5 primeiras e 5 ultimas
print(df_airplane)

#traz as primeiras 5 linhas do documento
print(df_airplane.head())