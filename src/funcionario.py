
def cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO funcionario (nome, cpf, cargo, salario, data_admissao, id_setor)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (nome, cpf, cargo, salario, data_admissao, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Funcionário cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT f.id_funcionario, f.nome, f.cargo, s.nome AS Setor
    FROM funcionario f
    JOIN setor s ON f.id_setor = s.id_setor
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'ID':<5} | {'NOME':<18} | {'CARGO':<25} | {'SETOR':<15}")
    print("-" * 70)
    for funcionario in dados:
        id_func, nome, cargo, setor = funcionario
        print(f"{id_func:<5} | {nome:<18} | {cargo:<25} | {setor:<15}")

    print("\nConsulta de funcionários finalizada.")
    cursor.close()
    conexao.close()

def atualizar_cargo_salario(id_funcionario, novo_cargo, novo_salario):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE funcionario 
    SET cargo = %s, salario = %s 
    WHERE id_funcionario = %s
    """
    valores = (novo_cargo, novo_salario, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Dados profissionais do funcionário ID {id_funcionario} atualizados!")
    cursor.close()
    conexao.close()

def deletar_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(sql, (id_funcionario,))
    conexao.commit()
    print(f"Funcionário ID {id_funcionario} deletado com sucesso.")
    cursor.close()
    conexao.close()
