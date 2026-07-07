import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        # Tenta criar a conexão com o banco de dados LOCAL
        conexao = mysql.connector.connect(
            host='localhost',          # Aponta para a sua própria máquina (ou '127.0.0.1')
            user='root',               # Usuário padrão da maioria das instalações locais
            password='root', # Substitua pela senha do seu MySQL local
            database='metalsul_industrial',      # Nome do banco que você criou localmente
            port=3306                  # Porta padrão do MySQL local (geralmente 3306)
        )
        
        # Verifica se a conexão foi bem-sucedida
        if conexao.is_connected():
            print("🟢 Conectado ao banco de dados LOCAL com sucesso!")
            return conexao

    except Error as erro:
        print(f"🔴 Erro ao conectar ao MySQL local: {erro}")
        return None

conectar()