# Unidade II — Programação Assistida por IA

**Disciplina:** Engenharia de Prompt e Aplicações em IA  
**Instituição:** Centro Universitário UDF  
**Professora:** Kadidja Valéria  
**Aluno:** Matheo Augustus Rocha Bagatini

---

## 📁 Estrutura do Repositório

```
engenharia-de-prompt-fundamentos/
│
├── README.md                 ← Este arquivo
├── PARECER.md                ← Parecer individual da Unidade II
├── Desafio.md                ← Desafio do Prompt Mestre
├── aula03.md · aula04.md · aula05.md
│
├── calculadora.py            ← Básico: calculadora com 4 operações
├── jogo_formas.py            ← Intermediário: jogo de formas geométricas
├── consulta_cep.py           ← Avançado: consulta à API ViaCEP
├── organizar_arquivos.py     ← Missão 01: organização de arquivos por extensão
├── consulta_api.py           ← Missão 02: ViaCEP + depuração
├── notificacoes.py           ← Missão 03: alertas por condição crítica
│
└── ProjetoModulo3/           ← Dreamy Hub (Low Code / Vibecode)
    ├── readme.md
    └── docs/                 ← capturas de tela
```

---

## 🧪 Atividades

### Projetos Práticos

| Nível | Projeto | Descrição |
|-------|---------|-----------|
| Básico | [Calculadora](./calculadora.py) | 4 operações matemáticas com menu interativo |
| Intermediário | [Jogo das Formas](./jogo_formas.py) | Jogo educativo de formas geométricas |
| Avançado | [Consulta CEP](./consulta_cep.py) | API ViaCEP com tratamento de erros completo |

### Missões

| Missão | Projeto | Ferramenta IA |
|--------|---------|---------------|
| 01 | [Automação de Arquivos](./organizar_arquivos.py) | Ghostwriter (Replit) |
| 02 | [Consulta a APIs](./consulta_api.py) | Ghostwriter (Replit) |
| 03 | [Sistema de Notificações](./notificacoes.py) | GitHub Copilot |

### Projeto do Módulo 3

| Projeto | Descrição |
|---------|-----------|
| [Dreamy Hub](./ProjetoModulo3/readme.md) | Hub de gestão de clientes para agência de social media |

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

```bash
git clone https://github.com/paodilas/engenharia-de-prompt-fundamentos.git
cd engenharia-de-prompt-fundamentos
python calculadora.py
```

Para os scripts que usam a API ViaCEP (avancado e missao02):
```bash
pip install requests
```

Todos os outros scripts usam apenas bibliotecas nativas do Python.

---

##  Transparência

> Este repositório foi produzido com apoio de ferramentas de IA (GitHub Copilot e Claude), conforme exigido pela metodologia da disciplina. Todo o código gerado foi revisado, validado e ajustado pelo autor. A responsabilidade pelo conteúdo entregue é integralmente do estudante, em conformidade com os princípios éticos discutidos na Unidade II.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE).
