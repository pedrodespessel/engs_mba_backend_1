import random

numero_secreto = random.randint(1,10)
tentativas = 3
print('\n========================')
print('========================\n')
print('\nBem-vindo ao guess_game!\n')


while True:
    escolha = int(input('Escolha um número de 1 a 10:'))
    tentativas -= 1

    if escolha == numero_secreto:
        print(f'Parabéns, você acertou o número secreto ${numero_secreto} com ${3 - tentativas} tentativa(s)!')
        break
    elif escolha < numero_secreto:
        print('vc errou o número é maior')
        print('tentativas restantes:', tentativas)
    else:
        print('vc errou o número é menor.')
        print('tentativas restantes:', tentativas)

    if tentativas < 1:
        print(f'Suas tentativas acabaram, você perdeu! O número era ${numero_secreto}')
        break