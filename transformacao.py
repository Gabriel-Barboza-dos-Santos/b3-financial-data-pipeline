##

import pandas as pd

print("Iniciando a transformação e limpeza dos dados")

#Carregar os dados brutos
df = pd.read_csv("dados_brutos_b3.csv")

#Renomear colunas para o padrão de banco de dados (snake_case)
df.rename(columns={
    'Date': 'data',
    'Open': 'preco_abertura',
    'High': 'preco_maximo',
    'Low': 'preco_minimo',
    'Close': 'preco_fechamento',
    'Volume': 'volume_negociado',
    'Dividends': 'dividendos',
    'Stock Splits': 'desdobramentos'
}, inplace=True)

#Tratar a coluna de data (remover fuso horário)
df['data'] = pd.to_datetime(df['data']).dt.tz_localize(None).dt.date

#Arredondar os valores numéricos para 2 casas decimais
colunas_preco = ['preco_abertura', 'preco_maximo', 'preco_minimo', 'preco_fechamento']
df[colunas_preco] = df[colunas_preco].round(2)

#Criar a coluna calculada para variação percentual diária (%)
df['variacao_diaria_pct'] = ((df['preco_fechamento'] - df['preco_abertura']) / df['preco_abertura'] * 100).round(2)

#Reorganizar as colunas mantendo 'ticker' e 'data' no início
colunas_ordenadas = ['data', 'ticker', 'preco_abertura', 'preco_maximo', 'preco_minimo', 'preco_fechamento', 'variacao_diaria_pct', 'volume_negociado', 'dividendos', 'desdobramentos']
df = df[colunas_ordenadas]

#Exibir os primeiros registros limpos
print("\nPrimeiras linhas dos dados transformados:")
print(df[['data', 'ticker', 'preco_fechamento', 'variacao_diaria_pct']].head())

#Salvar os dados transformados
df.to_csv("dados_tratados_b3.csv", index=False)
print("\nArquivo 'dados_tratados_b3.csv' gerado com sucesso!")