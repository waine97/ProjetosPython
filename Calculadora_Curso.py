import os

print ("==========")
operacao = {
    "+":"Soma",
    "-":"Subtração",
    "*":"Multuplicação",
    "/":"Divisão",
    "^":"Exponenciação",
}

while True:
    os.system("cls")
    i = 0
    for op, name in operacao.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operação que deseja realizar: ")
    op = int(input())
    op_string = list (operacao.keys()) [op]

    print("")
    print("{} escolhida".format(op_string))
    print("")
    print("Qual o primeiro valor?")
    v1 = float(input())
    print("Qual o segundo valor?")
    v2 = float(input())

    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2

    print("")
    print("{} {} {} = {}".format(v1, op_string, v2, result))
    print ("==========")

    print ("Deseja fazer mais alguma operação? (Digite 1 para sair)")
    comando = int(input())
    if comando == 1:
        break
