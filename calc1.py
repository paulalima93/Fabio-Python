def menu():
    print("--- CALCULADORA ---")
    print("Escolha uma operação: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Somar")
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


while True:
    menu()
    escolha = input("Digite a opção: ")

    if escolha == "0":
        print("Encerrando a calculadora")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == "1":
        resultado = somar(num1, num2)
    elif escolha == "2":
        resultado = subtrair(num1, num2)
    elif escolha == "3":
        resultado = multiplicar(num1, num2)
    elif escolha == "4":
        resultado = dividir(num1, num2)
    else:
        print("Opção inválida, tente novamente.")
        
    print (f'Resultado: {resultado} \n')