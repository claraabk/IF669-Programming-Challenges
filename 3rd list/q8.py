# 1 input
qt_votos = int(input())

# Lista dos Shelbys p/ comparar e contabilizar os votos
lista_votos = []

# Input votos
for i in range(qt_votos):
    votador, voto = input().split(': ')

    if 'Shelby' in voto:
        lista_votos.append(voto)

# Lista dos votos nos Shelbys sem repetição
lista_unica = list(set(lista_votos))

# Variáveis iniciais p/ modificar
mais_votado = 0
segundo = 0
vencedor = 'a'
segundo_lugar = 'b'

# Alterando as variáveis de acordo com a votação

if len(lista_unica) > 1:
    for indice in range(len(lista_unica)):

        if lista_votos.count(lista_unica[indice]) > mais_votado:

            segundo, mais_votado = mais_votado, lista_votos.count(lista_unica[indice])
            segundo_lugar, vencedor = vencedor, lista_unica[indice]

            porcentagem2 = (100 * segundo) / qt_votos
            porcentagem = (100 * mais_votado) / qt_votos
            
        elif lista_votos.count(lista_unica[indice]) < mais_votado and lista_votos.count(lista_unica[indice]) > segundo :
          
          segundo = lista_votos.count(lista_unica[indice])
          segundo_lugar = lista_unica[indice]
          porcentagem2 = ( 100 * segundo ) / qt_votos

    if vencedor == 'Thomas Shelby' and porcentagem > 50:
        print(
            f'{vencedor} ganhou a eleição com {porcentagem:.2f}% dos votos e continuara sendo o líder dos Peaky Blinders!!!')

    elif porcentagem > 50:
        print(
            f'Assumindo o lugar de Tommy, {vencedor} agora é o novo líder da gangue vencendo a eleição com {porcentagem:.2f}% dos votos!')

    elif porcentagem < 50 :
        if vencedor == 'Thomas Shelby' or segundo == 'Thomas Shelby':
            print(
                f'Precisaremos ter uma segunda rodada entre os membros {vencedor} e {segundo_lugar}, que tiveram respectivamente {porcentagem:.2f}% e {porcentagem2:.2f}% dos votos, Tommy ainda está na disputa.')

        else:
            print(
                f'Precisaremos ter uma segunda rodada entre os membros {vencedor} e {segundo_lugar}, que tiveram respectivamente {porcentagem:.2f}% e {porcentagem2:.2f}% dos votos, teremos um novo líder!')

elif len(lista_unica) == 1:
    vencedor = lista_unica[0]
    votos = lista_votos.count(lista_votos[0])
    porcentagem = (100 * votos) / qt_votos

    if porcentagem > 50:
        if vencedor == 'Thomas Shelby':
            print(
                f'{vencedor} ganhou a eleição com {porcentagem:.2f}% dos votos e continuara sendo o líder dos Peaky Blinders!!!')
        else:
            print(
                f'Assumindo o lugar de Tommy, {vencedor} agora é o novo líder da gangue vencendo a eleição com {porcentagem:.2f}% dos votos!')
    elif porcentagem < 50:
        print('Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!')

elif len(lista_unica) == 0:
    print('Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!')
