import pandas as pd

df_modelos = pd.read_csv('modelos.csv', sep=";")
#print(df_modelos)


#printando as colunas do arquivo
#print('Colunas encontradas no arquivo')
#print(list(df_modelos.columns))

#entrada manual dos dados

novo_modelo = {
    "id":"6",
    "modelo":"Airbus A321neo",
    "companhia":"Azul",
    "capacidade":"240",
    "ano_fabricacao":"2021"
}

segundo_modelo = {
    "id":"7",
    "modelo":"Boeing 747-8 Intercontinental",
    "companhia":"Lufthansa",
    "capacidade":"467",
    "ano_fabricacao":"2016"
}

terceiro_modelo = {
    "id":"8",
    "modelo":"Embraer E195-E2",
    "companhia":"KLM",
    "capacidade":"132",
    "ano_fabricacao":"2020"
}

#df_modelos = pd.concat([df_modelos, pd.DataFrame([novo_modelo, segundo_modelo, terceiro_modelo])], ignore_index=True)
#df_modelos.to_csv('modelos.csv', sep=";", index=False)


#inserção dos dados com loop while através do usuário

def choice():
    choice = input('Informe uma opção: \n1 - Adicionar um modelo \n2 - Imprimir na tela \n3 - Sair\n')
    return choice


print("______________ Modelos de Aviões ______________________\n")
escolha = choice()

while True:
    if escolha == "1":

        id = input('informe o id: ')
        modelo = input('Informe o modelo: ')
        companhia = input('Informe a companhia: ')
        capacidade = input('Informe a capacidade: ')
        ano_fabricacao = input('Informe o ano de fabricação')

        quarto_modelo = {
            "id":id,
            "modelo":modelo,
            "companhia":companhia,
            "capacidade":capacidade,
            "ano_fabricacao":ano_fabricacao
        }

        df_modelos = pd.concat([df_modelos, pd.DataFrame([quarto_modelo])], ignore_index=True)
        df_modelos.to_csv('modelos.csv', sep=";", index=False)
        #adicionando separador conforme o arquivo csv
        escolha = choice()
    elif escolha == "2":
        print(df_modelos)
        escolha = choice()
    else: 
        print("saindo")
        break 
