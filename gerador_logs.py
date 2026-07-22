import psycopg2
from datetime import datetime
import random
import os
from dotenv import load_dotenv

# segurança

load_dotenv()

try:
    related = psycopg2.connect(
        host="localhost",
        port="5433",
        database="dw_logs",
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    
    cursor = related.cursor()
    print(" Conexão com o Postgres realizada com sucesso!\n")

    
    #  Geração de Logs aleatorios
   
    niveis_severidade = ["INFO", "WARNING", "ERROR"]
    mensagens_sistema = [
        "Transação processada com sucesso.",
        "Timeout de conexão com o servidor externo.",
        "Falha de autenticação: credenciais inválidas.",
        "Serviço reiniciado automaticamente.",
        "Permissão negada ao acessar o diretório base.",
        "Backup diário concluído."
    ]

    # Sorteia automaticamente
    nivel = random.choice(niveis_severidade)
    mensagem = random.choice(mensagens_sistema)
    timestamp = datetime.now()

    
    query_insercao = """
        INSERT INTO staging_logs (data_hora, nivel_alerta, mensagem_log)
        VALUES (%s, %s, %s);
    """
    
    # Executa e salva no banco
    cursor.execute(query_insercao, (timestamp, nivel, mensagem))
    related.commit()
    
    print(f" Log inserido com sucesso: [{nivel}] {mensagem}")

except Exception as erro:
    print(f" Ocorreu um erro no pipeline: {erro}")

finally:
  
    #  Conclusão 
    if 'related' in locals() and related:
        cursor.close()
        related.close()
        print("\n Conexão com o banco encerrada com segurança.")