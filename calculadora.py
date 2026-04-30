# calculadora.py
# Nível Básico - Calculadora Simples
# Disciplina: Engenharia de Prompt e Aplicações em IA - UDF
# Gerado com apoio do GitHub Copilot e revisado pelo autor

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números. Lança erro se divisor for zero."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b

def exibir_menu():
    print("\n========== CALCULADORA ==========")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
    print("=================================")

def obter_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número.")

def main():
    print("Bem-vindo à Calculadora!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma operação: ").strip()

        if opcao == "0":
            print("Encerrando a calculadora. Até mais!")
            break
        elif opcao in ("1", "2", "3", "4"):
            a = obter_numero("Digite o primeiro número: ")
            b = obter_numero("Digite o segundo número: ")

            try:
                if opcao == "1":
                    resultado = somar(a, b)
                    print(f"Resultado: {a} + {b} = {resultado}")
                elif opcao == "2":
                    resultado = subtrair(a, b)
                    print(f"Resultado: {a} - {b} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicar(a, b)
                    print(f"Resultado: {a} × {b} = {resultado}")
                elif opcao == "4":
                    resultado = dividir(a, b)
                    print(f"Resultado: {a} ÷ {b} = {resultado:.4f}")
            except ValueError as e:
                print(e)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
