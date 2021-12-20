#Funcao p/surfe
def surfe(moedas,tempo) :
    moedas_ganhas = ( tempo + moedas ) / 2

    return int(moedas_ganhas)

#Funcao p/ pescaria
def pescaria(moedas) :

    if moedas % 2 == 0 :
        moedas = ( moedas % 7 ) * 6

    else :
        moedas = ( moedas % 7 ) ** 2

    return int(moedas)

#Funcao p/ danca
def danca(moedas) :
    
    if moedas % 10 == 0 :
        moedas += 5

    else :
        while moedas % 10 != 0 :
            moedas += 1

    return moedas

#Funcao p/ jogo aqua
def aqua(moedas) :
    termo = str(int(moedas))
    lista = list(termo)
    moedas_soma = 0

    for i in range(len(lista)) :
        moedas_soma += int(lista[i])

    return moedas_soma

#Tempo, moeda e jogos no comeco do jogo
tempo = 0
moedas = 10
qt_jogos = 0

#Continuar input enquanto n bate 2 min
while tempo < 120 :
    jogo = input()

    #Aplicando as funcoes dependendo do jogo escolhido
    if jogo == 'Surfe' :
        moedas += surfe(moedas,tempo)
        tempo += 20
        qt_jogos += 1
        print(f'O pinguim acabou de concluir o jogo Surfe na Caçamba e agora possui {moedas} moedas.')

    elif jogo == 'Pescaria' :
        moedas += pescaria(moedas)
        tempo += 30
        qt_jogos += 1
        print(f'O pinguim acabou de concluir o jogo Pescaria no Gelo e agora possui {moedas} moedas.')

    elif jogo == 'Danca' :
        moedas = danca(moedas)
        tempo += 15
        qt_jogos += 1
        print(f'O pinguim acabou de concluir o jogo Concurso de Dança e agora possui {moedas} moedas.')

    elif jogo == 'Aqua' :
        moedas += aqua(moedas)
        tempo += 50
        qt_jogos += 1
        print(f'O pinguim acabou de concluir o jogo Aquagrabber e agora possui {moedas} moedas.')

#Print final
else:
    print(f'\nParabens! Você terminou o Circuito Pinguim, participando de {qt_jogos} jogos e acumulando a quantia de {moedas} moedas.')



