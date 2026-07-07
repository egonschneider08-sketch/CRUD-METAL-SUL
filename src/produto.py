
def cadastrar_produto(nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO produto (nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Produto cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT p.id_produto, p.nome, p.preco_fabricacao, p.quantidade_estoque, c.nome
    FROM produto p
    JOIN categoria_produto c ON p.id_categoria = c.id_categoria
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'ID':<5} | {'PRODUTO':<25} | {'PREÇO FAB.':<12} | {'ESTOQUE':<8} | {'CATEGORIA':<20}")
    print("-" * 78)
    for prod in dados:
        id_prod, nome, preco, estoque, categoria = prod
        print(f"{id_prod:<5} | {nome:<25} | R$ {preco:<9.2f} | {estoque:<8} | {categoria:<20}")

    print("\nConsulta de produtos finalizada.")
    cursor.close()
    conexao.close()

def atualizar_estoque_preco(id_produto, novo_preco, novo_estoque):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE produto 
    SET preco_fabricacao = %s, quantidade_estoque = %s 
    WHERE id_produto = %s
    """
    valores = (novo_preco, novo_estoque, id_produto)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Estoque e preço do produto ID {id_produto} atualizados.")
    cursor.close()
    conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM produto WHERE id_produto = %s"
    cursor.execute(sql, (id_produto,))
    conexao.commit()
    print(f"Produto ID {id_produto} removido do catálogo.")
    cursor.close()
    conexao.close()
