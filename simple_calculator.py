# calculadora_bilingue.py

class Cores:
    ROXO = '\033[95m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'
    NEGRITO = '\033[1m'

# Dicionários de tradução
mensagens = {
    "PT": {
        "titulo": "=== Calculadora Simples ===",
        "autor": "Desenvolvido por David Matos",
        "escolha_operacao": "Escolha a operação:",
        "opcoes": ["1 - Adição", "2 - Subtração", "3 - Multiplicação", "4 - Divisão", "0 - Sair"],
        "digite_op": "Digite o número da operação (0-4): ",
        "invalida": "Operação inválida.",
        "numero1": "Digite o primeiro número: ",
        "numero2": "Digite o segundo número: ",
        "erro_zero": "Erro: divisão por zero.",
        "resultado": "Resultado:",
        "saindo": "Saindo da calculadora. Até mais!",
        "invalido": "Valor inválido. Digite um número válido.",
        "idioma": "Escolha o idioma / Choose language (PT/EN): ",
        "idioma_invalido": "Idioma inválido. Usando português por padrão.",
    },
    "EN": {
        "titulo": "=== Simple Calculator ===",
        "autor": "Developed by David Matos",
        "escolha_operacao": "Choose the operation:",
        "opcoes": ["1 - Addition", "2 - Subtraction", "3 - Multiplication", "4 - Division", "0 - Exit"],
        "digite_op": "Enter the operation number (0-4): ",
        "invalida": "Invalid operation.",
        "numero1": "Enter the first number: ",
        "numero2": "Enter the second number: ",
        "erro_zero": "Error: division by zero.",
        "resultado": "Result:",
        "saindo": "Exiting calculator. See you!",
        "invalido": "Invalid input. Please enter a valid number.",
        "idioma": "Escolha o idioma / Choose language (PT/EN): ",
        "idioma_invalido": "Invalid language. Defaulting to Portuguese.",
    }
}

def mostrar_menu(lang):
    print(f"{Cores.ROXO}{Cores.NEGRITO}{mensagens[lang]['titulo']}{Cores.RESET}")
    print(f"{Cores.ROXO}{mensagens[lang]['autor']}{Cores.RESET}\n")
    print(f"{Cores.ROXO}{mensagens[lang]['escolha_operacao']}{Cores.RESET}")
    for opcao in mensagens[lang]["opcoes"]:
        print(opcao)

def obter_operacao(lang):
    op = input(f"{Cores.ROXO}{mensagens[lang]['digite_op']}{Cores.RESET}")
    if op not in ("0", "1", "2", "3", "4"):
        print(f"{Cores.VERMELHO}{mensagens[lang]['invalida']}{Cores.RESET}")
        return None
    return op

def obter_numero(lang, mensagem):
    while True:
        try:
            return float(input(f"{Cores.ROXO}{mensagem}{Cores.RESET}"))
        except ValueError:
            print(f"{Cores.VERMELHO}{mensagens[lang]['invalido']}{Cores.RESET}")

def calcular(op, num1, num2, lang):
    if op == "1":
        return num1 + num2, "+"
    elif op == "2":
        return num1 - num2, "-"
    elif op == "3":
        return num1 * num2, "*"
    elif op == "4":
        if num2 == 0:
            print(f"{Cores.VERMELHO}{mensagens[lang]['erro_zero']}{Cores.RESET}")
            return None, None
        return num1 / num2, "/"

def escolher_idioma():
    lang = input(f"{Cores.ROXO}{mensagens['PT']['idioma']}{Cores.RESET}").strip().upper()
    if lang not in ("PT", "EN"):
        print(f"{Cores.VERMELHO}{mensagens['PT']['idioma_invalido']}{Cores.RESET}")
        return "PT"
    return lang

def main():
    lang = escolher_idioma()
    while True:
        mostrar_menu(lang)
        op = obter_operacao(lang)

        if op is None:
            continue
        if op == "0":
            print(f"{Cores.ROXO}{mensagens[lang]['saindo']}{Cores.RESET}")
            break

        num1 = obter_numero(lang, mensagens[lang]["numero1"])
        num2 = obter_numero(lang, mensagens[lang]["numero2"])

        resultado, simbolo = calcular(op, num1, num2, lang)

        if resultado is not None:
            print(f"\n{Cores.ROXO}{Cores.NEGRITO}{mensagens[lang]['resultado']}{Cores.RESET} {num1} {simbolo} {num2} = {Cores.ROXO}{resultado}{Cores.RESET}")
        print()  # linha em branco

if __name__ == "__main__":
    main()
