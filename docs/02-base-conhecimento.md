# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e dar continuidade ao atendimento e ser mais eficiente |
| `perfil_investidor.json` | JSON | Personalizar o nosso agente e poder orientar de forma mais eficiente quanto ao tipo de investimentp |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que ele possa ensiar/orientar os clientes |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações para prover recomendações de controle de gastos |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Acrescentado o FFI ao arquivo de produto financeiro.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

Pode ser via injeção de dados diretamente no prompt (contrl + c, control + v) ou carregar os arquivos via código conforme exemplo abaixo:

````
import pandas as pd
import json

# CVS

historico = pd.read_cvs('data/historico_atendimento.cvs')
transacoes = pd.read_csv('data/trasacoes.csv')

# JSON

whith open('data/perfil_investido.json', 'r', encoding='utf-8') as f:
      perfil = json.load(f)

whith open('data/produto_financeiro.json', 'r', encoding='utf-8') as f:
      produtos = json.load(f)

````

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
pomos "injetar" os dados em nosso prompt, garantindo que o Agente possa ter o melhor contexto. Sendo que em soluções mais robustas, é mais recomendado que as injeções sejam carregadas dinâmicamente para que tenha mais flaxibilidade.
````
Dados do Cliente/Perfil (data/perfil_investidor.json):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

````
````

historico de atendimento do cliente (data/historico_atendimento.csv):


data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

````

````

Transações do Cliente (data/transacoes.csv):

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

````
````

Produtos disponíveis (data/produtos_financeiros.json):

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
   {
    "nome": "Fundo de Investimento Imobiliaros (FII's)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "6% 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

````

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.


O contexto abaixo, tem como base os dados originais da base de conhecimento,contudo foi sintetizado deixando as informações mais relevantes, sendo otimizado assim o consumo de tokens. Entretanto, vale ressaltar que é mais importante obter as informações relevantes disponíveis, do que economizar tokens.
```
Dados do Cliente:

- Nome: João Silva
- Perfil: Moderado
- Objetivo principal: Construir reserva de emergência
- Patrimonio Total: 15000.00
- Reserva Atual: R$ 10.000.00 (meta R$ 15.000)

````
````
Resumo de Gastos:

- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Laser: R$ 55,90
- Total de saída: R$ 2.488,90

````
````
Produtos disponíveis para aplicação:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo de Ivestimento Imobiliário (risco médio)
- CDB Multimercado (risco médio)
- Fundo de Ações (risco alto)

````
