
def cadastrar_ordem_producao(data_producao, quantidade_produzida, status_producao, tempo_estimado, tempo_real, id_produto, id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO ordem_producao (data_producao, quantidade_produzida, status_producao, tempo_estimado, tempo_real, id_produto, id_funcionario)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (data_producao, quantidade_produzida, status_producao, tempo_estimado, tempo_real, id_produto, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Ordem de Produção aberta com sucesso!")
    cursor.close()
    conexao.close()

def listar_ordens_producao():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT o.id_ordem, o.data_producao, p.nome, o.quantidade_produzida, o.status_producao
    FROM ordem_producao o
    JOIN produto p ON o.id_produto = p.id_produto
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'OP ID':<6} | {'DATA':<10} | {'PRODUTO':<25} | {'QTD':<6} | {'STATUS':<15}")
    print("-" * 71)
    for ordem in dados:
        id_ordem, data, produto, qtd, status = ordem
        print(f"{id_ordem:<6} | {str(data):<10} | {produto:<25} | {qtd:<6} | {status:<15}")

    print("\nConsulta de Ordens de Produção finalizada.")
    cursor.close()
    conexao.close()

def atualizar_status_ordem(id_ordem, novo_status, tempo_real):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE ordem_producao 
    SET status_producao = %s, tempo_real = %s 
    WHERE id_ordem = %s
    """
    valores = (novo_status, tempo_real, id_ordem)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Status da OP ID {id_ordem} atualizado para: {novo_status}.")
    cursor.close()
    conexao.close()

def deletar_ordem_producao(id_ordem):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM ordem_producao WHERE id_ordem = %s"
    cursor.execute(sql, (id_ordem,))
    conexao.commit()
    print(f"Ordem de Produção ID {id_ordem} excluída.")
    cursor.close()
    conexao.close()

