## Criação do codigo main.py para a automatização de todos os processos.

import os
import subprocess
import sys
import time

def executar_etapa(nome_etapa, arquivo_script):
    print(f"\n==========================================")
    print(f"Executando etapa: {nome_etapa}")
    print(f"==========================================")
    
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    inicio = time.time()
    resultado = subprocess.run(
        [sys.executable, arquivo_script], 
        capture_output=True, 
        text=True, 
        encoding="utf-8",
        errors="replace",
        env=env
    )
    fim = time.time()
    
    if resultado.returncode == 0:
        print(resultado.stdout)
        print(f" {nome_etapa} concluída em {fim - inicio:.2f} segundos.")
    else:
        print(f" Erro na etapa {nome_etapa}:")
        print(resultado.stderr)
        raise SystemExit(1)

def main():
    print("Iniciando Pipeline de Dados Financeiros B3")
    
    executar_etapa("Extração-Extract (E)", "extracao.py")
    executar_etapa("Transformação-Transform (T)", "transformacao.py")
    executar_etapa("Carga-Load (L)", "carga.py")
    
    print("\n==========================================")
    print("PIPELINE FINALIZADO COM SUCESSO!")
    print("==========================================")

if __name__ == "__main__":
    main()