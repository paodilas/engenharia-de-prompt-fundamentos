# 🔷 Nível Intermediário — Jogo das Formas Geométricas

## 📋 Descrição

Jogo educativo de terminal onde o jogador recebe dicas sobre uma forma geométrica e deve identificá-la corretamente. Quanto mais rápido acertar, mais pontos ganha.

## 🚀 Como executar

```bash
python jogo_formas.py
```

> Requer Python 3.x — nenhuma biblioteca externa necessária.

## 🎮 Regras do jogo

- A cada rodada, uma forma aleatória é sorteada
- Uma dica é exibida (ex: *"Tenho 3 lados e 3 ângulos"*)
- O jogador tem **3 tentativas** por rodada
- Pontuação por tentativa:
  - 1ª tentativa correta → **30 pontos**
  - 2ª tentativa correta → **20 pontos**
  - 3ª tentativa correta → **10 pontos**
  - Errou tudo → **0 pontos**

## 🔷 Formas incluídas

| Forma | Dica |
|-------|------|
| Triângulo | 3 lados e 3 ângulos |
| Quadrado | 4 lados iguais, ângulos retos |
| Círculo | Sem lados, redondo |
| Retângulo | 4 lados, opostos iguais |
| Hexágono | 6 lados — favorito das abelhas |
| Pentágono | 5 lados |

## 🧠 Como a IA ajudou

| Etapa | Contribuição |
|-------|-------------|
| Dicionário de formas | Copilot sugeriu estrutura com `sinonimos` para aceitar variações de digitação |
| Sistema de pontuação | Copilot gerou lógica de `tentativas * 10` |
| Exibição do ranking | Copilot gerou o bloco condicional de classificação |
| **Lógica de negócio** | **Humano** — definiu as dicas, balanceou a pontuação e validou a experiência do jogo |
