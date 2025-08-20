# calculadora.py

class Cores:
    ROXO = '\033[95m'       # roxo (magenta claro)
    VERMELHO = '\033[91m'   # vermelho
    RESET = '\033[0m'       # resetar cor
    NEGRITO = '\033[1m'     # negrito

def mostrar_menu():
    print(f"{Cores.ROXO}{Cores.NEGRITO}=== Simple Calculator ==={Cores.RESET}")
    print(f"{Cores.ROXO}developed by David Matos{Cores.RESET}\n")
    print(f"{Cores.ROXO}Escolha a operação:{Cores.RESET}")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def obter_operacao():
    op = input(f"{Cores.ROXO}Digite o número da operação (1-4): {Cores.RESET}")
    if op not in ("1", "2", "3", "4"):
        print(f"{Cores.VERMELHO}Operação inválida.{Cores.RESET}")
        return None
    return op

def obter_numero(mensagem):
    while True:
        try:
            return float(input(f"{Cores.ROXO}{mensagem}{Cores.RESET}"))
        except ValueError:
            print(f"{Cores.VERMELHO}Valor inválido. Digite um número válido.{Cores.RESET}")

def calcular(op, num1, num2):
    if op == "1":
        return num1 + num2, "+"
    elif op == "2":
        return num1 - num2, "-"
    elif op == "3":
        return num1 * num2, "*"
    elif op == "4":
        if num2 == 0:
            print(f"{Cores.VERMELHO}Erro: divisão por zero.{Cores.RESET}")
            return None, None
        return num1 / num2, "/"

def main():
    mostrar_menu()
    op = obter_operacao()
    if not op:
        return

    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")

    resultado, simbolo = calcular(op, num1, num2)

    if resultado is not None:
        print(f"\n{Cores.ROXO}{Cores.NEGRITO}Resultado:{Cores.RESET} {num1} {simbolo} {num2} = {Cores.ROXO}{resultado}{Cores.RESET}")

if __name__ == "__main__":
    main()
