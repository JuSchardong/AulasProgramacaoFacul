fim = "x"


def enumero(v1):
    try:
        int(v1)
    except ValueError:
        return False
    return True


while fim.upper() != "S":
    v1 = input("Digite um numero inteiro: ")
    if enumero(v1):
        if int(v1) <= 10:
            print("MENSAGEM 1")
        elif 10 < int(v1) <= 100:
            print("MENSAGEM 2")
        elif int(v1) > 100:
            print("MENSAGEM 3")
    else:
        print("NÃO É UM NUMERO INTEIRO OU NÃO É UM NUMERO")

    fim = input("Deseja finalizar? Digite 'S' para sim ou 'N' para não: ")

    while fim.upper() != "S" and fim.upper() != "N":
        fim = input("Deseja finalizar? Digite 'S' para sim ou 'N' para não: ")
