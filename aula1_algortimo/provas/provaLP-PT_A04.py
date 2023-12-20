'''LP-PY-A04- Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência até que ele acerte. Para ajudar o usuário, o programa deve informar se o número é maior ou menor que o número a ser adivinhado. Ao final, imprima o número adivinhado e a quantidade de tentativas.'''

import random

# Escolha do número aleatório
num_adivinhar = random.randint(1, 30)
# Inicialização das variáveis
tentativas = 0
adivinhar = False

print('**********************************')
print('---- TENTE ADIVINHAR O NÚMERO ----')
print('**********************************')
# Loop  adivinhar número
while not adivinhar:
    tentativa = int(input("Digite um número: "))
    tentativas += 1

    if tentativa == num_adivinhar:
        adivinhar = True
    elif tentativa < num_adivinhar:
        print("Não deu... Tente um número maior.")
    else:
        print("Quase.... Tente um número menor.")

# Impressão do resultado
print(f"Parabéns! Você adivinhou o número {num_adivinhar} em {tentativas} tentativas.")
