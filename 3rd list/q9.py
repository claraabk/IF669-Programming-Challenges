#Lista: Média - Pró bonos - Maior pontuação
lista_mike = [0,0,0]
lista_harvey = [0,0,0]
lista_louis = [0,0,0]

#Soma inicial mike e total de casos inicial
soma_mike, casos_mike = 0,0
soma_harvey, casos_harvey = 0,0
soma_louis, casos_louis =0,0

#Input
qt_casos = int(input())

#P/ adicionar a lista de cada pessoa 
for i in range(qt_casos) :
    nome, tipo, pontuacao = input().split()

    if nome == 'Mike' :
        soma_mike += int(pontuacao)
        casos_mike += 1
        if tipo =='pro-bono' :
            lista_mike[1] += 1
        if int(pontuacao) > int(lista_mike[2]) :
            lista_mike[2] = int(pontuacao)

    elif nome == 'Harvey' :
        soma_harvey += int(pontuacao)
        casos_harvey += 1
        if tipo == 'pro-bono' :
            lista_harvey[1] += 1
        if int(pontuacao) > int(lista_harvey[2]) :
            lista_harvey[2] = int(pontuacao)

    elif nome == 'Louis' :
        soma_louis += int(pontuacao)
        casos_louis += 1
        if tipo == 'pro-bono' :
            lista_louis[1] += 1
        if int(pontuacao) > int(lista_louis[2]) :
            lista_louis[2] = int(pontuacao)

#Média de cada um 
lista_mike[0] = soma_mike / casos_mike
lista_harvey[0] = soma_harvey / casos_harvey
lista_louis[0] = soma_louis / casos_louis

#Print por participante
print(f'Mike;\nMédia: {lista_mike[0]:.2f}\nQuantidade de Pró-bonos: {lista_mike[1]}\nMáximo: {lista_mike[2]}\n')
print(f'Louis;\nMédia: {lista_louis[0]:.2f}\nQuantidade de Pró-bonos: {lista_louis[1]}\nMáximo: {lista_louis[2]}\n')
print(f'Harvey;\nMédia: {lista_harvey[0]:.2f}\nQuantidade de Pró-bonos: {lista_harvey[1]}\nMáximo: {lista_harvey[2]}\n')

#Definindo o vencedor e o perdedor 
if lista_mike > lista_harvey and lista_mike > lista_louis :
    vencedor = 'Mike'

    if lista_harvey > lista_louis :
        perdedor = 'Louis'

    else:
        perdedor = 'Harvey'

elif lista_louis > lista_mike and lista_louis > lista_harvey :
    vencedor = 'Louis'

    if lista_harvey > lista_mike :
        perdedor = 'Mike'

    else :
        perdedor = 'Harvey'

elif lista_harvey > lista_louis and lista_harvey > lista_mike :
    vencedor = 'Harvey'

    if lista_louis > lista_mike :
        perdedor = 'Mike'

    else :
        perdedor = 'Louis'

elif lista_mike==lista_louis and lista_mike==lista_harvey :
    vencedor = 'Mike'
    perdedor = 'Harvey'

print(f'Quem ganhou a competição e vai ficar com a sala nova foi o {vencedor}!!! E o coitado que vai ter que comprar os móveis vai ser o {perdedor}.')









