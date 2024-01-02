def calculadora():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair da calculadora")
        oper = int(input("Digite o número da operação desejada: "))

        if oper == 0:
            print("Saindo da calculadora.")
            break
        elif oper in range(1, 5):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if oper == 1:
                resultado = num1 + num2
            elif oper == 2:
                resultado = num1 - num2
            elif oper == 3:
                resultado = num1 * num2            
            elif oper == 4:
                #Verificando se o segundo número é zero evitando divisão por zero
                resultado = num1 / num2 if num2 != 0 else "Erro: número inválido, divisão por zero"            
                print(f"Resultado: {resultado}")
            else:
                print("Opção não existe. Escolha uma opção válida.")

                
                
if __name__ == "__main__":
                    calculadora()
