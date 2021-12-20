#Qt inicial e do bunker
qt_pre = int(input())
qt_bunker = int(input())

#Qt inicial de cada profissao
medicina = 0
engenharia = 0
ciencia = 0
docencia = 0

#Lista inicial nome e profissao
lista_nomes = []
lista_profissoes = []

#Inputs para a pre-selecao
for i in range(qt_pre) :
    nome, profissao = input().split(': ')
    lista_nomes.append(nome)
    lista_profissoes.append(profissao)

    if profissao == 'Engenheiro(a)' :
        engenharia += 1
        
        if engenharia == qt_bunker/4 :
            print('Conseguimos chegar a quantidade maxima de Engenheiros')
    
    elif profissao == 'Cientista' :
        ciencia += 1
        
        if ciencia == qt_bunker/4:
          print('Conseguimos chegar a quantidade maxima de Cientistas')
          
    elif profissao == 'Professor(a)' :
        docencia += 1
        
        if docencia == qt_bunker/4 :
          print('Conseguimos chegar a quantidade maxima de Professores')
        
    elif profissao == 'Medico(a)' :
        medicina += 1
        
        if medicina == qt_bunker/4 :
          print('Conseguimos chegar a quantidade maxima de Medicos')

#Input p/ novas seleçoes 
#Caso n tenha chegado na qt maxima
if qt_pre < qt_bunker :

    try :
        while True :
          #Novo comando
            comando = input()

            if comando == 'buscar' :
                pessoa = input()

                if pessoa in lista_nomes :
                    print(f'{pessoa} ja esta no bunker')

                else :
                    print(f'{pessoa} ainda não chegou no bunker...')

            elif comando == 'adicionar' :
                nome2, profissao2 = input().split(': ')

                if profissao2 == 'Engenheiro(a)' and engenharia < qt_bunker/4 :
                    lista_nomes.append(nome2)
                    lista_profissoes.append(profissao2)
                    engenharia += 1

                    if engenharia == qt_bunker/4 :
                        print('Conseguimos chegar a quantidade maxima de Engenheiros')

                elif profissao2 == 'Cientista' and ciencia < qt_bunker/4 :
                    lista_nomes.append(nome2)
                    lista_profissoes.append(profissao2)
                    ciencia += 1

                    if ciencia == qt_bunker/4 :
                        print('Conseguimos chegar a quantidade maxima de Cientistas')

                elif profissao2 == 'Professor(a)' and docencia < qt_bunker/4 :
                    lista_nomes.append(nome2)
                    lista_profissoes.append(profissao2)
                    docencia += 1

                    if docencia == qt_bunker/4 :
                        print('Conseguimos chegar a quantidade maxima de Professores')

                elif profissao2 == 'Medico(a)' and medicina < qt_bunker/4 :
                    lista_nomes.append(nome2)
                    lista_profissoes.append(profissao2)
                    medicina += 1

                    if medicina == qt_bunker/4 :
                        print('Conseguimos chegar a quantidade maxima de Medicos')

            else:
                print('**COMANDO INVALIDO**')

    except :
      
        #Testando se chegou na qt maxima 
        if len(lista_nomes) < qt_bunker :
            print('Na nossa busca no banco de dados, nao achamos pessoas suficientes com os parametros de selecao')

        else :
            print('Chegamos a nossa capacidade maxima')
        
        #Output relatorios
        print('\nRelatorio:')
        print(f'Medicos: {medicina}')
        print(f'Engenheiros: {engenharia}')
        print(f'Cientistas: {ciencia}')
        print(f'Professores: {docencia}')

else:
    print('Chegamos a nossa capacidade maxima')

    #Output relatorios
    print('\nRelatorio:')
    print(f'Medicos: {medicina}')
    print(f'Engenheiros: {engenharia}')
    print(f'Cientistas: {ciencia}')
    print(f'Professores: {docencia}')



