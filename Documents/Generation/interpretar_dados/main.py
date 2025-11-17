import pandas as pd
#criar um alias para pandas, para facilitar 

df_dados_turma = pd.read_csv('dados_turma.csv')
# leitura do arquivo python pelo pandas 

#df_dados_turma = pd.read_csv('dados_turma.csv', sep=',', encoding='utf-8'
# caso o separador não seja 'j', você pode usar o sep='', para setar o separador
# caso não reconhecer operadores digitados, se altera o argumento encoding=''

print(df_dados_turma)

#adiciona novo valor no data frame e em geral o data frame tem muitos campos
# se o python lê como chave-valor, posso utilizar dicionario para adicionar valores

#inserção manual dos dados

novo_aluno = {
    "Carimbo de data/hora":"17/11/2025 10:33:42",
    "nome": "Karina",
    "cidade": "Santo André",
    "zona": "ABC"
}

df_dados_turma = pd.concat([df_dados_turma, pd.DataFrame([novo_aluno])], ignore_index=True)
# para adicionar novo valor,chame o dataframe e atribua a função concat da biblioteca pd.concat e chamar atts [meu frame e novo dado]
# como na linha acima 

df_dados_turma.to_csv("dados_turma.csv",index=False)

