# notificacoes.py
# Missão 03 - Sistema de Notificações
# Disciplina: Engenharia de Prompt e Aplicações em IA - UDF
# Gerado com apoio do GitHub Copilot e refatorado com sugestão de limpeza do Copilot

from datetime import datetime

# ─── Versão 1 (antes da refatoração pelo Copilot) ────────────────────────────
# def checar_temperatura(temp):
#     if temp > 80:
#         print("ALERTA: temperatura crítica! " + str(temp))
#     else:
#         print("Temperatura ok: " + str(temp))
#
# def checar_cpu(uso):
#     if uso > 90:
#         print("ALERTA: CPU sobrecarregada! " + str(uso) + "%")
#     else:
#         print("CPU ok: " + str(uso) + "%")
# ─────────────────────────────────────────────────────────────────────────────

# ─── Versão 2 (após refatoração sugerida pelo Copilot) ───────────────────────

def _timestamp() -> str:
    """Retorna o timestamp atual formatado."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def emitir_alerta(tipo: str, valor: float, unidade: str, mensagem: str) -> None:
    """Dispara um alerta crítico formatado no console (simula e-mail)."""
    print(f"\n{'!'*45}")
    print(f"  🚨 ALERTA CRÍTICO — {tipo.upper()}")
    print(f"  ⏰ Timestamp : {_timestamp()}")
    print(f"  📊 Valor     : {valor}{unidade}")
    print(f"  📋 Mensagem  : {mensagem}")
    print(f"{'!'*45}\n")

def emitir_ok(tipo: str, valor: float, unidade: str) -> None:
    """Exibe mensagem de status normal."""
    print(f"  ✅ [{_timestamp()}] {tipo}: {valor}{unidade} — Normal")

def checar_temperatura(temperatura: float, limite: float = 80.0) -> None:
    """Verifica se a temperatura ultrapassou o limite crítico."""
    if temperatura > limite:
        emitir_alerta(
            tipo="Temperatura",
            valor=temperatura,
            unidade="°C",
            mensagem=f"Temperatura acima de {limite}°C! Risco de superaquecimento."
        )
    else:
        emitir_ok("Temperatura", temperatura, "°C")

def checar_cpu(uso_cpu: float, limite: float = 90.0) -> None:
    """Verifica se o uso de CPU ultrapassou o limite crítico."""
    if uso_cpu > limite:
        emitir_alerta(
            tipo="CPU",
            valor=uso_cpu,
            unidade="%",
            mensagem=f"Uso de CPU acima de {limite}%! Sistema sobrecarregado."
        )
    else:
        emitir_ok("CPU", uso_cpu, "%")

def checar_memoria(uso_memoria: float, limite: float = 85.0) -> None:
    """Verifica se o uso de memória RAM ultrapassou o limite crítico."""
    if uso_memoria > limite:
        emitir_alerta(
            tipo="Memória RAM",
            valor=uso_memoria,
            unidade="%",
            mensagem=f"Uso de memória acima de {limite}%! Risco de travamento."
        )
    else:
        emitir_ok("Memória", uso_memoria, "%")

def checar_disco(uso_disco: float, limite: float = 95.0) -> None:
    """Verifica se o uso do disco ultrapassou o limite crítico."""
    if uso_disco > limite:
        emitir_alerta(
            tipo="Disco",
            valor=uso_disco,
            unidade="%",
            mensagem=f"Disco com {uso_disco}% de uso! Risco de falha por espaço insuficiente."
        )
    else:
        emitir_ok("Disco", uso_disco, "%")

def executar_monitoramento(metricas: dict) -> None:
    """Executa todas as verificações de monitoramento com base nas métricas fornecidas."""
    print("\n" + "="*45)
    print("   🖥️  SISTEMA DE MONITORAMENTO ATIVO")
    print(f"   ⏰ {_timestamp()}")
    print("="*45)

    checar_temperatura(metricas.get("temperatura", 0))
    checar_cpu(metricas.get("cpu", 0))
    checar_memoria(metricas.get("memoria", 0))
    checar_disco(metricas.get("disco", 0))

    print("="*45)
    print("   Monitoramento concluído.")
    print("="*45 + "\n")

def main():
    # Cenário 1: todos os valores normais
    print("\n>>> CENÁRIO 1: Valores normais")
    executar_monitoramento({
        "temperatura": 65.0,
        "cpu": 45.0,
        "memoria": 60.0,
        "disco": 70.0
    })

    # Cenário 2: condições críticas
    print(">>> CENÁRIO 2: Condições críticas")
    executar_monitoramento({
        "temperatura": 95.0,
        "cpu": 98.0,
        "memoria": 92.0,
        "disco": 97.0
    })

    # Cenário 3: monitoramento interativo
    print(">>> CENÁRIO 3: Inserir valores manualmente")
    try:
        metricas_manuais = {
            "temperatura": float(input("  Temperatura (°C): ")),
            "cpu": float(input("  Uso de CPU (%): ")),
            "memoria": float(input("  Uso de Memória (%): ")),
            "disco": float(input("  Uso de Disco (%): ")),
        }
        executar_monitoramento(metricas_manuais)
    except ValueError:
        print("  ⚠️  Valor inválido inserido. Use números.")

if __name__ == "__main__":
    main()
