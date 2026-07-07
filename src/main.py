from database import conectar

from funcionario import (
    listar_funcionarios, cadastrar_funcionario, atualizar_cargo_salario, deletar_funcionario
)
from fornecedor import (
    listar_fornecedores, cadastrar_fornecedor, atualizar_fornecedor, deletar_fornecedor
)
from produto import (
    listar_produtos, cadastrar_produto, atualizar_estoque_preco, deletar_produto
)
from setor import (
    listar_setores, cadastrar_setor, atualizar_setor, deletar_setor
)

while True:
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Gerenciar Funcionários")
    print("2 - Gerenciar Fornecedores")
    print("3 - Gerenciar Produtos")
    print("4 - Gerenciar Setores")
    print("0 - Sair")

    opcao_menu = input("\nEscolha uma tabela/opção: ")

    if opcao_menu == "0":
        print("bye bye")
        break

    elif opcao_menu == "1":
        while True:
            print("\n====== GERENCIAR FUNCIONÁRIOS ======")
            print("1 - Listar funcionários")
            print("2 - Cadastrar funcionário")
            print("3 - Atualizar cargo/salário")
            print("4 - Remover funcionário")
            print("0 - Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                listar_funcionarios()
            elif opcao == "2":
                nome = input("Nome: ")
                cpf = input("CPF (11 dígitos): ")
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))
                data_admissao = input("Data de admissão (AAAA-MM-DD): ")
                id_setor = int(input("ID setor: "))
                cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor)
                print("Funcionário cadastrado com sucesso!")
            elif opcao == "3":
                id_funcionario = int(input("ID funcionário: "))
                novo_cargo = input("Novo Cargo: ")
                novo_salario = float(input("Novo Salário: "))
                atualizar_cargo_salario(id_funcionario, novo_cargo, novo_salario)
            elif opcao == "4":
                id_funcionario = int(input("ID funcionário: "))
                deletar_funcionario(id_funcionario)
            elif opcao == "0":
                break
            else:
                print("Tente novamente!!!!!!!!!!!!!!")

    elif opcao_menu == "2":
        while True:
            print("\n====== GERENCIAR FORNECEDORES ======")
            print("1 - Listar fornecedores")
            print("2 - Cadastrar fornecedor")
            print("3 - Atualizar contato (Tel/Cidade)")
            print("4 - Remover fornecedor")
            print("0 - Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                listar_fornecedores()
            elif opcao == "2":
                razao_social = input("Razão Social: ")
                cnpj = input("CNPJ (14 dígitos): ")
                telefone = input("Telefone: ")
                cidade = input("Cidade: ")
                cadastrar_fornecedor(razao_social, cnpj, telefone, cidade)
                print("Fornecedor cadastrado com sucesso!")
            elif opcao == "3":
                id_fornecedor = int(input("ID fornecedor: "))
                novo_telefone = input("Novo Telefone: ")
                nova_cidade = input("Nova Cidade: ")
                atualizar_fornecedor(id_fornecedor, novo_telefone, nova_cidade)
            elif opcao == "4":
                id_fornecedor = int(input("ID fornecedor: "))
                deletar_fornecedor(id_fornecedor)
            elif opcao == "0":
                break
            else:
                print("Tente novamente!!!!!!!!!!!!!!")

    elif opcao_menu == "3":
        while True:
            print("\n====== GERENCIAR PRODUTOS ======")
            print("1 - Listar produtos")
            print("2 - Cadastrar produto")
            print("3 - Atualizar preço/estoque")
            print("4 - Remover produto")
            print("0 - Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                listar_produtos()
            elif opcao == "2":
                nome = input("Nome do Produto: ")
                descricao = input("Descrição: ")
                preco_fabricacao = float(input("Preço de Fabricação: "))
                quantidade_estoque = int(input("Quantidade em Estoque: "))
                id_categoria = int(input("ID Categoria: "))
                id_fornecedor = int(input("ID Fornecedor: "))
                cadastrar_produto(nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor)
                print("Produto cadastrado com sucesso!")
            elif opcao == "3":
                id_produto = int(input("ID produto: "))
                novo_preco = float(input("Novo Preço: "))
                novo_estoque = int(input("Novo Estoque: "))
                atualizar_estoque_preco(id_produto, novo_preco, novo_estoque)
            elif opcao == "4":
                id_produto = int(input("ID produto: "))
                deletar_produto(id_produto)
            elif opcao == "0":
                break
            else:
                print("Tente novamente!!!!!!!!!!!!!!")

    elif opcao_menu == "4":
        while True:
            print("\n====== GERENCIAR SETORES ======")
            print("1 - Listar setores")
            print("2 - Cadastrar setor")
            print("3 - Atualizar setor")
            print("4 - Remover setor")
            print("0 - Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                listar_setores()
            elif opcao == "2":
                nome = input("Nome do Setor: ")
                localizacao = input("Localização (Bloco): ")
                cadastrar_setor(nome, localizacao)
                print("Setor cadastrado com sucesso!")
            elif opcao == "3":
                id_setor = int(input("ID setor: "))
                novo_nome = input("Novo Nome: ")
                nova_localizacao = input("Nova Localização: ")
                atualizar_setor(id_setor, novo_nome, nova_localizacao)
            elif opcao == "4":
                id_setor = int(input("ID setor: "))
                deletar_setor(id_setor)
            elif opcao == "0":
                break
            else:
                print("Tente novamente!!!!!!!!!!!!!!")

    else:
        print("Tente novamente!!!!!!!!!!!!!!")