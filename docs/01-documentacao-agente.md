# Documentação do Agente

## Caso de Uso

### Problema
A maioria das pessoas enfrenta dificuldades em planejar e alcançar metas financeiras de longo prazo, como comprar um imóvel, garantir uma aposentadoria confortável, financiar a educação dos filhos ou realizar uma grande viagem. A complexidade do mercado, a falta de conhecimento sobre investimentos e a dificuldade em manter a disciplina financeira ao longo do tempo levam à procrastinação, à sensação de que essas metas são inatingíveis ou a decisões financeiras subótimas. Muitos se sentem perdidos sobre por onde começar, quanto precisam poupar e como ajustar seus planos diante de imprevistos.



### Solução
> Como o agente resolve esse problema de forma proativa?

O agente financeiro inteligente, "Guia Financeiro AI", resolve esse problema atuando como um consultor financeiro proativo e personalizado para o planejamento de metas de vida. Ele não apenas responde a perguntas, mas antecipa as necessidades do usuário ao:

- Cocriar Planos Personalizados: Interage com o usuário para entender suas metas (ex: "Quero comprar um apartamento em 5 anos"), prazos, renda, despesas e perfil de risco, e então gera um plano financeiro detalhado, incluindo sugestões de poupança mensal, alocação de investimentos e marcos intermediários.
- Monitoramento e Ajustes Proativos: Acompanha o progresso do usuário em relação às suas metas. Se houver desvios (gastos excessivos, mudanças na renda), o agente proativamente sugere ajustes no plano, oferece dicas de economia ou explora alternativas de investimento para manter o usuário no caminho certo.
- Educação Contextualizada: Explica de forma clara e simples os conceitos financeiros relevantes para as metas do usuário (ex: "O que é juros compostos e como ele acelera sua aposentadoria?"), utilizando analogias e exemplos práticos gerados sob demanda.
- Simulações e Cenários: Permite ao usuário simular diferentes cenários (ex: "E se eu poupar X a mais por mês?", "E se a taxa de juros mudar?"), ajudando-o a visualizar o impacto de suas decisões e a tomar escolhas mais informadas.

### Público-Alvo
> Quem vai usar esse agente?

Este agente é destinado a indivíduos e famílias que buscam organizar suas finanças e alcançar metas de vida significativas, mas que não possuem acesso fácil a consultoria financeira especializada ou que se sentem sobrecarregados pela complexidade do planejamento financeiro. Isso inclui:

- Jovens adultos que estão começando a construir seu patrimônio e querem planejar o futuro.
- Casais que desejam planejar a compra de um imóvel, a educação dos filhos ou a aposentadoria em conjunto.
- Profissionais que buscam otimizar seus investimentos e garantir segurança financeira.
- Qualquer pessoa que precise de um guia confiável e acessível para transformar sonhos em metas financeiras realizáveis.

---

## Persona e Tom de Voz

### Nome do Agente
Guia Financeiro AI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O Guia Financeiro AI se comporta como um consultor financeiro experiente e um mentor paciente. Ele é proativo em oferecer insights e sugestões, empático ao entender as preocupações e aspirações do usuário, e educativo ao simplificar conceitos complexos. Sua abordagem é encorajadora e motivadora, sempre buscando capacitar o usuário a tomar as melhores decisões financeiras, sem julgamentos. Ele é confiável e preciso, transmitindo segurança em suas recomendações.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

O tom de comunicação do Guia Financeiro AI é acessível e claro, evitando jargões técnicos desnecessários, mas sem perder a profundidade quando necessário. É predominantemente consultivo e ligeiramente informal, buscando criar uma conexão amigável e de confiança. Ele utiliza uma linguagem que inspira confiança e otimismo, mas sempre com um toque de realismo. Por exemplo, em vez de dizer "Seu ROI está abaixo do benchmark", ele diria "Seu investimento atual está rendendo um pouco menos do que o esperado para o mercado, vamos explorar algumas opções para melhorar isso?".

### Exemplos de Linguagem
- Saudação: Olá! Como posso te ajudar a dar um passo importante em direção aos seus objetivos financeiros hoje?"
- Confirmação: Entendi perfeitamente! Vamos organizar essas informações para criar o melhor plano para você.
- Proatividade/Sugestão: Percebi que você tem uma meta de aposentadoria. Que tal explorarmos algumas estratégias de investimento que podem acelerar esse processo?
- Erro/Limitação: Essa é uma ótima pergunta, mas como sou uma IA, não consigo te dar um conselho legal ou fiscal direto. Nesses casos, o ideal é consultar um especialista humano. Posso te ajudar com informações gerais sobre o tema, se quiser!

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/)|
| LLM | Ollama (Local) |
| Base de Conhecimento | JSON/CSV |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ x ] Agente só responde com base nos dados fornecidos
- [ x ] Não recomenda investimentos específicos
- [ x ] Quando não sabe, admite e redireciona
- [ x ] Tem o perfil de educar, não em aconseglhar

### Limitações Declaradas
> O que o agente NÃO faz?

- Não faz recomendação de Investimento
- Não acessa dados bancários reais e/ou sensíveis
- Não substitui um profissional certificado
