#Definindo a funcao de validacao 
def validacao(id):
    id = list(id)
    soma_total = 0
    
    #Alterando os numeros de acordo com os criterios
    for i in range (len(id)) :
        if i % 2 != 0 :
            id[(len(id)-1)-i] = int(id[(len(id)-1)-i])*2
            
            #Fazendo alteracao caso tenha mais de 2 digitos
            if int(id[(len(id)-1)-i]) >= 10 :
                termo = str(id[(len(id)-1)-i])
                lista = list(termo)

                j= 0
                soma = int(lista[j]) + int(lista[j+1])
                id[(len(id) - 1) - i] = soma
    
    #Somando pra encontrar o resultadp final
    for w in range(len(id)) :
        soma_total += int(id[w])


    return soma_total


#Input
id = input()
id = id.replace('id', '')

resultado = int(validacao(id))

#Printando valido ou xitado
if resultado % 10 == 0 :
    print(f'Analisando ID: {id}')
    print('Situacao: Jogador limpo')
else:
    print(f'Analisando ID: {id}')
    print('Situacao: XITADO ATE OS DENTES')


