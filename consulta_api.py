# consulta_api.py
# Missão 02 - Consulta Simples a APIs (ViaCEP)
# Disciplina: Engenharia de Prompt e Aplicações em IA - UDF
# Gerado com apoio do Ghostwriter (Replit) e revisado pelo autor
# Nota: erro intencional foi provocado na URL para demonstrar depuração com IA

import requests
import json

# URL correta da API ViaCEP
# Versão com erro intencional (demonstração de depuração):
# URL_BASE = "https://viacep.com.br/ws/{cep}/jsoon/"  # ← erro proposital: "jsoon" em vez de "json"
# A IA do Replit identificou o erro e sugeriu a correção abaixo:
URL_BASE = "https://viacep.com.br/ws/{cep}/json/"

def formatar_cep(cep: str) -> str:
    """Remove formatação do CEP e valida o número de dígitos."""
    cep_limpo = cep.replace("-", "").replace(".", "").strip()
    if not cep_limpo.isdigit() or len(cep_limpo) != 8:
        raise ValueError(f"CEP inválido: '{cep}'. Esperado: 8 dígitos numéricos.")
    return cep_limpo

def consultar_viacep(cep: str) -> dict:
    """
    Realiza requisição GET à API ViaCEP.
    Trata erros de conexão, timeout e CEP inexistente (try/except).
    """
    cep_formatado = formatar_cep(cep)
    url = URL_BASE.format(cep=cep_formatado)

    try:
        print(f"\n🌐 Consultando: {url}")
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

    except requests.exceptions.ConnectionError:
        raise ConnectionError("❌ Sem conexão. Verifique sua internet e tente novamente.")
    except requests.exceptions.Timeout:
        raise TimeoutError("⏱ A requisição excedeu o tempo limite. Tente novamente.")
    except requests.exceptions.HTTPError as err:
        raise RuntimeError(f"❌ Erro HTTP {resposta.status_code}: {err}")

    dados = resposta.json()

    if dados.get("erro"):
        raise ValueError(f"⚠️  CEP '{cep}' não encontrado. Verifique e tente novamente.")

    return dados

def imprimir_json_formatado(dados: dict) -> None:
    """Imprime o JSON recebido de forma legível e indentada."""
    print("\n📦 Resposta JSON da API (formatada):")
    print("-" * 40)
    print(json.dumps(dados, indent=4, ensure_ascii=False))
    print("-" * 40)

def imprimir_resumo(dados: dict) -> None:
    """Exibe um resumo legível dos dados de endereço."""
    print("\n📍 Resumo do Endereço:")
    print(f"  CEP        : {dados.get('cep', '—')}")
    print(f"  Logradouro : {dados.get('logradouro', '—')}")
    print(f"  Bairro     : {dados.get('bairro', '—')}")
    print(f"  Cidade     : {dados.get('localidade', '—')} / {dados.get('uf', '—')}")
    print(f"  IBGE       : {dados.get('ibge', '—')}")

def main():
    print("="*45)
    print("   🔍 MISSÃO 02 — CONSULTA DE CEP (ViaCEP)")
    print("="*45)
    print("Digite 'sair' para encerrar.\n")

    while True:
        cep = input("CEP: ").strip()

        if cep.lower() == "sair":
            print("Encerrando. Até mais!")
            break

        try:
            dados = consultar_viacep(cep)
            imprimir_json_formatado(dados)
            imprimir_resumo(dados)
        except (ValueError, ConnectionError, TimeoutError, RuntimeError) as e:
            print(str(e))

        print()

if __name__ == "__main__":
    main()
