import math

def menu():
    print("--- CALCULADORA ---")
    print("Escolha uma operação: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Raiz Quadrada")
    print("6 - Potência")
    print("7 - Porcentagem")
    print("8 - Logaritmo")
    print("0 - Sair")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0 :
        return "Erro: não é possível dividir por zero"
    return a / b

def raiz_quadrada(a):
    return math.sqrt(a)

def potencia(a, b):
    return math.pow(a, b)

def porcentagem(a, b):
    return (a/100)*b

def logaritmo(a, b):
    return math.log(a, b)

while True:
    menu()
    try:
        escolha = int(input("Digite a opção: "))
        
        if escolha == 0:
            print("Encerrando a calculadora")
            break
    
        if escolha in [1, 2, 3, 4, 5, 6, 7, 8]:

            if escolha == 5:
                num1 = float(input("Digite o número: "))
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
        

            if escolha == 1:
                resultado = somar(num1, num2)
                print (f'Resultado: {resultado} \n')
            elif escolha == 2:
                resultado = subtrair(num1, num2)
                print (f'Resultado: {resultado} \n')
            elif escolha == 3:
                resultado = multiplicar(num1, num2)
                print (f'Resultado: {resultado} \n')
            elif escolha == 4:
                resultado = dividir(num1, num2)
                print (f'Resultado: {resultado} \n')
            elif escolha == 5:
                resultado = raiz_quadrada(num1)
                print (f'Resultado: {resultado} \n')
            elif escolha == 6:
                resultado = potencia(num1, num2)
                print (f'Resultado: {resultado} \n')
            elif escolha == 7:
                resultado = porcentagem(num1, num2)
                print (f'Resultado: {resultado} \n')
            elif escolha == 8:
                resultado = logaritmo(num1, num2)
                print (f'Resultado: {resultado} \n')
        else:
            print("Opção inválida, tente novamente.")

    except ValueError:
        print("Erro: digite apenas NÚMEROS \n")
        continue


