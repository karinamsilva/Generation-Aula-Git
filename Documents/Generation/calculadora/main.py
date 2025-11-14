from functions import calculation

# * = all tudo 

def menu():
    print('Gen Calc')
    print('1 - soma')
    print('2 - subtração')
    print('3 - mulitplicação')
    print('4 - Divisão')
    print('5 - potencia')
    print('6 - raiz ')
    print('qualquer outro digito')

if __name__ == "__main__":
# garante que o codigo só rode se executar main.py
    menu()
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))
    opcao = input('Escolha uma opção: ')

    print(calculation(num1,num2,opcao))
    

    '''if opcao == '1':
        print(soma(num1,num2))
    elif opcao == '2': 
        print(subtracao(num1,num2))
    elif opcao == '3':
        print(multiplicacao(num1,num2))
    elif opcao == '4':
        print(divisao(num1,num2))
    elif opcao == '5':
        print(potencia(num1,num2))
    elif opcao == '6':
        print(raiz(num1,num2))
    else:
        print('Operação invalida')'''






