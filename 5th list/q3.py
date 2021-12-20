#Função p/ ordenar a lista
def ordenacao_batalhoes (lista_batalhoes) :

    #Algoritmo p/ ordenar a lista
    for i in range(len(lista_batalhoes)-1):

        for j in range(len(lista_batalhoes)-1):

            if int(lista_batalhoes[j]) > int(lista_batalhoes[j + 1]):
                lista_batalhoes[j], lista_batalhoes[j + 1] = lista_batalhoes[j + 1], lista_batalhoes[j]

    return lista_batalhoes

#Função p/ realizar busca binária
def busca_binaria (lista_ordenada,procurado) :
    #Caso base: O número não está na lista
    if procurado not in lista_ordenada :
        return -1

    #Encontrando a metade da lista
    metade = int(len(lista_ordenada)-1/2)

    #Caso base : O número procurado foi encontrado no meio da lista
    if lista_ordenada[metade] == procurado :
        return metade

    #O número procurado é maior que o elemento do meio
    elif procurado > lista_ordenada[metade] :
        return busca_binaria(lista_ordenada[metade:],procurado)

    #O número procurado é menor que o elemento do meio
    elif procurado < lista_ordenada[metade] :
        return busca_binaria(lista_ordenada[:metade],procurado)

#Input : Qt de batalhões
batalhoes = int(input())
#Lista inicial batalhões p/ apendar
lista_batalhoes = []

#Input do tamanho de cada batalhão
for i in range(batalhoes) :
    tamanho = int(input())

    #Condição : Apendar só se for positivo
    if tamanho >= 0 :
        lista_batalhoes.append(tamanho)

#Chamando a função de ordenação da lista
lista_ordenada = ordenacao_batalhoes(lista_batalhoes)

#Input da qt de buscas
buscas = int(input())

#Input do número a se procurar
for i in range(buscas) :
    procurado = int(input())

    #Condição : O número não foi encontrado
    if busca_binaria(lista_ordenada,procurado) == -1 :
        print('Busca falhou: -1')

    #Condição : O número foi encontrado
    else :
        print(f'Busca com sucesso: {busca_binaria(lista_ordenada,procurado)}')



