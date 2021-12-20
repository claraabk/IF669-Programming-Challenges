lista = []
entrada = 'a'

while entrada != 'fim' :
    entrada = input()
    
    if entrada == 'adicionar':
        name = str(input())
        lista.append(name)
        print(f'{name} foi adicionada ao final da lista')
        
    elif entrada == 'remover':
        name = input()
        lista.remove(name)
        print(f'{name} foi removida da lista')
        
    elif entrada == 'atualizar posiçao' :
        name = input()
        indice = int(input())
        posicao_atual = lista.index(name)
        
        if posicao_atual == indice :
            print(f'Nada mudou, {name} ja esta na posiçao certa')
            
        else:
            lista.remove(name)
            lista.insert(indice,name)
            print(f'{name} foi inserida na posição {indice} da lista')

else:
    if len(lista) == 0 :
        print('Não sobraram pretendentes para voce, Ted')
    else:
            print(*lista)










