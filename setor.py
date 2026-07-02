
def cadastrar_setor(nome, localizacao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO setor (nome, localizacao)
    VALUES (%s, %s)
    """
    valores = (nome, localizacao)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Setor cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_setores():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT id_setor, nome, localizacao FROM setor"
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'ID':<5} | {'NOME DO SETOR':<25} | {'LOCALIZAÇÃO':<15}")
    print("-" * 50)
    for setor in dados:
        id_setor, nome, localizacao = setor
        print(f"{id_setor:<5} | {nome:<25} | {localizacao:<15}")
    
    print("\nConsulta de setores finalizada.")
    cursor.close()
    conexao.close()

def atualizar_setor(id_setor, novo_nome, nova_localizacao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE setor 
    SET nome = %s, localizacao = %s 
    WHERE id_setor = %s
    """
    valores = (novo_nome, nova_localizacao, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Setor ID {id_setor} atualizado com sucesso!")
    cursor.close()
    conexao.close()

def deletar_setor(id_setor):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM setor WHERE id_setor = %s"
    cursor.execute(sql, (id_setor,))
    conexao.commit()
    print(f"Setor ID {id_setor} deletado com sucesso.")
    cursor.close()
    conexao.close()
