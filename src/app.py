
import pandas as pd
import json

# ============== CARREGAR DADOS =================

#csv
historico = pd.read_csv('data/historico_atendimento.cvs')
transacoes = pd.read_csv('data/trasacoes.csv')

#JSON
perfil = json.load(open('data/perfil_investido.json'))
produtos = json.load( open('data/produto_financeiro.json'))


#=============== MONTAR CONTEXTO ==============

contexto =f"""
Cliente: {perfil['nome']}, {perfil['idade']} anos, perfil{perfil['perfil_investidor']}
Objetivo: {perfil['objetivo-principal']}
Patrimônio: R$ {perfil['patrimonio_total']}, | RESERVA: R$ {perfil['reserva_emergencia_atual']} 

Transações recentes:
{trasacoes.ro_string(index=False)}

Atendimento Anteriores:
{historico.to_string(index=False)}

Produtos Disponíveis:
{json.dump(produ, index=2, ensure_ascii=False)}

"""