#Input qt de competidores
qt_competidores = int(input())

#Inputs 1 competidor
nome1 = input()
pontuacao1 = 0
manobra = 'a'

while manobra != 'Fim' :
    manobra = input()
    if manobra == 'Gap':
        pontuacao1 += 10
    elif manobra == 'Barspin':
        pontuacao1 += 30
    elif manobra == 'Superhomem':
        pontuacao1 += 100
    elif manobra == 'Rotacao de 360':
        pontuacao1 += 50
    elif manobra == 'Rotacao de 720':
        pontuacao1 += 150
    elif manobra == 'Rotacao de 1080':
        pontuacao1 += 400
    elif manobra == 'Backflip':
        pontuacao1 += 250
    elif manobra == 'Frontflip':
        pontuacao1 += 500


#Variáveis p/ comparar no final
melhor_pontuacao = pontuacao1
segunda_pontuacao = 0
terceira_pontuacao = 0
nome_campeao = nome1
nome_segundo = nome1
nome_terceiro = nome1

#Inputs p/ o resto dos competidores
for i in range(1,qt_competidores):
    nome = input()
    pontuacao = 0
    manobra2 = 'a'

    while manobra2 != 'Fim':
        manobra2 = input()
        if manobra2 == 'Gap':
            pontuacao += 10
        elif manobra2 == 'Barspin':
            pontuacao += 30
        elif manobra2 == 'Superhomem':
            pontuacao += 100
        elif manobra2 == 'Rotacao de 360':
            pontuacao += 50
        elif manobra2 == 'Rotacao de 720':
            pontuacao += 150
        elif manobra2 == 'Rotacao de 1080':
            pontuacao += 400
        elif manobra2 == 'Backflip':
            pontuacao += 250
        elif manobra2 == 'Frontflip':
            pontuacao += 500
    
    #Comparação entre as pontuacoes p/ determinar ordem
    if pontuacao > melhor_pontuacao and pontuacao > segunda_pontuacao and pontuacao > terceira_pontuacao :
        terceira_pontuacao, segunda_pontuacao, melhor_pontuacao = segunda_pontuacao, melhor_pontuacao, pontuacao
        nome_terceiro, nome_segundo, nome_campeao = nome_segundo, nome_campeao, nome

    elif pontuacao < melhor_pontuacao and pontuacao > segunda_pontuacao and pontuacao > terceira_pontuacao :
        terceira_pontuacao, segunda_pontuacao = segunda_pontuacao, pontuacao
        nome_terceiro, nome_segundo = nome_segundo, nome

    elif pontuacao < melhor_pontuacao and pontuacao < segunda_pontuacao and pontuacao > terceira_pontuacao :
        terceira_pontuacao = pontuacao
        nome_terceiro = nome

    elif pontuacao == melhor_pontuacao and pontuacao > segunda_pontuacao and pontuacao > terceira_pontuacao :
        terceira_pontuacao, segunda_pontuacao = segunda_pontuacao, pontuacao
        nome_terceiro, nome_segundo = nome_segundo, nome

    elif pontuacao < melhor_pontuacao and pontuacao == segunda_pontuacao and pontuacao > terceira_pontuacao :
        terceira_pontuacao = pontuacao
        nome_terceiro = nome

#Print
print(f'{nome_campeao}\n{melhor_pontuacao}\n{nome_segundo}\n{segunda_pontuacao}\n{nome_terceiro}\n{terceira_pontuacao}')