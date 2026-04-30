# consulta_cep.py
# Nível Avançado - API de Consulta de CEP (ViaCEP)
# Disciplina: Engenharia de Prompt e Aplicações em IA - UDF
# Gerado com apoio do GitHub Copilot e revisado pelo autor

import requests
import json

def validar_cep(cep: str) -> str:
    """Remove caracteres não numéricos e valida o formato do CEP."""
    cep_limpo = cep.replace("-", "").replace(".", "").strip()
    if not cep_limpo.isdigit() or len(cep_limpo) != 8:
        raise ValueError(f"CEP inválido: '{cep}'. O CEP deve conter exatamente 8 dígitos.")
    return cep_limpo

def consultar_cep(cep: str) -> dict:
    """
    Consulta a API pública ViaCEP e retorna os dados de endereço.
    Lança exceções em caso de erro de conexão ou CEP inexistente.
    """
    cep_formatado = validar_cep(cep)
    url = f"https://viacep.com.br/ws/{cep_formatado}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Sem conexão com a internet. Verifique sua rede.")
    except requests.exceptions.Timeout:
        raise TimeoutError("A requisição demorou muito. Tente novamente.")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Erro na requisição HTTP: {e}")

    dados = resposta.json()

    if "erro" in dados:
        raise ValueError(f"CEP '{cep}' não encontrado na base de dados.")

    return dados

def exibir_endereco(dados: dict) -> None:
    """Formata e exibe os dados de endereço de forma legível."""
    print("\n" + "="*45)
    print("           📍 ENDEREÇO ENCONTRADO")
    print("="*45)
    print(f"  CEP        : {dados.get('cep', 'N/A')}")
    print(f"  Logradouro : {dados.get('logradouro', 'N/A')}")
    print(f"  Complemento: {dados.get('complemento', 'N/A') or '—'}")
    print(f"  Bairro     : {dados.get('bairro', 'N/A')}")
    print(f"  Cidade     : {dados.get('localidade', 'N/A')}")
    print(f"  Estado     : {dados.get('uf', 'N/A')}")
    print(f"  IBGE       : {dados.get('ibge', 'N/A')}")
    print("="*45)

def main():
    print("\n🔍 CONSULTA DE CEP — ViaCEP")
    print("Digite 'sair' para encerrar.\n")

    while True:
        cep_entrada = input("Digite o CEP (ex: 01001-000): ").strip()

        if cep_entrada.lower() == "sair":
            print("Encerrando. Até mais!")
            break

        try:
            dados = consultar_cep(cep_entrada)
            exibir_endereco(dados)
        except ValueError as e:
            print(f"⚠️  {e}")
        except (ConnectionError, TimeoutError, RuntimeError) as e:
            print(f"❌ {e}")

        print()

if __name__ == "__main__":
    main()
