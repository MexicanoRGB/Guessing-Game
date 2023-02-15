import random

print('*************************************************')
print('Seja Muito Bem Vindo Ao Nosso Jogo De Adivinhação')
print('*************************************************')

Numero_Secreto = random.randrange(1,1000)
Total_De_Tentativas = 0
Pontos = 1000
Pontos_Perdidos = 0
Rodada = 0
print('Qual O Nivel De Dificuldade?')
print('(1) Fácil (2) Médio (3)Difícil')
nivel = int(input('Defina O Nivel: '))

if(nivel == 1):
    Total_De_Tentativas = 30
    Pontos_Perdidos = 25
elif(nivel == 2):
    Total_De_Tentativas = 20
    Pontos_Perdidos = 50
else:
    Total_De_Tentativas = 10
    Pontos_Perdidos = 100

for Rodada in range(Total_De_Tentativas):
    print("\nTentativa {} de {}".format(Rodada, Total_De_Tentativas))

    chute = int(input("Digite Um Número Entre 1 e 1000: "))
    print('\nVocê Digitou' , chute)

    if(chute < 1 or chute > 1000):
        print('Voce Deve Digitar Um Número Entre 1 e 1000')
        continue

    acertou = bool(chute == Numero_Secreto)
    maior = bool(chute > Numero_Secreto)
    menor = bool(chute < Numero_Secreto)

    if(acertou == True):
        print('Você Acertou E Fez {} Pontos!!'.format(Pontos))
        break
    else:
        Pontos = Pontos - Pontos_Perdidos  
            
        if(maior):
            print('Você Errou! o seu chute foi Maior do que o Número Secreto.')
        elif(menor):
            print('Você Errou! o seu chute foi Menor do que o Número Secreto.')
            print('Minimo{}'.format(chute))
    
    Rodada = Rodada +1

if(Rodada == Total_De_Tentativas):
    print('O número secreto era: {}'.format(Numero_Secreto))

print('fim de jogo')
input()        