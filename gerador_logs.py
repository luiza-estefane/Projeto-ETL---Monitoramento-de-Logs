import psycopg2
from datetime import datetime
import random
import os
import time
from dotenv import load_dotenv

#====================================================
# segurança 
#====================================================

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
    print("Conexão com o Postgres realizada com sucesso!\n")

    #====================================================
    # 3. Geração de Logs Dinâmicos
    #====================================================
    # Listas para simular o comportamento de um sistema 
    niveis_severidade = ["INFO", "WARNING", "ERROR"]
    mensagens_sistema = [
        "Transação processada com sucesso.",
        "Timeout de conexão com o servidor externo.",
        "Falha de autenticação: credenciais inválidas.",
        "Serviço reiniciado automaticamente.",
        "Pico de uso de CPU detectado.",
        "Permissão negada ao acessar o diretório base.",
        "Backup diário concluído."
    ]

    # sorteia automaticamente
    nivel = random.choice(niveis_severidade)
    mensagem = random.choice(mensagens_sistema)
    timestamp = datetime.now()

 
    # 4. Inserção na Staging Area
 
    # Ajuste o nome da tabela (staging_logs) e colunas conforme o seu banco criado no Docker
    query_insercao = """
        INSERT INTO staging_logs (data_hora, nivel_alerta, mensagem_log)
        VALUES (%s, %s, %s);
    """
    
    # Executa e salva no banco
    cursor.execute(query_insercao, (timestamp, nivel, mensagem))
    related.commit()
    
    print(f"Log inserido com sucesso: [{nivel}] {mensagem}")

except Exception as erro:
    print(f" Ocorreu um erro no pipeline: {erro}")

finally:
   
    # 5. conclusão
  
    if 'related' in locals() and related:
        cursor.close()
        related.close()
        print("\nConexão com o banco encerrada com segurança.")
