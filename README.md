# B3 Financial Data ETL Pipeline

Um pipeline de dados **ETL (Extract, Transform, Load)** automatizado e modular desenvolvido em **Python 3.14**, focado em extrair cotações históricas da B3 (Ações e FIIs), transformar e padronizar os dados com **Pandas** e armazená-los em um banco relacional **SQLite**.

---

## Arquitetura do Pipeline

O projeto adota o princípio de separação de responsabilidades em arquitetura de dados:

    tickers.txt     extracao.py     transformacao     carga.py
     (config)       (API Yahoo)       (pandas)        (SQlite)


                            main.py
                        (codigo chefe)


1.Configuração (`tickers.txt`): Lista parametrizada de ativos da B3 a serem processados.

2.Extração (`extracao.py`): Consome a API do `yfinance` para buscar dados brutos e os salva em formato CSV.

3.Transformação (`transformacao.py`): Higieniza datas, padroniza nomes de colunas (snake_case), arredonda valores decimais e calcula a variação percentual diária.

4.Carga (`carga.py`): Conecta ao SQLite e aos dados na tabela unificada `cotacoes_b3`.

5.Orquestrador (`main.py`): Gerencia a execução sequencial do fluxo via `subprocess`, com tratamento de codificação UTF-8 e medição de tempo de execução.

---

## Tecnologias Utilizadas

* **Linguagem**: Python 3.14
* **Manipulação de Dados**: Pandas
* **Fonte de Dados**: Yahoo Finance (`yfinance`)
* **Banco de Dados**: SQLite3
* **Ambiente**: Virtualenv (`venv`) no Windows

---

Projeto finalizado com maestria!