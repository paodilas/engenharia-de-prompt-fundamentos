 # Atividade Prática: Desmontando a Máquina

## Etapa 1 – Análise de Tokens

**Frase inserida no Tokenizer:** "Matheo Augustus Rocha Bagatini A engenharia de prompt otimiza LLMs"

**Resultados:** Foram gerados **15 tokens** e 66 caracteres.

**Observações da divisão morfológica:**
Ao colocar a frase no sistema, fica claro que a IA não lê as palavras como nós. O meu nome e sobrenome ("Mat", "heo", "Bag", "atini") e a palavra "otimiza" ("otim", "iza") foram fatiados em pedaços menores. Por outro lado, palavras comuns no idioma base da IA (inglês), como "prompt", formaram um único token. Isso mostra que o vocabulário da IA é otimizado estatisticamente, e não por regras gramaticais humanas.

<img width="935" height="846" alt="image" src="https://github.com/user-attachments/assets/310a08d5-6153-4fc3-ba7f-3f7123ebb54f" />

## Etapa 2 – Teste de Previsibilidade

**Prompt base:** "O gato come..."

**Simulação 1: Modo "Muito Técnica" (Baixa Temperatura)**
Pedi para a IA agir de forma puramente lógica e biológica. As 3 palavras mais prováveis geradas foram:
1. **Ração:** Justificativa estatística, pois é o alimento doméstico mais associado à rotina do animal.
2. **Carne:** Justificativa biológica, dado que felinos são carnívoros estritos.
3. **Rato:** Justificativa instintiva e cultural (a clássica relação de caça).

**Simulação 2: Modo "Muito Criativa" (Alta Temperatura)**
Pedi para a IA completar a frase em um contexto poético e fantasioso. As 3 palavras prováveis mudaram completamente:
1. **Estrelas:** Tratando o gato como um ser místico devorando a noite.
2. **Tempo:** Uma metáfora sobre como os gatos dormem o dia todo, "consumindo" as horas.
3. **Segredos:** Personificando o animal como um guardião silencioso de mistérios.

## Etapa 3 – Raciocínio CoT (Chain-of-Thought)

**Desafio:** "Qual é a terceira letra da quinta palavra da frase 'O rato roeu a roupa do Rei de Roma'?"

**Tentativa 1 (Sem CoT):** Ao enviar a pergunta de forma direta, a IA costuma errar a resposta, pois tenta adivinhar o resultado estatisticamente em um único pulo, sem processar a estrutura da frase.

**Tentativa 2 (Forçando o Passo a Passo - CoT):**
Refiz o prompt guiando o raciocínio: *"Resolva pensando passo a passo: 1) Liste as palavras da frase. 2) Identifique a 5ª palavra. 3) Identifique a 3ª letra dessa palavra."*

**Resultado:** A resposta correta ("u") foi atingida perfeitamente ao forçar o modelo a "pensar em voz alta", como mostra a imagem abaixo.

<img width="935" height="846" alt="image" src="https://github.com/user-attachments/assets/447410f1-8532-42db-8b82-2bc2bcfb7468" />

## Conclusão: A Influência dos Tokens na Resposta da IA

A divisão de tokens influencia diretamente os acertos e erros da IA porque o modelo não enxerga "letras" ou "palavras", mas sim blocos numéricos (como vimos com os 15 tokens gerados na Etapa 1). Quando pedimos para a IA identificar a "terceira letra de uma palavra", ela tem dificuldade porque, para o modelo, aquela palavra pode ser um token indivisível ou dividida de forma não intuitiva. 

É exatamente por isso que técnicas como o *Chain-of-Thought* (Passo a Passo) são vitais. Ao forçar a IA a listar as palavras e depois soletrá-las, nós a obrigamos a gerar novos tokens intermediários. Esse "espaço para rascunho" permite que o modelo processe a lógica de forma estruturada e chegue à resposta correta, contornando a limitação de como ele processa a linguagem.
