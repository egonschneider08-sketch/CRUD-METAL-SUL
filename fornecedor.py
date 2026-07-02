
def cadastrar_fornecedor(razao_social, cnpj, telefone, cidade):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO fornecedor (razao_social, cnpj, telefone, cidade)
    VALUES (%s, %s, %s, %s)
    """
    valores = (razao_social, cnpj, telefone, cidade)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Fornecedor cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_fornecedores():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT id_fornecedor, razao_social, cnpj, cidade FROM fornecedor"
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'ID':<5} | {'RAZÃO SOCIAL':<25} | {'CNPJ':<16} | {'CIDADE':<15}")
    print("-" * 68)
    for forn in dados:
        id_forn, razao, cnpj, cidade = forn
        print(f"{id_forn:<5} | {razao:<25} | {cnpj:<16} | {cidade:<15}")

    print("\nConsulta de fornecedores finalizada.")
    cursor.close()
    conexao.close()

def atualizar_fornecedor(id_fornecedor, novo_telefone, nova_cidade):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE fornecedor 
    SET telefone = %s, cidade = %s 
    WHERE id_fornecedor = %s
    """
    valores = (novo_telefone, nova_cidade, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Contato do Fornecedor ID {id_fornecedor} atualizado.")
    cursor.close()
    conexao.close()

def deletar_fornecedor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM fornecedor WHERE id_fornecedor = %s"
    cursor.execute(sql, (id_fornecedor,))
    conexao.commit()
    print(f"Fornecedor ID {id_fornecedor} removido.")
    cursor.close()
    conexao.close()


