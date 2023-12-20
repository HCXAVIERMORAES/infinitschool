'''2)Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
 Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
valorGas = float(2.5)
valorAlcoo = float(1.9)
valorPago = float(0.0)
valorDesconto = float(0.0)
litroVendido = float(input('Digite quantos litros deseja abastecer: '))
tipoCombustivo =str(input('Digite o tipo de combustivel desejado (A-álcool, G-gasolina): '))
if(tipoCombustivo == 'A' or tipoCombustivo == 'a'):
  if(litroVendido <= 20):
    valorDesconto = (1 - (3/100)) * valorAlcoo
    valorPago = valorDesconto * litroVendido
  elif(litroVendido > 20):
    valorDesconto = (1 -(5/100)) * valorAlcoo
    valorPago = valorDesconto * litroVendido
else :
  if(litroVendido <= 20):
    valorDesconto = (1 - (4/100)) * valorGas
    valorPago = valorDesconto * litroVendido
  elif(litroVendido > 20):
    valorDesconto = (1 - (6/100))  * valorGas
    valorPago = valorDesconto * litroVendido

print('Foram abastecidos: ',litroVendido,'litros')
print('valor pago: R${:.2f}'.format(valorPago))
if tipoCombustivo == 'A' or tipoCombustivo == 'a':
  tipoCombustivo = 'Álcoo'
else :
  tipoCombustivo = 'Gasolina'
print('Tipo de combustivel: ',tipoCombustivo)
print('Valor pago com desconto: R${:.2f}'.format(valorDesconto),'por litro')
