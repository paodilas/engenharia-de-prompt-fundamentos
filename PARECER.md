# 📝 Parecer Individual — Unidade II

**Disciplina:** Engenharia de Prompt e Aplicações em IA  
**Instituição:** Centro Universitário UDF  
**Professora:** Kadidja Valéria  
**Período:** Abril de 2026  

---

## 1. Introdução

A Unidade II da disciplina Engenharia de Prompt e Aplicações em IA abordou, de forma aprofundada, o tema da Programação Assistida por Inteligência Artificial. Ao longo das aulas, foram discutidas as transformações que as ferramentas de IA estão promovendo no ciclo de desenvolvimento de software, desde a geração automática de código até a refatoração inteligente e a automação de tarefas repetitivas. O presente parecer tem por objetivo sistematizar as experiências práticas vivenciadas durante a unidade, relacionando-as aos conteúdos teóricos apresentados, com especial ênfase nas ferramentas utilizadas, no workflow de colaboração humano-IA e nas questões éticas que permeiam esse novo paradigma de desenvolvimento.

---

## 2. Práticas Realizadas

Durante a Unidade II, as atividades práticas foram conduzidas com o suporte de duas ferramentas de IA: o **GitHub Copilot** e o **Claude (Anthropic)**. A experiência com o GitHub Copilot se deu principalmente no contexto de sugestões de código inline, em que a ferramenta demonstrou forte capacidade de antecipar padrões sintáticos e completar blocos lógicos de maneira ágil. Essa dinâmica corresponde à evolução apresentada em aula, que descreve a transição dos *assistentes reativos* — que realizam autocompletar de código — para *agentes autônomos* capazes de planejar, executar, refatorar e depurar.

O Claude foi utilizado como apoio na formulação de prompts, na organização lógica de soluções e na revisão crítica de raciocínios. Essa experiência ilustrou, na prática, o **Loop de Colaboração Humano-IA** abordado nas aulas: o ciclo de instrução (definir objetivo claro), processamento (a IA propõe estrutura e lógica), revisão (validar sem aceitar cegamente) e ajuste (refinar o código resultante). Ficou evidente que a qualidade do resultado é diretamente proporcional à qualidade do prompt elaborado pelo usuário.

Um aprendizado significativo foi perceber os limites e os pontos fortes de cada ferramenta. O Copilot se destacou na geração de estruturas boilerplate e sugestões de sintaxe, enquanto o Claude demonstrou maior aptidão para raciocínio contextual e explicação de lógicas complexas. Em ambos os casos, a intervenção humana continuou sendo indispensável para garantir a lógica de negócio, tratar casos extremos (*edge cases*) e tomar decisões arquiteturais.

---

## 3. Relação com o Conteúdo Estudado

### 3.1 Workflow Sustentável com IA

O modelo de workflow sustentável apresentado na aula de 24/04 estrutura o processo em cinco etapas: **planejamento, implementação, revisão, teste e manutenção**. Essa estrutura foi percebida como altamente coerente com a prática. Na etapa de planejamento, ficou clara a importância de separar as decisões de arquitetura de alto nível — responsabilidade humana — da geração do código boilerplate, delegada à IA. Na fase de revisão, a máxima aprendida foi: nunca aceitar código gerado sem validar o comportamento prático.

Os cinco princípios fundamentais — **Transparência, Verificação, Progressão, Documentação e Revisão por Pares** — funcionaram como um guia valioso. Em particular, o princípio da Transparência reforçou a necessidade de compreender o que a IA gera, e não apenas copiar e aplicar. Se a IA gerar algo que o desenvolvedor não compreende totalmente, a orientação é clara: *pause e aprenda*.

### 3.2 Ética e Responsabilidade Legal

Um dos pontos mais impactantes da unidade foi a discussão sobre responsabilidade legal. Conforme destacado em aula, com base em **Lee, Goldberg e Kohane (2024)**: ferramentas de IA são assistentes, não agentes autônomos — o desenvolvedor que aceita e implementa código gerado por IA assume total responsabilidade por esse código. Esse entendimento é crucial e transforma a postura com que se utiliza qualquer ferramenta generativa.

Além disso, os riscos de vulnerabilidades de segurança (como injeção de SQL e uso de bibliotecas desatualizadas), violações de licenças de propriedade intelectual e a replicação de viés em algoritmos são ameaças reais que exigem uma postura crítica e vigilante por parte do desenvolvedor. A IA não tem consciência de segurança; essa responsabilidade é inteiramente humana (**Barcaui, 2025**).

### 3.3 Arsenal Técnico: Copilot, Replit e Ghostwriter

A unidade apresentou três ferramentas centrais:

| Ferramenta | Perfil | Superpoder |
|------------|--------|-----------|
| **GitHub Copilot** | Co-piloto tático | Sugestões inline e refatoração inteligente |
| **Replit + Ghostwriter** | Base de operações | Ambiente cloud com execução imediata |
| **Ghostwriter** | Analista de contexto | Depuração contextual nativa |

Embora a prática direta com Replit/Ghostwriter tenha sido mais pontual nesta unidade, a compreensão de seus perfis e casos de uso permitiu um olhar mais estratégico sobre quando e como cada ferramenta agrega valor ao processo de desenvolvimento.

---

## 4. Análise Crítica

A principal aprendizagem desta unidade pode ser sintetizada na fórmula apresentada ao final das aulas:

> **[ Intuição Humana ] + [ Velocidade da IA ] = [ Desenvolvedor Aumentado ]**

A IA é, de fato, uma parceira poderosa, mas seu uso indiscriminado pode gerar **dependência cognitiva** — o risco de "esquecer como programar" — além de introduzir código inseguro e problemas de licenciamento.

Pesquisas consolidadas de instituições como McKinsey, PwC, MIT, Stanford, Harvard, FGV e IBGE, mencionadas em aula, confirmam que profissionais que dominam o uso de IA apresentam remuneração superior, crescimento mais acelerado e maior atratividade para recrutadores. Esses dados reforçam que dominar essas práticas não é opcional: é uma exigência do mercado atual.

A maior reflexão que esta unidade provocou foi a mudança de perspectiva sobre o papel do desenvolvedor: o valor profissional deixa de estar em "digitar sintaxe" e passa a residir em **"arquitetar soluções lógicas e seguras"**. *A ferramenta agiliza a digitação; o desenvolvedor define a direção.*

---

## 5. Conclusão

A Unidade II consolidou uma visão equilibrada e madura sobre a colaboração humano-IA no desenvolvimento de software. Ficou claro que as ferramentas de programação assistida por IA representam uma evolução significativa na produtividade, mas exigem responsabilidade, senso crítico e transparência por parte de quem as utiliza. O aprendizado desta unidade será incorporado como uma prática contínua: usar a IA com consciência, validar o que é gerado, documentar as escolhas e manter a autoria intelectual sobre cada linha de código implementada.

**Ferramentas de IA utilizadas:**
- **Claude (Anthropic)** — apoio na organização e redação do parecer, com revisão e validação do conteúdo pelo autor.
- **GitHub Copilot** — utilizado durante as atividades práticas para sugestões de código inline e refatoração.
