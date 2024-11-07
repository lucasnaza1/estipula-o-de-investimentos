from time import sleep
aplicacao_mensal = float(input('Digite o valor a ser aplicado mensalmente: '))
valor_ativo = float(input('Qual o valor do ativo que pretende adquirir?'))
quantidade_cotas = int(aplicacao_mensal//valor_ativo)
rentabilidade_ativo = float(input('Quanto de dividendo, em média, o ativo está pagando?'))
meses = int(input('Digite quantos meses você quer especular: '))
print('----'*20)
primeiro_mes = quantidade_cotas * rentabilidade_ativo
ultimo_mes = (quantidade_cotas * meses) * rentabilidade_ativo
total_investido = aplicacao_mensal * meses
print('Calculando...')
print('----'*20)
sleep(1)
print('Aplicação no primeiro mês: R${:.2f}'.format(aplicacao_mensal))
print('----'*20)
print('Duração: {} meses'.format(meses))
print('----'*20)
print('Total investido em {} meses: R${:.2f}'.format(meses,total_investido))
print('----'*20)
print('Quantidade de cotas adquiridas por mês: {}'.format(quantidade_cotas))
print('----'*20)
print('quantidade de cotas adquiridas ao total: ', quantidade_cotas*meses)
print('----'*20)
print('Rendimento no primeiro mês: R${:.2f}'.format(primeiro_mes))
print('----'*20)
print('Rendimento no ultimo mês: R${:.2f}'.format(ultimo_mes))
print('----'*20)
print('Levando em conta que não haverá reaplicação de verba!!!')

