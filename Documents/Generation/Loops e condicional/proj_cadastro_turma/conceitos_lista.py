#lista - variavel que suporta muitos dados

frutas = []
#lista vazia 
print(frutas)

#adicionar, ver, excluir ou sair

print('__________________ Bem vindo ao Varejão Gen________________________')
print('Suas opções são: \n1 - adicionar fruta \n2 - Excluir fruta \n3- Ver lista \n4 - Sair')

escolha = int(input('Qual opção desejada? '))
if escolha < 1 or escolha > 4:
    print('Escolha inválida, finalizando o sistema')
else:
    while escolha >= 1 or escolha <= 4:
        if escolha == 1:
            fruta = input('qual fruta quer adicionar? ')
            frutas.append(fruta)
            escolha = int(input('Qual opção desejada? '))
        elif escolha == 2: 
            for posicao, cada_fruta in enumerate(frutas, start=1):
                print(f"fruta {cada_fruta} está na posição {posicao}")
            excluir_fruta = int(input('Qual fruta deseja excluir'))
            print(f'fruta {frutas[excluir_fruta-1]} excluida')
            frutas.pop(excluir_fruta-1)
            escolha = int(input('Qual opção desejada? '))
        elif escolha == 3:
            for i in frutas:
                print(i)
            escolha = int(input('Qual opção desejada? '))
        else: 
            print('Saindo...')
            break
        