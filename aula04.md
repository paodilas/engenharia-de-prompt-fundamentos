# Laboratório: O Motor Cognitivo e Framework RTF

## Tarefa 1: Matriz de Execução (O Caos vs. A Estrutura)

**Tema escolhido:** O que é uma API?

### Resultado 1: Persona "Pirata Engraçado"
> "Ahoy, marujo dos sete mares de silício! Imagine que você tá numa taverna com a barriga roncando. Você não vai invadir a cozinha do capitão pra roubar a carne, certo? Você chama o garçom! Arrr! A API é exatamente o garçom do seu navio digital! Você (o aplicativo) entrega o seu mapa do tesouro (pedido) pra ela, a API navega até a cozinha (o servidor de dados), pega o ouro e joga direto no seu convés! Sem a API, nossos navios de código não conseguiriam trocar farpas nem tesouros pela internet! Yo-ho-ho!"

### Resultado 2: Persona "Arquiteto de Sistemas de Nível Mundial"
> "Uma API (Application Programming Interface) atua como um contrato formal e padronizado de comunicação entre sistemas de software distintos. Como arquiteto, projeto APIs como camadas de abstração cruciais: elas expõem funcionalidades ou dados de um backend sem revelar sua lógica interna de implementação. Operando geralmente sobre protocolos robustos como HTTP/REST, GraphQL ou gRPC, as APIs garantem que microserviços, bancos de dados e aplicações front-end interajam de forma segura, escalável e totalmente agnóstica em relação à linguagem de programação subjacente."

### Análise Crítica: Qual texto foi mais tecnicamente preciso e por quê?
O texto do **Arquiteto de Sistemas** foi infinitamente mais preciso. Enquanto a persona do pirata utilizou analogias lúdicas (garçom, taverna, navios) úteis apenas para leigos entenderem o *conceito* básico de requisição/resposta, a persona do arquiteto utilizou terminologia técnica exata (*camada de abstração, protocolos, HTTP/REST, microserviços, agnóstica*). O arquiteto explicou não apenas o que a API faz, mas a sua **função estrutural** na engenharia de software (segurança, escalabilidade e padronização).

---

## Tarefa 2: O Framework RTF (Role, Task, Format)

**Prompt Utilizado:**
*Você é um instrutor de Python experiente. Crie uma função que calcule a média de uma lista de números, incluindo tratamento de erros rigoroso para listas vazias. Forneça o código Python amplamente comentado, seguido de exatos 3 casos de teste.*

**Resultado Gerado pela IA:**

```python
def calcular_media(numeros):
    """
    Calcula a média aritmética de uma lista de números.
    
    Parâmetros:
    numeros (list): Uma lista contendo valores numéricos (int ou float).
    
    Retorna:
    float: O valor da média calculada.
    
    Levanta:
    ValueError: Se a lista estiver vazia.
    TypeError: Se a lista contiver elementos não numéricos.
    """
    
    # Verificação rigorosa: Impede o processamento de listas vazias para evitar ZeroDivisionError
    if not numeros:
        raise ValueError("Erro: A lista de números não pode estar vazia.")
        
    # Verificação de tipo: Garante que todos os elementos iterados sejam números
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Erro: A lista deve conter apenas valores numéricos (inteiros ou decimais).")
        
    # Calcula a soma de todos os elementos e divide pelo comprimento da lista
    soma_total = sum(numeros)
    quantidade_elementos = len(numeros)
    
    return soma_total / quantidade_elementos
# 3 CASOS DE TESTE (Como solicitado)
# Caso de Teste 1: Caminho feliz (Lista válida com números mistos)
try:
    print("Teste 1 (Lista Válida):", calcular_media([10, 20.5, 30, 40.5])) 
    # Saída esperada: 25.25
except Exception as e:
    print(e)

# Caso de Teste 2: Tratamento de Erro Rigoroso (Lista Vazia)
try:
    print("Teste 2 (Lista Vazia):", calcular_media([]))
except ValueError as e:
    print(f"Teste 2 Capturado com sucesso -> {e}") 
    # Saída esperada: Erro: A lista de números não pode estar vazia.

# Caso de Teste 3: Tratamento de Erro de Tipagem (String na lista)
try:
    print("Teste 3 (Dados Inválidos):", calcular_media([10, "vinte", 30]))
except TypeError as e:
    print(f"Teste 3 Capturado com sucesso -> {e}")
    # Saída esperada: Erro: A lista deve conter apenas valores numéricos...

## Ação Final: Resposta Argumentativa
**Como a definição explícita de um papel (Persona) alterou a qualidade e a estrutura técnica da resposta da Inteligência Artificial?**
A definição explícita da Persona altera drasticamente a forma como a IA processa a linguagem. Quando não definimos um papel, a IA busca uma resposta no "centro" de sua base de dados, gerando textos medianos e genéricos. Porém, ao impor uma Persona técnica (como "Instrutor de Python" ou "Arquiteto de Sistemas"), forçamos o modelo a buscar relações estatísticas em um subconjunto altamente especializado de dados. 
Como resultado, a qualidade da resposta dá um salto: o vocabulário se torna rigoroso e preciso (abandonando analogias muito simplistas), a estrutura da informação ganha formatação profissional (comentários precisos, tratamento de exceções) e o nível de profundidade resolve problemas reais de engenharia. A Persona, portanto, funciona como uma "lente de foco", transformando o conhecimento difuso da IA em uma entrega técnica de alto nível.
