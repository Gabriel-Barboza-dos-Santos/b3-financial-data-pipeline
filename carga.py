##Criação do codigo para load dos dados.

import pandas as pd
import sqlite3

print("Iniciando a carga dos dados no Banco de Dados")

#Ler os dados tratados
df = pd.read_csv("dados_tratados_b3.csv")

#Conectar (ou criar) o banco de dados SQLite local 'b3_data.db'
conexao = sqlite3.connect("b3_data.db")

#Salvar o DataFrame no banco de dados na tabela 'cotacoes_b3'
df.to_sql("cotacoes_b3", conexao, if_exists="replace", index=False)

print("Dados carregados com sucesso na tabela 'cotacoes_b3'!")

#Consulta de teste por ativo
print("\nTestando consulta SQL no banco (Última cotação por ativo):")
query = """
SELECT data, ticker, preco_fechamento, variacao_diaria_pct 
FROM cotacoes_b3 
ORDER BY data DESC, ticker ASC
LIMIT 10;
"""
df_resultado = pd.read_sql_query(query, conexao)
print(df_resultado)

conexao.close()