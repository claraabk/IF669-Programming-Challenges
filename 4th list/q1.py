#Criando a função
def pont(lista_rodada) :
    lista_rodada = lista_rodada.split()
    pontuacao_rodada = 0

    for i in range(len(lista_rodada)):
        if lista_rodada[i] == 'X' :
            pontuacao_rodada += 5

        if i > 0 and lista_rodada[i] == 'X' and lista_rodada[i-1] == 'X' :
            pontuacao_rodada += 5

        pontuacao_total = 0 + pontuacao_rodada

    return pontuacao_total

#Variáveis iniciais 
break_point = '0 0 0 0 0'
resultado = 0

#Inputs
while True :
    lista_rodada = input()

    if lista_rodada == break_point :
        break

    else :
        if lista_rodada == 'X X X X X' :
            print('Note streak!')
            resultado += 20

        resultado += pont(lista_rodada)


#Output dependendo da pontuacao
if resultado < 15 :
    print('Song failed!')
elif resultado >= 15 and resultado <= 49 :
    print('Nada bom, amigo...')
elif resultado >= 50 and resultado <= 69 :
    print('Wow, rock and roll na veia!')
elif resultado >= 70 and resultado <= 100 :
    print('YOU ROCK!!!')
elif resultado > 100 :
    print('TEMOS UMA NOVA LENDA DO ROCK!')


#Output final
print(f'Sua pontuação foi de {resultado} pontos')