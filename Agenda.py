AGENDA = {}

AGENDA["guilherme"] = {
    "telefone": "99999910",
    "email": "guilherme@bol.com",
    "endereco": "av.1"
}

AGENDA["vania"] = {
    "telefone": "99999920",
    "email": "vania@bol.com",
    "endereco": "av.2"
}

AGENDA["lucas"] = {
    "telefone": "99999930",
    "email": "lucas@bol.com",
    "endereco": "av.3"
}

def mostrar_contato():
    for contato in AGENDA:
        print(contato)

def buscar_contato(contato):
    print("nome: ", contato)
    print("telefone: ", AGENDA[contato]["telefone"])
    print("email: ", AGENDA[contato]["email"])
    print("endereço: ", AGENDA[contato]["endereco"])
    print("----------------------------------------------")

def incluir_ou_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    print(">>>>contato {} adicionado/editado com sucesso a lista".format(contato))
    print("----------------------------------------------")

def excluindo_contato(contato):
    AGENDA.pop(contato)
    print(">>>> o contato {} foi excluido com sucesso".format(contato))
    print("----------------------------------------------")

def imprimir_menu():
    print("----------------------------------------------")
    print("1 - mostrar contato")
    print("2 - buscar contato")
    print("3 - incluir contato")
    print("4 - editar contato")
    print("5 - excluir contato")
    print("0 - fechar agenda")
    print("----------------------------------------------")

while True:
    imprimir_menu()
    opcao = input("selecione uma opção: ")

    if opcao == '1':
        mostrar_contato()
    elif opcao == '2':
        contato = input("digite o nome do contato:")
        try:
            buscar_contato(contato)
        except:
            print("este contato nao esta na agenda!")

    elif opcao == '3' or opcao == '4':
        contato = input("digite o nome do contato: ")
        telefone = input("digite o telefone: ")
        email = input("digite o email: ")
        endereco = input("digite o endereço: ")
        incluir_ou_editar_contato(contato, telefone, email, endereco)

    elif opcao == '5':
        contato = input("digite o nome do contato: ")
        excluindo_contato(contato)

    elif opcao == '0':
        print(">>>>encerrando agenda<<<<")
        break
    else:
        print("opção invalida")
