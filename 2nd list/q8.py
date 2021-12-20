#Pontuacao inicial
djoko = 0
federer = 0

#Loop p/ contabilizar a pontuacao 
while  djoko < 4 and federer <4 :
    novo_ponto = input()
    if novo_ponto == 'djoko' :
        djoko += 1
    elif novo_ponto == 'federer' :
        federer += 1
else :
    while djoko - federer < 2 and federer - djoko <2 :
        nova_pontuacao = input()
        if nova_pontuacao == 'djoko' :
            djoko += 1
        elif nova_pontuacao =='federer':
            federer += 1
    else:
        if federer > djoko:
            print(f'Roger federer ganhou o game com a pontuacao de {federer} a {djoko}!')
        elif djoko > federer :
            print(f'Djokovic ganhou o game com a pontuacao de {djoko} a {federer}!')
