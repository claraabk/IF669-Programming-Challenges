#Função : Percorrer o mapa até achar o 'O' ou entrar em um beco sem saída
def funcao_caminho(mapa,posicao_y,posicao_x,dimensao):

    # CASO BASE
    # O Ponto 'O' de saída está a Sul
    if posicao_y+1 < dimensao and mapa[posicao_y+1][posicao_x] == 'O' :
        # Ponto = F
        mapa[posicao_y + 1][posicao_x] = 'F'
        # Printando o mapa : Para cada linha printe c/ join
        for w in range(dimensao):
            print(''.join(mapa[w]))

        # Printando mensagem de direção
        print('Por aqui meus amigos vamos pelo Sul\n')

        return 1

    # O Ponto 'O' de saída está a Leste
    elif posicao_x+1 < dimensao and mapa[posicao_y][posicao_x+1] == 'O' :
        #Novo ponto = F
        mapa[posicao_y][posicao_x+1] = 'F'
        #Printando o mapa : Para cada linha printe c/ join
        for w in range(dimensao) :
            print(''.join(mapa[w]))

        #Printando mensagem de direção
        print('Por aqui meus amigos vamos pelo Leste\n')

        return 1

    # O Ponto 'O' de saída está a Norte
    elif posicao_y > 0 and mapa[posicao_y-1][posicao_x] == 'O' :
        #Novo ponto = F
        mapa[posicao_y-1][posicao_x] = 'F'
        #Printando o mapa : Para cada linha printe c/ join
        for w in range(dimensao) :
            print(''.join(mapa[w]))

        #Printando a mensagem de direção
        print('Por aqui meus amigos vamos pelo Norte')

        return 1

    ## O Ponto 'O' de saída está a Oeste
    elif posicao_x > 0 and mapa[posicao_y][posicao_x-1] == 'O' :
        #Novo ponto = F
        mapa[posicao_y][posicao_x-1] = 'F'
        #Printando novo mapa : Para cada linha printe c/ join
        for w in range(dimensao) :
            print(''.join(mapa[w]))

        #Printando a mensagem de direção
        print('Por aqui meus amigos vamos pelo Oeste\n')

        return 1

    #Não entrando no caso base
    else:

        #Condição : O ponto ta no Sul
        if posicao_y+1 < dimensao and mapa[posicao_y+1][posicao_x] == '.' :
            #Ponto = F
            mapa[posicao_y+1][posicao_x] = 'F'
            #Printando o mapa : Para cada linha printe c/ join
            for w in range(dimensao) :
                print(''.join(mapa[w]))

            #Printando mensagem de direção
            print('Por aqui meus amigos vamos pelo Sul\n')

            #Nova posição y
            posicao_y = posicao_y + 1

            #Chamando a função com o novo mapa
            return funcao_caminho(mapa,posicao_y,posicao_x,dimensao)

        #Condição : O ponto está a Leste
        elif posicao_x+1 < dimensao and mapa[posicao_y][posicao_x+1] == '.' :
            #Novo ponto = F
            mapa[posicao_y][posicao_x+1] = 'F'
            #Printando o mapa : Para cada linha printe c/ join
            for w in range(dimensao) :
                print(''.join(mapa[w]))

            #Printando mensagem de direção
            print('Por aqui meus amigos vamos pelo Leste\n')

            #Nova posição x
            posicao_x = posicao_x + 1

            #Chamando a função com novo mapa
            return funcao_caminho(mapa,posicao_y,posicao_x,dimensao)

        #Condição : O ponto está a Norte
        elif posicao_y > 0 and mapa[posicao_y-1][posicao_x] == '.' :
            #Novo ponto = F
            mapa[posicao_y-1][posicao_x] = 'F'
            #Printando o mapa : Para cada linha printe c/ join
            for w in range(dimensao) :
                print(''.join(mapa[w]))

            #Printando a mensagem de direção
            print('Por aqui meus amigos vamos pelo Norte')

            #Nova posição y
            posicao_y = posicao_y-1

            #Chamando a função com novo mapa
            return funcao_caminho(mapa,posicao_y,posicao_x,dimensao)

        #Condição : O ponto está a Oeste
        elif posicao_x > 0 and mapa[posicao_y][posicao_x-1] == '.' :
            #Novo ponto = F
            mapa[posicao_y][posicao_x-1] = 'F'
            #Printando novo mapa : Para cada linha printe c/ join
            for w in range(dimensao) :
                print(''.join(mapa[w]))

            #Printando a mensagem de direção
            print('Por aqui meus amigos vamos pelo Oeste\n')

            #Nova direção x
            posicao_x = posicao_x - 1

            #Chamando a função com novo mapa
            return funcao_caminho(mapa, posicao_y, posicao_x, dimensao)

        else:
            return funcao_caminho(mapa,posicao_y,posicao_x,dimensao)

#Input : Dimensão do mapa
dimensao = int(input())

#Posição X e Y inicial
posicao_y = int(input())
posicao_x = int(input())

#Lista inicial pra formar o mapa
mapa = []

#Loop p/ formar lista de listas
for i in range(dimensao) :
    #P/ cada linha novo input
    nova_linha = input()
    #Formando uma lista diferente com cada linha
    nova_linha = list(nova_linha)
    #Apendando na lista mapa
    mapa.append(nova_linha)

#Erro de recursão ( Loop infinito - não encontrou saída 'O' )
try:
    if funcao_caminho(mapa, posicao_y, posicao_x, dimensao) == 1 :
        for w in range(dimensao):
            print(''.join(mapa[w]))
        print('Conseguimos!!')

except RecursionError :
    print('Amigos a jornada foi incrível, porém ela acaba por aqui...')

