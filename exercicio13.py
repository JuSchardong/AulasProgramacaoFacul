fim = "x"
while(fim.upper() != "S"):
    v1 = input("Digite um numero inteiro: ")
    def isnumber (v1):
        try:
            int(v1)
        except ValueError:
            print("NÃO É UM NUMERO INTEIRO OU NÃO É UM NUMERO") 
            return False
        return True


    if(isnumber(v1)):
        if(int(v1) <= 10):
            print("MENSAGEM 1")
        elif(int(v1) > 10 and int(v1) <= 100):
            print("MENSAGEM 2")
        elif(int(v1) > 100):
            print("MENSAGEM 3")
    while(fim.upper() != "S" and fim.upper() != "N"):
        fim = input("Deseja finalizar? Digite 'S' para sim ou 'N' para não: ")

    