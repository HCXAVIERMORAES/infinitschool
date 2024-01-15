'''[LP-A01] A partir do que aprendemos até agora:
    A) Crie um exemplo de cada uma das principais tipagens de variáveis.
   B) Crie uma solicitação de dados ao usuário.
   C) Imprima a solicitação anterior na tela com uma mensagem personalizada.'''
#A  Crie um exemplo de cada uma das principais tipagens de variáveis.
#tipo inteiro -> int
inteiro = 5
print(type(inteiro))

#tipo Tipo ponto flutuante -> float
ponto_flutuante = 3.1415
print(type(ponto_flutuante))

# Tipo string -> str
texto = 'Rato'
print(type(texto))

#tipo boolean -> bool
verdade = True
print(type(verdade))

#B Crie uma solicitação de dados ao usuário.
dados = str(input(f'Informe seu nome: '))

#C Imprima a solicitação anterior na tela com uma mensagem personalizada
print(f'Olá {dados}, Seja bem vindo!')
