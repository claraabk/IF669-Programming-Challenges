#Função p/ adicionar ao output a nova string
def funcao_principal(n) :

    #Output em branco
    output = ''

    #Casos bases 1 e 0
    if n == 0 :
        output += 'Precious'
        
    elif n == 1 :
        output += 'My'
        
    #Adicionando ao output a partir de recursão    
    else :
        output += ( funcao_principal(n-1) + funcao_principal(n-2) )

    #Retornando o output completo
    return output

#input
n = int(input())

#output
print(funcao_principal(n))







