def calc_proteinas(peso, objetivo):
    if objetivo == 1:
        return peso * 2
    elif objetivo ==2:
        return peso * 1.6
    elif objetivo == 3: 
        return peso * 1.8
    else:
        return None
    #none não faz nada 

def calc_imc(peso,altura):
    return peso / (altura **2)

def imc(valor_imc):
    if valor_imc < 18.5:
        return "abaixo do peso"
    elif valor_imc < 24.9:
        return "peso normal"
    elif valor_imc < 29.9:
        return "sobrepeso"
    else:
        return "obesidade"