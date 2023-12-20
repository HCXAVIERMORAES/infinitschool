'''[PY-A01] Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.'''
senha = '1234'
emai = 'fernanda@gmail.com'
contador = 3
correto = True
print('*************************')
print('---CADASTRO DE USUARIO---')
print('*************************')
print('Confirme seu email e sua senha!')
while correto == True:
  email_digitado = input('Digite seu email: ')
  senha_digitada = input('Digite sua senha: ')
  if senha_digitada == senha and email_digitado == emai:
    print('Seja bem vindo!!')
    print('Continue com o cadastro.....')
    break
  else:
    contador -= 1
    print('senha ou email incorreto.')
    print(f'Você tem mais {contador} tentativas..')
    if contador == 0:
      correto = False
      print('Fim do programa.')
