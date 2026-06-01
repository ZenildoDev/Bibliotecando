# BOOKCONTROL - SISTEMA DE BIBLIOTECA

# Usando o módulo datetime para importar a classe datetime e timedelta
from datetime import datetime, timedelta

# Criação das duas listas principais
livros = []
usuarios = []

# Função estética
def linha():
    print("-" * 50)

# Função responsável para Cadastrar livros
def cadastrar_livro():
    linha()
    print("CADASTRAR LIVRO")

    nome = input("Nome do livro: ")
    autor = input("Autor: ")

    #Dicionário variável que guarda as informações chave:valor
    livro = {
        "nome": nome,
        "autor": autor,
        "status": "Disponível",
        "usuario": "",
        "data_emprestimo": None
    }
    #Append guarda informações dentro de uma lista
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Cadastrar usuário
def cadastrar_usuario():
    linha()
    print("CADASTRAR USUÁRIO")

    nome = input("Nome do usuário: ").lower()
    usuarios.append(nome)

    print("Usuário cadastrado com sucesso!")

# Listar livros
def listar_livros():
    linha()
    print("LISTA DE LIVROS")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    #Enumerate vai númerar cada item do for e armazenar no i
    for i, livro in enumerate(livros):
        if livro["data_emprestimo"]:
            #strftime serve para formatar datas
            data = livro["data_emprestimo"].strftime("%d/%m/%Y")
        else:
            data = "-"

        print(f"{i+1}. {livro['nome']} - {livro['autor']} - {livro['status']} - {livro['usuario']} - {data}")

# Emprestar livro
def emprestar_livro():
    linha()
    print("EMPRÉSTIMO DE LIVRO")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    usuario = input("Nome do usuário: ").lower()

    if usuario not in usuarios:
        print("Usuário não cadastrado.")
        return

    listar_livros()

    escolha = int(input("Número do livro: ")) - 1

    if escolha < 0 or escolha >= len(livros):
        print("Livro inválido.")
        return

    livro = livros[escolha]

    if livro["status"] == "Emprestado":
        print("Livro já emprestado.")
    else:
        livro["status"] = "Emprestado"
        livro["usuario"] = usuario

        #Data e horário atual
        livro["data_emprestimo"] = datetime.now()

        print("Livro emprestado com sucesso!")


        prazo = livro["data_emprestimo"] + timedelta(days=7)
        print("Devolver até:", prazo.strftime("%d/%m/%Y"))

# Devolver livro
def devolver_livro():
    linha()
    print("DEVOLUÇÃO DE LIVRO")

    listar_livros()

    escolha = int(input("Número do livro: ")) - 1

    if escolha < 0 or escolha >= len(livros):
        print("Livro inválido.")
        return

    livro = livros[escolha]

    if livro["status"] == "Disponível":
        print("Esse livro não está emprestado.")
    else:
        data_emprestimo = livro["data_emprestimo"]
        hoje = datetime.now()

        dias = (hoje - data_emprestimo).days

        if dias > 7:
            print(f"Livro devolvido com atraso de {dias - 7} dias.")
        else:
            print("Livro devolvido no prazo.")

        livro["status"] = "Disponível"
        livro["usuario"] = ""
        livro["data_emprestimo"] = None

        print("Devolução realizada com sucesso!")

# Buscar livro
def buscar_livro():
    linha()
    print("BUSCAR LIVRO")

    busca = input("Digite nome do livro: ").lower()

    encontrado = False

    for livro in livros:
        if busca in livro["nome"].lower():
            print(f"{livro['nome']} - {livro['autor']} - {livro['status']}")
            encontrado = True

    if not encontrado:
        print("Livro não encontrado.")

# Livros atrasados
def livros_atrasados():
    linha()
    print("LIVROS ATRASADOS")

    encontrou = False

    for livro in livros:
        if livro["status"] == "Emprestado" and livro["data_emprestimo"]:
            dias = (datetime.now() - livro["data_emprestimo"]).days

            if dias > 7:
                print(f"{livro['nome']} - Usuário: {livro['usuario']} - {dias-7} dias de atraso")
                encontrou = True

    if not encontrou:
        print("Nenhum livro atrasado.")

# MENU
while True:
    linha()
    print("BOOKCONTROL - SISTEMA DE BIBLIOTECA")
    linha()

    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Usuário")
    print("3 - Listar Livros")
    print("4 - Emprestar Livro")
    print("5 - Devolver Livro")
    print("6 - Buscar Livro")
    print("7 - Livros Atrasados")
    print("8 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        cadastrar_livro()

    elif op == "2":
        cadastrar_usuario()

    elif op == "3":
        listar_livros()

    elif op == "4":
        emprestar_livro()

    elif op == "5":
        devolver_livro()

    elif op == "6":
        buscar_livro()

    elif op == "7":
        livros_atrasados()

    elif op == "8":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")