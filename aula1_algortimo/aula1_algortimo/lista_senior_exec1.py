'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado
informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
salarioAtual = float(input('Digite o salário atual do funcionario: R$'))
novoSalario = 0.0

if(salarioAtual <= 280.00):
  reajuste = float(20/100)
  percentual = '20'
  novoSalario = salarioAtual + (salarioAtual*reajuste)
  aumento = float(novoSalario - salarioAtual)
elif(salarioAtual > 280.0 and salarioAtual < 700.0):
   reajuste = float(15/100)
   percentual = '15'
   novoSalario = salarioAtual + (salarioAtual*reajuste)
   aumento = float(novoSalario - salarioAtual)
elif(salarioAtual >= 700.0 and salarioAtual < 1500.0):
   reajuste = float(10/100)
   percentual = '10'
   novoSalario = salarioAtual + (salarioAtual*reajuste)
   aumento = float(novoSalario - salarioAtual)
else :
   reajuste = float(5/100)
   percentual = '5'
   novoSalario = salarioAtual + (salarioAtual*reajuste)
   aumento = float(novoSalario - salarioAtual)

#salário antes do reajuste
print(f'O salário antes do reajuste era: R${salarioAtual}')
#percentual de aumento
print(f'O reajuste foi de {percentual}%')
#valor do aumento
print(f'O valor do aumento foi de R${aumento} ')
#novo salario
print(f'O novo salarioo é: R${novoSalario}')
print('Obrigado!!!')
