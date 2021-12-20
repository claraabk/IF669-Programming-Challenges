#Inputs
nome = str(input())
qt_treinos = int(input())

a = int(2)
gol_treino1 = int(input())

#Variáveis para menor e maior quantidade de gols
maior_gol = gol_treino1
menor_gol = gol_treino1

if qt_treinos==1:
    print(f'Belo dia de treinos, {nome}! Hoje o seu melhor desempenho foi de {gol_treino1} gols e o pior foi de {gol_treino1} gols. Rumo ao Ouro!')
else:
    while ( qt_treinos >= a ):
        gol = int(input())
        a = a + 1
        if ( gol >= maior_gol ):
            maior_gol = gol
        elif ( gol <= menor_gol ):
            menor_gol = gol

    print(f'Belo dia de treinos, {nome}! Hoje o seu melhor desempenho foi de {maior_gol} gols e o pior foi de {menor_gol} gols. Rumo ao Ouro!')


