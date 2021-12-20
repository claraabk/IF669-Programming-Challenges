#Lista inicial do alfabeto
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Funcao p/ encontrar o termo fibonacci
def fibonacci(chave) :
    n1 = 1
    n2 = 1

    for i in range(2,chave) :
        resultado = n1 + n2
        n1 = n2
        n2 = resultado

    return resultado

#Primeiro input e lista vazia p/ o output
qt_frase = int(input())
lista_output = []

#Encontrando o output de cada frase
for i in range(qt_frase) :
    chave = int(input())
    frase = input()

    #Tirando os espaços, deixando em minúscula e criando uma lista
    frase = frase.replace(' ','')
    frase.lower()
    frase = list(frase)

    lista_output = []

    #Encontrando a frase final 
    for i in range(len(frase)) :
        #Posicao inicial no alfabeto
        posicao = alfabeto.index(frase[i])
        
        #Somando a posicao de acordo com a sequencia de fibonacci
        nova_posicao = posicao + fibonacci(chave)
        
        #Caso ultrapasse a lista
        if nova_posicao > 25 :
            nova_posicao = nova_posicao % 26
        
        #Apendando a letra na lista do output
        lista_output.append(alfabeto[nova_posicao])
        
        #Somando o termo em fibonacci
        chave += 1
    
    #Printando a lista
    print(''.join(lista_output))




