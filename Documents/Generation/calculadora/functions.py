

'''def soma(num1,num2):
    return num1 + num2 

def subtracao(num1,num2):
    return num1 - num2 

def divisao(num1,num2):
    if num2 == 0:
            return "Erro, não é possível dividir por zero"
    else:
        return num1 / num2 

def multiplicacao(num1,num2):
    return num1 * num2 


def potencia(num1,num2):
    return num1 ** num2 

def raiz(num1,num2):
    if num2 < 0:
        return "Erro ao calcular"
    else:
        return num1 ** (1/num2)'''

def calculation(num1,num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation.lower() == 'x':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Erro, não é possível dividir por zero"
        else:
            return num1 / num2 
    elif operation == 'P':
        return num1 ** num2
    elif operation == 'R':
        return num1 ** (1/num2)

