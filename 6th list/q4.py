#Listas e dicionários vazios p/ apendar
lista_atividades = []
nome_atividade = {}
lista_nomes = []

#Try except p/ qt indefinida de input
try:

    while True:
        #Input nome - atividade
        nome = input()
        #Separando o input apenas no 1 espaço
        nome, atividade = nome.split(' ',1)

        #Criando uma lista com o total de atividades sem se repetir
        if atividade not in lista_atividades :
            lista_atividades.append(atividade)

        #Criando uma lista com os nomes sem se repetir
        if nome not in lista_nomes :
            lista_nomes.append(nome)

        #Condição: O nome está aparecendo pela 1 vez - adicionando ao dicionário
        if nome not in nome_atividade :
            nome_atividade[nome] = [atividade]
        #Apendando a atividade ao nome dentro do dicionário
        else:
            nome_atividade[nome].append(atividade)

except:

    #Para cada nome da lista - > Printar o nome 
    for nome in lista_nomes :
        print(f'{nome}:')
        
        # P cada atividade da lista, se não estiver na lista desse nome ->  print
        for atividade in lista_atividades :

            if atividade not in nome_atividade[nome] :
                print(f'- {atividade}')






