movimento_1 = str(input())

if movimento_1!='cima' and movimento_1!='baixo' and movimento_1!='esquerda' and movimento_1!='direita':
    print('O jogador nao fez nenhuma entrada valida')
else:
    movimento_2 = str(input())
    if movimento_2==movimento_1:
        print('O jogador fez somente 1 movimento(s)')
    elif (movimento_1=='cima' and movimento_2=='baixo') or (movimento_1=='baixo' and movimento_2=='cima') or (movimento_1=='esquerda' and movimento_2=='direita') or (movimento_1=='direita' and movimento_2=='esquerda'):
        print('O jogador fez somente 1 movimento(s)')
    elif movimento_2!='cima' and movimento_2!='baixo' and movimento_2!='esquerda' and movimento_2!='direita':
        print('O jogador fez 1 movimento(s) e tentou uma entrada invalida')
    else:
        movimento_3=str(input())
        if movimento_3==movimento_2:
            print('O jogador fez somente 2 movimento(s)')
        elif (movimento_2=='cima' and movimento_3=='baixo') or (movimento_2=='baixo' and movimento_3=='cima') or (movimento_2=='esquerda' and movimento_3=='direita') or (movimento_2=='direita' and movimento_3=='esquerda'):
            print('O jogador fez somente 2 movimento(s)')
        elif movimento_3!='cima' and movimento_3!='baixo' and movimento_3!='esquerda' and movimento_3!='direita':
            print('O jogador fez 2 movimento(s) e tentou uma entrada invalida')
        else:
            movimento_4 = str(input())
            if movimento_4==movimento_3:
                print('O jogador fez somente 3 movimento(s)')
            elif (movimento_3=='cima' and movimento_4=='baixo') or (movimento_3=='baixo' and movimento_4=='cima') or (movimento_3=='esquerda' and movimento_4=='direita') or (movimento_3=='direita' and movimento_4=='esquerda'):
                print('O jogador fez somente 3 movimento(s)')
            elif movimento_4!='cima' and movimento_4!='baixo' and movimento_4!='esquerda' and movimento_4!='direita':
                print('O jogador fez 3 movimento(s) e tentou uma entrada invalida')
            else:
                movimento_5 = str(input())
                if movimento_5==movimento_4:
                    print('O jogador fez somente 4 movimento(s)')
                elif (movimento_4=='cima' and movimento_5=='baixo') or (movimento_4=='baixo' and movimento_5=='cima') or (movimento_4=='esquerda' and movimento_5=='direita') or (movimento_4=='direita' and movimento_5=='esquerda'):
                    print('O jogador fez somente 4 movimento(s)')
                elif movimento_5!='cima' and movimento_5!='baixo' and movimento_5!='esquerda' and movimento_5!='direita':
                    print('O jogador fez 4 movimento(s) e tentou uma entrada invalida')
                else:
                    print('O jogador conseguiu fazer todos 5 movimentos com sucesso!')