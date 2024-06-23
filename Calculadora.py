import os

continuar = True
while continuar:
    print("======Bem Vindo a essa simples calculador=======")
    print("Qual operação matemática deseja fazer?")
    print(" 0 = Adição \n 1 = Subtração \n 2 = Multiplicação \n 3 = Divisão") 

    operacao = int(input())

    if operacao == 0:
        print("Digite o primeiro número: ")
        num1 = float(input())
        print("Digite o segundo número: ")
        num2 = float(input())
        total = num1 + num2
        print ("O valor da soma é {}".format(total))
        print ("Você deseja fazer mais cálculos ou deseja finalizar? 0 - Sim / 1 - Não")
        escolha = int(input())
        if escolha == 0:
            os.system('cls')
            continue
        elif escolha == 1:
            break
        else: 
            break
    elif operacao == 1:
        print("Digite o primeiro número: ")
        num1 = float(input())
        print("Digite o segundo número: ")
        num2 = float(input())
        total = num1 - num2
        print ("O valor da soma é {}".format(total))
        print ("Você deseja fazer mais cálculos ou deseja finalizar? 0 - Sim / 1 - Não")
        escolha = int(input())
        if escolha == 0:
            os.system('clear')
            continue
        elif escolha == 1:
            break
        else: 
            break
    elif operacao == 2:
        print("Digite o primeiro número: ")
        num1 = float(input())
        print("Digite o segundo número: ")
        num2 = float(input())
        total = num1 * num2
        print ("O valor da soma é {}".format(total))
        print ("Você deseja fazer mais cálculos ou deseja finalizar? 0 - Sim / 1 - Não")
        escolha = int(input())
        if escolha == 0:
            os.system('clear')
            continue
        elif escolha == 1:
            break
        else: 
            break
    elif operacao == 3:
        print("Digite o primeiro número: ")
        num1 = float(input())
        print("Digite o segundo número: ")
        num2 = float(input())
        total = num1 / num2
        print ("O valor da soma é {}".format(total))
        print ("Você deseja fazer mais cálculos ou deseja finalizar? 0 - Sim / 1 - Não")
        escolha = int(input())
        if escolha == 0:
            os.system('clear')
            continue
        elif escolha == 1:
            break
        else: 
            break
    else:
        break