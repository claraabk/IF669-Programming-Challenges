#Input e criacao da lista a partir do input
alfabeto = input()
alfabeto = alfabeto.split()

codigo = input()
codigo = codigo.split()

letra_1 = input()

#Definicao da posicao inicial
posicao_inicial = alfabeto.index(letra_1)

#Lista para printar a mensagem final
mensagem = []

#Loop p/ apendar a mensagem
for i in range (len(codigo)) :
    if codigo[i] == '/' :
        mensagem.append(' ')

    elif codigo[i] == 'R' :
        mensagem.append(alfabeto[posicao_inicial])

    else:
        posicao = posicao_inicial + int(codigo[i])

        if posicao > 25 :
            posicao = posicao % 26

        mensagem.append(alfabeto[posicao])
        posicao_inicial = posicao

#Output
print(''.join(mensagem))