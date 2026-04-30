# organizar_arquivos.py
# Missão 01 - Automação de Arquivos
# Disciplina: Engenharia de Prompt e Aplicações em IA - UDF
# Gerado com apoio do Ghostwriter (Replit) e revisado pelo autor

import os
import shutil

# Mapeamento de extensões para pastas de destino
MAPA_EXTENSOES = {
    # Documentos
    ".pdf": "documentos",
    ".doc": "documentos",
    ".docx": "documentos",
    ".txt": "documentos",
    ".odt": "documentos",
    # Imagens
    ".jpg": "imagens",
    ".jpeg": "imagens",
    ".png": "imagens",
    ".gif": "imagens",
    ".bmp": "imagens",
    ".svg": "imagens",
    ".webp": "imagens",
    # Vídeos
    ".mp4": "videos",
    ".avi": "videos",
    ".mkv": "videos",
    ".mov": "videos",
    # Áudios
    ".mp3": "audios",
    ".wav": "audios",
    ".ogg": "audios",
    # Planilhas
    ".xls": "planilhas",
    ".xlsx": "planilhas",
    ".csv": "planilhas",
    # Apresentações
    ".ppt": "apresentacoes",
    ".pptx": "apresentacoes",
    # Código
    ".py": "codigo",
    ".js": "codigo",
    ".html": "codigo",
    ".css": "codigo",
    ".json": "codigo",
    # Compactados
    ".zip": "compactados",
    ".rar": "compactados",
    ".tar": "compactados",
    ".gz": "compactados",
}

def criar_pasta_se_nao_existir(caminho: str) -> None:
    """Cria a pasta de destino caso ela não exista."""
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"  📁 Pasta criada: {caminho}")

def obter_pasta_destino(extensao: str, pasta_raiz: str) -> str:
    """Retorna o caminho da pasta de destino com base na extensão."""
    categoria = MAPA_EXTENSOES.get(extensao.lower(), "outros")
    return os.path.join(pasta_raiz, categoria)

def organizar_pasta(pasta_origem: str) -> dict:
    """
    Organiza os arquivos da pasta de origem em subpastas por extensão.
    Retorna um relatório com o número de arquivos movidos por categoria.
    """
    if not os.path.isdir(pasta_origem):
        raise NotADirectoryError(f"O caminho '{pasta_origem}' não é uma pasta válida.")

    relatorio = {}
    arquivos = [
        f for f in os.listdir(pasta_origem)
        if os.path.isfile(os.path.join(pasta_origem, f))
    ]

    if not arquivos:
        print("⚠️  Nenhum arquivo encontrado para organizar.")
        return relatorio

    print(f"\n🔍 {len(arquivos)} arquivo(s) encontrado(s). Iniciando organização...\n")

    for nome_arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, nome_arquivo)
        _, extensao = os.path.splitext(nome_arquivo)

        pasta_destino = obter_pasta_destino(extensao, pasta_origem)
        criar_pasta_se_nao_existir(pasta_destino)

        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        # Evita sobrescrever arquivos com mesmo nome
        if os.path.exists(caminho_destino):
            base, ext = os.path.splitext(nome_arquivo)
            caminho_destino = os.path.join(pasta_destino, f"{base}_duplicado{ext}")

        shutil.move(caminho_origem, caminho_destino)

        categoria = os.path.basename(pasta_destino)
        relatorio[categoria] = relatorio.get(categoria, 0) + 1
        print(f"  ✅ Movido: {nome_arquivo} → {categoria}/")

    return relatorio

def exibir_relatorio(relatorio: dict) -> None:
    """Exibe o resumo da organização."""
    print("\n" + "="*40)
    print("         📊 RELATÓRIO FINAL")
    print("="*40)
    total = sum(relatorio.values())
    for categoria, qtd in sorted(relatorio.items()):
        print(f"  {categoria:<20} : {qtd} arquivo(s)")
    print("-"*40)
    print(f"  {'TOTAL':<20} : {total} arquivo(s)")
    print("="*40)

def main():
    print("="*40)
    print("   📂 ORGANIZADOR AUTOMÁTICO DE ARQUIVOS")
    print("="*40)

    pasta = input("\nDigite o caminho da pasta a organizar\n(ou pressione Enter para usar a pasta atual): ").strip()

    if not pasta:
        pasta = os.getcwd()

    print(f"\n🗂  Organizando: {pasta}")

    try:
        relatorio = organizar_pasta(pasta)
        if relatorio:
            exibir_relatorio(relatorio)
            print("\n✅ Organização concluída com sucesso!")
    except NotADirectoryError as e:
        print(f"\n❌ Erro: {e}")
    except PermissionError:
        print("\n❌ Erro: Sem permissão para mover arquivos nesta pasta.")

if __name__ == "__main__":
    main()
