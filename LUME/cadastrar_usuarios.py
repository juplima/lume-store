import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "lume"
}

def criar_conexao():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print("❌ Erro de conexão:", e)
    return None

def cadastrar_usuario(nome, email, senha, tipo):
    conn = criar_conexao()
    if not conn:
        print("❌ Falha ao conectar no banco")
        return
    
    cursor = None
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, email, senha, tipo))
        conn.commit()
        print(f"✅ Usuário '{nome}' cadastrado com sucesso! ID:", cursor.lastrowid)
    except Error as e:
        print("❌ Erro ao inserir:", e)
    finally:
        if cursor:
            cursor.close()
        conn.close()

def main():
    print("=== Script iniciar cadastro ===")
    nome = input("Digite o nome do usuário: ").strip()
    email = input("Digite o email: ").strip()
    senha = input("Digite a senha: ").strip()
    tipo = input("Digite o tipo (ex: admin, cliente): ").strip()

    if not (nome and email and senha and tipo):
        print("❌ Campos vazios – operação cancelada.")
        return

    cadastrar_usuario(nome, email, senha, tipo)
    
print("SQL executado e commit realizado.")

if __name__ == "__main__":
    main()