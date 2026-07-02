
def cadastrar_inspecao(data_inspecao, resultado_inspecao, observacoes_tecnicas, id_ordem):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO controle_qualidade (data_inspecao, resultado_inspecao, observacoes_tecnicas, id_ordem)
    VALUES (%s, %s, %s, %s)
    """
    valores = (data_inspecao, resultado_inspecao, observacoes_tecnicas, id_ordem)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Laudo de controle de qualidade registrado!")
    cursor.close()
    conexao.close()

def listar_inspecoes():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT cq.id_qualidade, cq.data_inspecao, cq.id_ordem, cq.resultado_inspecao, cq.observacoes_tecnicas
    FROM controle_qualidade cq
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    print(f"\n{'LAUDO ID':<9} | {'DATA':<10} | {'OP ID':<6} | {'RESULTADO':<12} | {'OBSERVAÇÕES':<30}")
    print("-" * 75)
    for cq in dados:
        id_q, data, id_o, resultado, obs = cq
        obs_resumida = (obs[:27] + '...') if obs and len(obs) > 27 else (obs or '')
        print(f"{id_q:<9} | {str(data):<10} | {id_o:<6} | {resultado:<12} | {obs_resumida:<30}")

    print("\nConsulta de controle de qualidade finalizada.")
    cursor.close()
    conexao.close()

def atualizar_resultado_inspecao(id_qualidade, novo_resultado, novas_observacoes):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE controle_qualidade 
    SET resultado_inspecao = %s, observacoes_tecnicas = %s 
    WHERE id_qualidade = %s
    """
    valores = (novo_resultado, novas_observacoes, id_qualidade)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Inspeção ID {id_qualidade} alterada com sucesso.")
    cursor.close()
    conexao.close()

def deletar_inspecao(id_qualidade):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM controle_qualidade WHERE id_qualidade = %s"
    cursor.execute(sql, (id_qualidade,))
    conexao.commit()
    print(f"Registro de Inspeção ID {id_qualidade} deletado.")
    cursor.close()
    conexao.close()
