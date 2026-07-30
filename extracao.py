##Criação do codigo para extração dos dados da b3.

import os
import pandas as pd
import yfinance as yf

print("Extraindo dados da B3")

#Carrega os tickers do arquivo tickers.txt
if not os.path.exists("tickers.txt"):
    print("Erro: O arquivo 'tickers.txt' não foi achado")
    exit(1)

with open("tickers.txt", "r") as f:
    tickers = [linha.strip() for linha in f if linha.strip() and not linha.startswith("#")]

print(f"Lista de ativos extraidos ({len(tickers)} ativos): {', '.join(tickers)}")

df_list = []

#Iterar sobre cada ativo para baixar o histórico
for ticker in tickers:
    print(f"Baixando dados de {ticker}")
    try:
        ativo = yf.Ticker(ticker)
        df_temp = ativo.history(period="1mo")
        
        if not df_temp.empty:
            #Adiciona a coluna com o nome do ativo limpo sem o sa (ex: PETR4)
            df_temp["ticker"] = ticker.replace(".SA", "")
            df_list.append(df_temp)
        else:
            print(f"Nenhum dado encontrado para {ticker}.")
    except Exception as e:
        print(f"Erro ao baixar {ticker}: {e}")

#Unir todos os dados em um único DataFrame
if df_list:
    df_final = pd.concat(df_list).reset_index()
    
    #Exibir primeiras linhas
    print("\nPrimeiras linhas dos dados extraídos:")
    print(df_final[['Date', 'ticker', 'Open', 'Close']].head())

    #Salvar no arquivo bruto
    df_final.to_csv("dados_brutos_b3.csv", index=False)
    print("\nDados brutos salvos com sucesso no arquivo 'dados_brutos_b3.csv'!")
else:
    print("Nenhum dado foi baixado.")
    exit(1)