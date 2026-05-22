# 🌙 Dreamy Hub — Projeto Módulo 3: Low Code / No Code / Vibecode

> **Disciplina:** engenharia de prompt e aplicações em IA 
> **Professor(a):** Kadidja Valéria  
> **Instituição:** UDF Centro Universitário  
> **Data:** 22/05/2026  
> **Aluno:** Matheo Augustus Rocha Bagatini

---

## 📌 Desafio Escolhido

O desafio proposto foi o desenvolvimento de um **hub de gestão de clientes para a agência de social media Dreamy**, uma empresa real de Brasília-DF. O sistema precisava resolver um problema concreto: clientes da agência não tinham visibilidade sobre o trabalho realizado para eles — posts planejados, demandas em andamento, pagamentos e métricas de crescimento ficavam dispersos em planilhas e mensagens de WhatsApp.

**O desafio central:** construir, do zero, uma plataforma web completa e segura onde cada cliente pudesse acessar exclusivamente seus próprios dados em tempo real, e o administrador pudesse gerenciar todos os clientes a partir de um único painel.

---

## 🖥️ Protótipo

### Link de Acesso
🔗 **[www.dreamysm.com.br](https://www.dreamysm.com.br)**

### Credenciais de Acesso para Avaliação
| Perfil | Login | Senha |
|--------|-------|-------|
| Teste (Avaliação) | testeudf | 12345678 |

> ℹ️ O perfil de teste permite visualizar o sistema completo na perspectiva do cliente.

### Como o Protótipo Funciona

O sistema possui dois perfis distintos com experiências completamente diferentes:

**Perfil Administrador (Dreamy):**
- Gerencia todos os clientes cadastrados
- Adiciona posts no calendário editorial de cada cliente
- Cria e acompanha demandas no kanban (Solicitado → Em andamento → Concluído)
- Lança pagamentos e contratos
- Faz upload de imagens para o simulador de feed
- Visualiza métricas de crescimento por cliente

**Perfil Cliente:**
- Acessa exclusivamente seus próprios dados
- Visualiza o calendário de posts agendados
- Acompanha o status das demandas em tempo real
- Consulta histórico de pagamentos e contratos
- Vê o simulador de feed do Instagram
- Recebe notificações quando o admin atualiza algo

### Arquitetura Técnica
```
Frontend (HTML/CSS/JS puro) → Vercel (www.dreamysm.com.br)
        ↓
Backend (Node.js + Express) → Railway (API REST)
        ↓
Banco de Dados (PostgreSQL)  → Railway
```

---

## ⚙️ Plataforma e Abordagem Utilizada

### Abordagem: Vibecode com IA (Claude Sonnet)

Este projeto foi desenvolvido inteiramente através de **engenharia de prompt** — utilizando o Claude (Anthropic) como parceiro de desenvolvimento em conversas iterativas e detalhadas. Nenhuma ferramenta no-code/low-code tradicional foi utilizada; ao invés disso, prompts precisos e bem estruturados guiaram a geração de código real e funcional.

### Stack Tecnológico
| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| Frontend | HTML5 + CSS3 + JavaScript puro | Sem dependências externas, arquivo único, fácil deploy |
| Backend | Node.js + Express | Ecossistema npm rico, compatível com Railway |
| Banco de Dados | PostgreSQL | Robusto, relacional, suporte a constraints e CASCADE |
| Deploy Frontend | Vercel | Deploy automático via GitHub, SSL gratuito |
| Deploy Backend | Railway | PostgreSQL integrado, deploy via GitHub |
| Autenticação | JWT (jsonwebtoken) | Stateless, seguro, carrega company_id no token |
| Criptografia | bcrypt | Hash de senhas com salt rounds = 10 |

### Justificativa da Abordagem

A escolha do **vibecode com Claude** foi motivada por:

1. **Velocidade de prototipagem:** sistema completo construído em dias, não semanas
2. **Projeto real com necessidade real:** a Dreamy precisava da ferramenta em produção rapidamente
3. **Custo zero de desenvolvimento:** sem contratar desenvolvedor sênior
4. **Controle total do código:** diferente de Bubble ou Webflow, o código gerado é totalmente nosso
5. **Iteração rápida:** erros corrigidos em minutos através de prompts de correção

---

## ✅ Vantagens Identificadas

### 1. Velocidade de Desenvolvimento Extraordinária
Um sistema que levaria meses para uma equipe tradicional foi construído em dias. A IA gerou código funcional para autenticação, banco de dados, API REST e frontend completo a partir de descrições em linguagem natural.

### 2. Custo Zero de Desenvolvimento
Todo o stack utilizado é gratuito (Vercel free tier, Railway free tier) e o desenvolvimento não exigiu pagamento a desenvolvedores. O único custo foi o tempo investido na engenharia de prompt.

### 3. Código 100% Proprietário e Auditável
Diferente de plataformas no-code como Bubble ou Webflow, o código gerado pertence totalmente ao projeto. É possível auditar, modificar, migrar de plataforma e escalar sem limitações impostas por terceiros.

### 4. Iteração e Correção em Tempo Real
Bugs e ajustes foram resolvidos em minutos através de prompts descritivos. O ciclo "problema → prompt → solução → teste" foi extremamente eficiente.

### 5. Funcionalidades Avançadas de Segurança
A IA foi capaz de implementar boas práticas de segurança (rate limiting, sanitização XSS, JWT, bcrypt, isolamento por company_id) que normalmente exigiriam conhecimento técnico especializado.

### 6. Documentação Gerada em Paralelo
As conversas com o Claude funcionaram como documentação viva do projeto — cada decisão técnica foi justificada e registrada no histórico de prompts.

---

## ⚠️ Limitações Encontradas

### 1. Limite de Créditos e Contexto da IA
O uso intensivo do Claude exigiu o plano pago (Claude Pro), pois o plano gratuito possui limites de mensagens que se esgotam rapidamente em sessões longas de desenvolvimento. Além disso, em conversas muito extensas, o modelo perde contexto de decisões anteriores, exigindo repetição de instruções e revisão de inconsistências geradas.

### 2. Dependência de Plataformas Externas (Lock-in)
O projeto depende de Vercel, Railway e GitHub. Uma mudança de política de preços ou encerramento de serviço pode exigir migração urgente. O Railway, por exemplo, encerrou o plano gratuito ilimitado, impactando diretamente o orçamento do projeto.

### 3. Dificuldade com Cache e Deploy
O Vercel frequentemente serviu versões antigas do código devido ao cache agressivo. A solução exigiu conhecimento técnico sobre como forçar redeployment — algo que um usuário sem background técnico não conseguiria resolver facilmente.

### 4. Latência Geográfica
O Railway não possui servidores no Brasil. Com servidores nos EUA, cada requisição tem ~450ms de latência, tornando o carregamento inicial mais lento. Resolvido parcialmente com requisições paralelas via `Promise.all`.

### 5. Debugging em Produção
Erros em produção sem acesso direto ao terminal exigiram estratégias criativas de debugging — como executar queries Node.js localmente conectadas ao banco remoto. A ausência de um ambiente de staging (homologação) foi um risco real durante o desenvolvimento.

### 6. Inconsistência entre Versões Geradas
Em diferentes sessões, a IA gerou versões conflitantes do mesmo arquivo, causando bugs em produção. A ausência de um sistema de versionamento robusto por parte da IA exigiu atenção manual constante para garantir que a versão correta estava sendo deployada.

---

## 📚 Reflexão Crítica

### Como lidamos com as limitações

**Limite de créditos:** O projeto exigiu upgrade para o plano pago do Claude Pro. Para maximizar o uso dos créditos, os prompts foram refinados para serem mais objetivos e incluir sempre o contexto necessário, evitando mensagens desnecessárias.

**Latência:** Implementamos carregamento paralelo com `Promise.all`, reduzindo o tempo de carregamento de ~3.5s para ~500ms. Também utilizamos cache local com localStorage para exibir dados instantaneamente enquanto a API carrega em background.

**Cache do Vercel:** Desenvolvemos um processo de deploy confiável — removendo o arquivo do git e recriando, além de adicionar arquivos de configuração que forçam o Vercel a reconhecer o projeto como HTML estático.

**Inconsistência de versões:** Mantivemos um registro das decisões arquiteturais importantes e sempre validamos a versão em produção via console do browser antes de considerar uma feature concluída.

### O que o vibecode pode e o que não pode

O vibecode com IA é **extraordinariamente poderoso** para:
- Gerar estruturas CRUD completas rapidamente
- Implementar padrões de segurança conhecidos
- Criar interfaces funcionais com identidade visual consistente
- Resolver problemas de lógica de negócio bem descritos

Mas **ainda exige habilidade humana** para:
- Debugar problemas de ambiente (cache, deploy, variáveis de ambiente)
- Tomar decisões arquiteturais de longo prazo
- Garantir consistência entre múltiplas sessões
- Testar e validar o produto final em produção

### Conclusão

O vibecode não elimina a necessidade de pensamento técnico — ele **democratiza o acesso à implementação técnica**. Um empreendedor com capacidade de descrever bem seus problemas e validar soluções consegue construir software de qualidade profissional sem ser desenvolvedor. Mas precisa entender o suficiente para identificar quando a IA erra e como corrigi-la.

---

## 👥 Colaboração

Este projeto foi desenvolvido individualmente por **Matheo Augustus Rocha Bagatini**, proprietário da Dreamy Social Media. Todas as decisões de produto, arquitetura, testes e validação foram tomadas pelo desenvolvedor. A IA foi utilizada como ferramenta de implementação, respondendo aos requisitos e correções definidos pelo desenvolvedor humano.

---

## 📝 Registro da Atividade

| Campo | Valor |
|-------|-------|
| Data | 22/05/2026 |
| Atividade | Mini-projeto de aplicação com vibecode/IA |
| Ferramenta principal | Claude (Anthropic) — engenharia de prompt |
| Repositório | [github.com/paodilas/dreamysm](https://github.com/paodilas/dreamysm) |
| Deploy | [www.dreamysm.com.br](https://www.dreamysm.com.br) |
| Professor(a) | Kadidja Valéria |
| Instituição | UDF Centro Universitário |

---

## 🚀 Próximos Passos

### Melhorias Planejadas para o Protótipo
- **UI/UX avançado:** Animações de entrada, transições suaves e design premium mantendo a identidade visual navy/creme/gold da Dreamy
- **Gerador de relatório PDF:** Relatório mensal automático com métricas e posts do período
- **Migração de servidor:** Avaliar alternativas ao Railway com servidores na América do Sul para reduzir latência

### Possíveis Evoluções para o Projeto Final
- **Integração com Instagram Graph API:** Sincronizar métricas reais automaticamente
- **Chat interno:** Canal de comunicação direto entre agência e cliente dentro da plataforma
- **Assinatura de contratos digital:** Integração com serviço de assinatura eletrônica
- **Dashboard público:** Versão simplificada do relatório para apresentações sem login

---

*Projeto desenvolvido com engenharia de prompt avançada usando Claude (Anthropic) | Dreamy Social Media — Brasília, DF*
