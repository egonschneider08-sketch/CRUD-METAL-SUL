
def cadastrar_categoria(nome, descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO categoria_produto (nome, descricao)
    VALUES (%s, %s)
    """
    valores = (nome, descricao)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Categoria de produto cadastrada!")
    cursor.close()
    conexao.close()

def listar_categorias():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT id_categoria, nome, descricao FROM categoria_produto"
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'ID':<5} | {'CATEGORIA':<25} | {'DESCRIÇÃO':<40}")
    print("-" * 75)
    for cat in dados:
        id_cat, nome, descricao = cat
        desc_resumida = (descricao[:37] + '...') if descricao and len(descricao) > 37 else (descricao or '')
        print(f"{id_cat:<5} | {nome:<25} | {desc_resumida:<40}")

    print("\nConsulta de categorias finalizada.")
    cursor.close()
    conexao.close()

def atualizar_categoria(id_categoria, novo_nome, nova_descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE categoria_produto 
    SET nome = %s, descricao = %s 
    WHERE id_categoria = %s
    """
    valores = (novo_nome, nova_descricao, id_categoria)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Categoria ID {id_categoria} atualizada com sucesso.")
    cursor.close()
    conexao.close()

def deletar_categoria(id_categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM categoria_produto WHERE id_categoria = %s"
    cursor.execute(sql, (id_categoria,))
    conexao.commit()
    print(f"Categoria ID {id_categoria} deletada.")
    cursor.close()
    conexao.close()

