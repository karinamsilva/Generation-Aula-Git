from functions import * 



def menu():
    print('Bem vindo ao protein-cal-gen')
    print('Escolha uma opção')
    print('1 - calcular proteinas')
    print('2 - calcular IMC')
    print('qualquer outro numero - Sair')


def menu_objetivo():
    print('Qual sua meta?')
    print('1 - Perder peso')
    print('2 - Manter peso')
    print('3 - Ganhar peso')


if __name__ == '__main__':
    


    while True:
        menu()
        opcao = int(input('Escolha a opção'))

        if opcao == 1:
            menu_objetivo()
            peso = float(input('Qual seu peso em KG: '))
            objetivo = int(input('qual seu objetivo? '))
            resultado_proteinas = calc_proteinas(peso, objetivo)

            print(f"você precisa de {round(resultado_proteinas,2)}")
        elif opcao == 2:
            peso_imc = float(input('Qual seu peso em KG: '))
            altura_imc = float(input('qual sua altura em Metros?  '))
            resultado_imc = calc_imc(peso_imc, altura_imc)
            print(f'seu imc é de {round(resultado_imc,2)}, {imc(resultado_imc)} ')

        else:
            print('FIM')
            break 



