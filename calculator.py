def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b


while True:

    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Escolha uma opção: ")

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida")
        continue

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = soma(n1, n2)
    elif opcao == "2":
        resultado = subtracao(n1, n2)
    elif opcao == "3":
        resultado = multiplicacao(n1, n2)
    elif opcao == "4":
        resultado = divisao(n1, n2)

    print(f"Resultado: {resultado}")

    continuar = input("Quer continuar? (s/n): ").lower()

    if continuar == "n":
        print("Programa encerrado.")
        break
