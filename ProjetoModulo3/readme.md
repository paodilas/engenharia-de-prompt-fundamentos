# 🌙 Dreamy Hub — Projeto Módulo 3: Low Code / No Code / Vibecode

> **Disciplina:** Engenharia de Prompt e Aplicações em IA  
> **Professor(a):** Kadidja Valéria  
> **Instituição:** UDF Centro Universitário  
> **Data:** 22/05/2026  
> **Aluno:** Matheo Augustus Rocha Bagatini

---

## 📌 Desafio Escolhido

O desafio escolhido foi o desenvolvimento de um **hub de gestão de clientes para a agência de social media Dreamy**, empresa real de Brasília-DF. O problema central era que clientes da agência não tinham visibilidade sobre o trabalho realizado — posts planejados, demandas em andamento, pagamentos e métricas ficavam dispersos em planilhas e WhatsApp.

A solução precisava permitir que cada cliente acessasse exclusivamente seus próprios dados em tempo real, enquanto o administrador gerenciava todos os clientes a partir de um único painel centralizado.

---

## 🖥️ Protótipo

🔗 **Link de acesso:** [www.dreamysm.com.br](https://www.dreamysm.com.br)

### Credenciais de Acesso para Avaliação
| Perfil | Login | Senha |
|--------|-------|-------|
| Teste (Avaliação) | testeudf@udf.com.br | 12345678 |

### Como o protótipo funciona

O sistema possui dois perfis com experiências distintas:

**Perfil Administrador:**
- Cadastra e gerencia clientes
- Adiciona posts no calendário editorial por cliente
- Cria demandas e acompanha pelo kanban (Solicitado → Em andamento → Concluído)
- Lança pagamentos e contratos em PDF
- Faz upload do feed do Instagram e métricas de crescimento

**Perfil Cliente:**
- Acessa exclusivamente seus próprios dados
- Visualiza posts agendados no calendário
- Acompanha demandas em tempo real
- Consulta pagamentos, contratos e feed do Instagram
- Recebe notificações quando o admin atualiza algo

> Os prints das telas estão na pasta `/docs` do repositório.

---

## ⚙️ Plataforma Utilizada

O projeto foi desenvolvido em **três etapas**, utilizando ferramentas distintas para cada fase:

### Etapa 1 — Esboço e Prototipagem Visual: Bubble + Antigravity

O processo começou com a criação do esboço e protótipo visual utilizando **Bubble** e **Antigravity**:

- **Bubble** foi utilizado para mapear o fluxo das telas, a estrutura de dados e a lógica de navegação entre os perfis (admin e cliente). Sua interface visual drag-and-drop permitiu validar rapidamente a arquitetura do sistema antes de partir para o desenvolvimento.

- **Antigravity** complementou o processo com a criação do esboço visual da identidade da plataforma — definindo a paleta de cores (navy/creme/gold), hierarquia de componentes e layout geral das telas.

Essa etapa foi essencial para ter clareza sobre **o que precisava ser construído** antes de partir para o código.

### Etapa 2 — Desenvolvimento: Claude (Vibecode via Engenharia de Prompt)

Com o esboço validado no Bubble e Antigravity, o desenvolvimento real foi feito utilizando o **Claude (Anthropic)** como ferramenta de vibecode. Os requisitos mapeados visualmente foram traduzidos em prompts precisos, que guiaram a geração do código completo:

- Frontend: HTML5 + CSS3 + JavaScript → hospedado no Vercel
- Backend: Node.js + Express → hospedado no Railway
- Banco de Dados: PostgreSQL → Railway
- Autenticação: JWT + bcrypt

### Justificativa da combinação de ferramentas

| Ferramenta | Papel no projeto | Por que foi escolhida |
|-----------|-----------------|----------------------|
| **Bubble** | Prototipagem do fluxo e estrutura de dados | Interface visual rápida para validar a lógica antes de codar |
| **Antigravity** | Esboço visual e identidade da plataforma | Facilidade para definir layout e componentes visuais |
| **Claude** | Desenvolvimento do código completo | Capacidade de gerar sistemas complexos a partir de linguagem natural |

---

## ✅ Vantagens Identificadas

1. **Prototipagem rápida com Bubble:** a interface drag-and-drop do Bubble permitiu mapear todo o fluxo do sistema visualmente em poucas horas, sem escrever uma linha de código. Isso acelerou muito a fase de planejamento.

2. **Esboço visual com Antigravity:** a ferramenta facilitou a definição da identidade visual e do layout antes do desenvolvimento, evitando retrabalho e garantindo consistência no design final.

3. **Desenvolvimento ágil com Claude:** com o esboço pronto, os prompts para o Claude foram muito mais precisos e objetivos, resultando em código funcional e alinhado com o que havia sido planejado nas etapas anteriores.

4. **Controle total sobre o código:** diferente de usar apenas o Bubble para o produto final, o código gerado pelo Claude pertence 100% ao projeto — sem lock-in de plataforma.

5. **Segurança avançada via prompts:** boas práticas como rate limiting, sanitização XSS, isolamento multi-tenant e criptografia bcrypt foram implementadas descrevendo os requisitos em linguagem natural.

---

## ⚠️ Limitações Encontradas

1. **Bubble não sustenta o produto final:** o Bubble foi excelente para o esboço, mas suas limitações de customização visual e performance o tornaram inviável para o produto real — exigindo migrar para desenvolvimento com Claude.

2. **Limite de créditos da IA:** o uso intensivo do Claude exigiu upgrade para o plano pago (Claude Pro), pois o plano gratuito se esgota rapidamente em sessões longas de desenvolvimento.

3. **Perda de contexto em sessões longas:** em conversas muito extensas, o Claude perdeu contexto de decisões anteriores, gerando código inconsistente e exigindo repetição de instruções.

4. **Dificuldade com cache e deploy:** o Vercel frequentemente serviu versões antigas do código, exigindo conhecimento técnico para resolver — algo além do escopo do low-code puro.

5. **Latência geográfica:** sem servidores no Brasil, cada requisição ao Railway tem ~450ms de latência, impactando a performance do sistema.

---

## 📚 Reflexão Crítica

O principal aprendizado foi que **as ferramentas low-code e o vibecode com IA funcionam melhor em combinação do que isoladamente**. O Bubble e o Antigravity foram fundamentais na fase de esboço — rápidos, visuais e intuitivos para validar ideias. Já o Claude foi indispensável para transformar esses esboços em um produto real, funcional e seguro.

**Como as limitações foram contornadas:**

- **Transição Bubble → Claude:** o esboço feito no Bubble serviu como documentação visual dos requisitos, tornando os prompts para o Claude muito mais precisos e reduzindo inconsistências.
- **Limite de créditos:** os prompts foram refinados para serem objetivos e incluir sempre o contexto necessário, evitando mensagens desnecessárias que consomem créditos.
- **Perda de contexto:** as decisões arquiteturais foram registradas e repetidas no início de cada nova sessão com a IA.
- **Cache do Vercel:** foram adicionados arquivos de configuração (`vercel.json`) que forçam o Vercel a servir o HTML estático corretamente.
- **Latência:** implementamos `Promise.all` para carregar todos os dados em paralelo, reduzindo o tempo de carregamento de ~3.5s para ~500ms.

---

## 👥 Colaboração

Este projeto foi desenvolvido individualmente por **Matheo Augustus Rocha Bagatini**, proprietário da Dreamy Social Media. Todas as decisões de produto, arquitetura, testes e validação foram tomadas pelo desenvolvedor. As ferramentas (Bubble, Antigravity e Claude) foram utilizadas como instrumentos de apoio em cada fase do projeto.

---

## 📝 Registro da Aula

| Campo | Valor |
|-------|-------|
| Data | 22/05/2026 |
| Atividade | Discussão crítica + mini-projeto de aplicação |
| Local | Laboratório de informática |
| Professor(a) | Kadidja Valéria |
| Repositório | [github.com/paodilas/dreamysm](https://github.com/paodilas/dreamysm) |
| Deploy | [www.dreamysm.com.br](https://www.dreamysm.com.br) |

---

## 🚀 Próximos Passos

**Melhorias sugeridas para o protótipo:**
- UI/UX avançado com animações e micro-interações mantendo a identidade visual da Dreamy
- Gerador de relatório PDF mensal automático com métricas e posts do período
- Migração para servidor com menor latência para o Brasil

**Possíveis evoluções para o Projeto Final da Unidade 3:**
- Integração com Instagram Graph API para sincronizar métricas reais automaticamente
- Chat interno entre agência e cliente dentro da plataforma
- Assinatura digital de contratos integrada
- Dashboard público para apresentações sem necessidade de login

---

*Projeto desenvolvido com Bubble, Antigravity e Claude (Anthropic) | Dreamy Social Media — Brasília, DF*
