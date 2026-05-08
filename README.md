# 🤖 Unidade II — Programação Assistida por IA

**Disciplina:** Engenharia de Prompt e Aplicações em IA  
**Instituição:** Centro Universitário UDF  
**Professora:** Kadidja Valéria  

---

##  Estrutura do Repositório

```
unidade2/
│
├──  README.md              ← Este arquivo
├──  PARECER.md             ← Parecer individual da Unidade II
│
├──  basico/
│   ├── calculadora.py        ← Calculadora com 4 operações
│   └── README.md
│
├──  intermediario/
│   ├── jogo_formas.py        ← Jogo educativo de formas geométricas
│   └── README.md
│
├──  avancado/
│   ├── consulta_cep.py       ← Consulta à API ViaCEP
│   └── README.md
│
├──  missao01/
│   ├── organizar_arquivos.py ← Automação de organização por extensão
│   └── README.md
│
├──  missao02/
│   ├── consulta_api.py       ← Consulta ViaCEP + depuração com IA
│   └── README.md
│
└──  missao03/
    ├─ notificacoes.py       ← Sistema de alertas por condição crítica
    └── README.md
```

---

##  Atividades

### Projetos Práticos

| Nível | Projeto | Descrição |
|-------|---------|-----------|
| Básico | [Calculadora](./basico/) | 4 operações matemáticas com menu interativo |
| Intermediário | [Jogo das Formas](./intermediario/) | Jogo educativo de formas geométricas |
| Avançado | [Consulta CEP](./avancado/) | API ViaCEP com tratamento de erros completo |

### Missões

| Missão | Projeto | Ferramenta IA |
|--------|---------|---------------|
| 01 | [Automação de Arquivos](./missao01/) | Ghostwriter (Replit) |
| 02 | [Consulta a APIs](./missao02/) | Ghostwriter (Replit) |
| 03 | [Sistema de Notificações](./missao03/) | GitHub Copilot |

---

##  Ferramentas de IA Utilizadas

| Ferramenta | Uso principal |
|------------|--------------|
| **GitHub Copilot** | Sugestões inline, geração de funções, refatoração |
| **Ghostwriter (Replit)** | Depuração contextual, correção de requisições, sugestões específicas |
| **Claude (Anthropic)** | Organização lógica, formulação de prompts, revisão de raciocínio |

---

##  Parecer

O parecer individual sobre a Unidade II está disponível em [`PARECER.md`](./PARECER.md).

---

##  Como executar os scripts

**Pré-requisito:** Python 3.x instalado.

Para os scripts que usam a API ViaCEP (avancado e missao02):
```bash
pip install requests
```

Todos os outros scripts usam apenas bibliotecas nativas do Python.

---

##  Transparência

> Este repositório foi produzido com apoio de ferramentas de IA (GitHub Copilot e Claude), conforme exigido pela metodologia da disciplina. Todo o código gerado foi revisado, validado e ajustado pelo autor. A responsabilidade pelo conteúdo entregue é integralmente do estudante, em conformidade com os princípios éticos discutidos na Unidade II.
