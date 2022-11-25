def enumero(n1):
    try:
        int(n1)
    except ValueError:
        return False
    return True


class Profissional:
    def __init__(self):
        self.__id = 0
        self.__nome = ""
        self.__especialidade = ""
        self.__sala = ""

    def get_id(self):
        return self.__id

    def set_id(self, x):
        self.__id = x

    def get_nome(self):
        return self.__nome

    def set_nome(self, x):
        self.__nome = x

    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, x):
        self.__especialidade = x

    def get_sala(self):
        return self.__sala

    def set_sala(self, x):
        self.__sala = x


class Visitante:
    def __init__(self):
        self.__id = 0
        self.__nome = ""
        self.__documento = ""

    def get_id(self):
        return self.__id

    def set_id(self, x):
        self.__id = x

    def get_nome(self):
        return self.__nome

    def set_nome(self, x):
        self.__nome = x

    def get_documento(self):
        return self.__documento

    def set_documento(self, x):
        self.__documento = x


class Visita:
    def __init__(self):
        self.visitante = Visitante()
        self.profissional = Profissional()
        self.data_visita = ""


def menu():
    escolha = ""
    lista_Profissionais = []
    lista_visitantes = []
    lista_visitas = []
    i = 0
    j = 0
    while escolha != "0":
        escolha = ""
        while not enumero(escolha):
            print("""
                            ======================
                            MENU
                            ======================
                            1- Cadastrar Profissional
                            2- Localizar Profissional
                            3- Cadastrar Visitante
                            4- Registrar Visita
                            5- Relatório de Conferência
                            0- Sair
                            Escolha:
                            """)

            escolha = input(">>>>")

            if enumero(escolha):
                if escolha == '1':
                    primeiroDado = True
                    p = Profissional()
                    if lista_Profissionais:
                        primeiroDado = False
                    if not primeiroDado:
                        i = i + 1
                        p.set_nome(input("Digite o nome do profissional: "))
                        p.set_especialidade(input("Digite a especialidade do profissional: "))
                        p.set_sala(input("Digite a sala do profissional: "))
                        p.set_id(i)
                        lista_Profissionais.append(p)
                    else:
                        i = 1
                        p.set_nome(input("Digite o nome do profissional: "))
                        p.set_especialidade(input("Digite a especialidade do profissional: "))
                        p.set_sala(input("Digite a sala do profissional: "))
                        lista_Profissionais.append(p)
                        p.set_id(i)

                if escolha == '2':
                    encontrado = False
                    lista_Profissionais_encontrados = []
                    localizar = ""
                    while not enumero(localizar):
                        localizar = input(
                            """
                            # 1- Localizar pelo Nome
                            # 2- Localizar pela Profissão
                            """
                        ).upper()
                        if enumero(localizar):
                            if int(localizar) < 3:
                                if localizar == '1':
                                    nome = input("Digite o Nome para pesquisar: ")
                                    print("------------------------------")
                                    for p in lista_Profissionais:
                                        if p.get_nome().upper() == nome.upper():
                                            lista_Profissionais_encontrados.append(p)
                                            encontrado = True
                                    if not encontrado:
                                        print("Nenhum profissional encontrado!")
                                        print("------------------------------")

                                if localizar == '2':
                                    especialidade = input("Digite a Especialidade para pesquisar: ")
                                    print("------------------------------")
                                    for p in lista_Profissionais:
                                        if p.get_especialidade().upper() == especialidade.upper():
                                            lista_Profissionais_encontrados.append(p)
                                            encontrado = True
                                    if not encontrado:
                                        print("Nenhum profissional encontrado!")
                                        print("------------------------------")

                                for pe in lista_Profissionais_encontrados:
                                    print("Nome: ", pe.get_nome(), " Sala: ", pe.get_sala())
                                    print("------------------------------")
                            else:
                                print("Não é uma opção valida")
                                print("------------------------------")
                        else:
                            print("Não é uma opção valida")
                            print("------------------------------")

                if escolha == '3':
                    primeiroDado = True
                    v = Visitante()
                    if lista_visitantes:
                        primeiroDado = False
                    if not primeiroDado:
                        j = j + 1
                        v.set_nome(input("Digite o nome do Visitante: "))
                        v.set_documento(input("Digite o Documento do Visitante: "))
                        v.set_id(j)
                        lista_visitantes.append(v)
                    else:
                        j = 1
                        v.set_nome(input("Digite o nome do Visitante: "))
                        v.set_documento(input("Digite o Documento do Visitante: "))
                        v.set_id(j)
                        lista_visitantes.append(v)

                if escolha == '4':
                    visitante_encontrado = False
                    profissional_encontrado = False
                    visita = Visita()
                    print("Visitantes: ")
                    print("==============================")
                    for v in lista_visitantes:
                        print("Nº Cadastro: ", v.get_id(), "Nome: ", v.get_nome(), " Documento: ", v.get_documento())
                        print("------------------------------")

                    print("Profissional: ")
                    print("==============================")
                    for p in lista_Profissionais:
                        print("Nº Cadastro: ", p.get_id(), "Nome: ", p.get_nome(), " Especialidade: ", p.get_especialidade(),
                              " Sala: ", p.get_sala())
                        print("------------------------------")

                    id_visitante = input("Digite o Nº do Cadastro do Visitante: ")
                    print("------------------------------")

                    if enumero(id_visitante):
                        for v in lista_visitantes:
                            if int(id_visitante) == v.get_id():
                                visita.visitante.set_id(v.get_id())
                                visita.visitante.set_nome(v.get_nome())
                                visita.visitante.set_documento(v.get_documento())
                                visitante_encontrado = True
                                break
                    else:
                        print("O dado digitado não é um número! ")
                        print("------------------------------")

                    if visitante_encontrado:
                        id_profissional = input("Digite o Nº do Cadastro do Profissional: ")
                        print("------------------------------")
                        if enumero(id_profissional):
                            for p in lista_Profissionais:
                                if int(id_profissional) == p.get_id():
                                    visita.profissional.set_id(p.get_id())
                                    visita.profissional.set_nome(p.get_nome())
                                    visita.profissional.set_especialidade(p.get_especialidade())
                                    visita.profissional.set_sala(p.get_sala())
                                    profissional_encontrado = True
                                    break
                        else:
                            print("O dado digitado não é um número! ")
                            print("------------------------------")
                    else:
                        print("Nenhum Visitante encontrado!")
                        print("------------------------------")

                    if profissional_encontrado:
                        visita.data_visita = input("Digite a data: ")
                        print("------------------------------")
                        lista_visitas.append(visita)
                    else:
                        print("Nenhum Profissional encontrado!")
                        print("------------------------------")

                if escolha == '5':
                    profissional_escolhido = Profissional()
                    print("Profissional: ")
                    print("==============================")
                    for p in lista_Profissionais:
                        print("Nº Cadastro: ", p.get_id(), "Nome: ", p.get_nome(), " Especialidade: ", p.get_especialidade(), " Sala: ", p.get_sala())
                        print("------------------------------")
                    profissional_id = input("Digite o Nº Cadastro do Profissional: ")
                    print("------------------------------")

                    if enumero(profissional_id):
                        for p in lista_Profissionais:
                            if p.get_id() == int(profissional_id):
                                profissional_escolhido.set_id(p.get_id())
                                profissional_escolhido.set_nome(p.get_nome())
                                profissional_escolhido.set_sala(p.get_sala())
                                profissional_escolhido.set_especialidade(p.get_especialidade())
                                break

                        print("Profissional: ", profissional_escolhido.get_nome())
                        for visita in lista_visitas:
                            if int(profissional_escolhido.get_id()) == int(visita.profissional.get_id()):
                                print("Visitante: ", visita.visitante.get_nome(), " Data da Visita: ", visita.data_visita)
                                print("------------------------------")
                    else:
                        print("O dado digitado não é um número! ")
                        print("------------------------------")

            else:
                print("Não é uma opção valida")
                print("------------------------------")


menu()
