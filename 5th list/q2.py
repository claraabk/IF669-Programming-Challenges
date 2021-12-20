#Função p/ alterar os números
def alteracao_numero (digitos) :

    # Transformando o número em string p/ formar uma lista
    digitos = str(digitos)

    #Criando a recursão
    if len(str(digitos)) >= 8 :
        return digitos

    else:
        # Criando a lista
        lista_digitos = list(digitos)

        # Lista vazia p/ o resultado
        lista_resultado = []
        # Lista com os números aparecendo uma vez p/ fazer a contagem
        lista_unica = list(set(lista_digitos))

        #P/ cada número que aparece na lista única, contabilize na lista de dígito
        for i in range(len(lista_unica)):
            #Somando a string p/ formar os pares
            novo_num = str(lista_digitos.count(lista_unica[i])) + lista_unica[i]
            #Apendando na lista do resultado
            lista_resultado.append(novo_num)

        #Ordenando do menor para o maior
        resultado_ordenado = sorted(lista_resultado)
        #Transformando em string novamente
        resultado_ordenado = ''.join(resultado_ordenado)

        return alteracao_numero(resultado_ordenado)

#Input
digitos = int(input())

#Chamando a função
resultado = alteracao_numero(digitos)

#Output
print(resultado)