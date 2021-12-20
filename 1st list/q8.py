#Input
musica1 = str(input())
musica2 = str(input())
musica3 = str(input())
musica4 = str(input())
musica5 = str(input())
musica6 = str(input())

#Qt de musicas e duracoes
duracoes_jg = 0
musicas_jg = 0

duracoes_zv = 0
musicas_zv = 0

#Separacao da string
musica_1 = musica1.split(' - ')
musica_2 = musica2.split(' - ')
musica_3 = musica3.split(' - ')
musica_4 = musica4.split(' - ')
musica_5 = musica5.split(' - ')
musica_6 = musica6.split(' - ')

#Manipulacao da duracao p/ float
duracao_1 = float(musica_1[2])
duracao_2 = float(musica_2[2])
duracao_3 = float(musica_3[2])
duracao_4 = float(musica_4[2])
duracao_5 = float(musica_5[2])
duracao_6 = float(musica_6[2])

#Condicoes
if ( musica_1[1] == 'Joao gomes' ):
    musicas_jg +=1
    duracoes_jg = duracoes_jg + duracao_1
elif ( musica_1[1] == 'Ze vaqueiro'):
    musicas_zv +=1
    duracoes_zv = duracoes_zv + duracao_1

if ( musica_2[1] == 'Joao gomes' ):
    musicas_jg +=1
    duracoes_jg = duracoes_jg + duracao_2
elif ( musica_2[1] == 'Ze vaqueiro'):
    musicas_zv +=1
    duracoes_zv = duracoes_zv + duracao_2

if ( musica_3[1] == 'Joao gomes' ):
    musicas_jg +=1
    duracoes_jg = duracoes_jg + duracao_3
elif ( musica_3[1] == 'Ze vaqueiro'):
    musicas_zv +=1
    duracoes_zv = duracoes_zv + duracao_3

if ( musica_4[1] == 'Joao gomes' ):
    musicas_jg +=1
    duracoes_jg = duracoes_jg + duracao_4
elif ( musica_4[1] == 'Ze vaqueiro'):
    musicas_zv +=1
    duracoes_zv = duracoes_zv + duracao_4

if ( musica_5[1] == 'Joao gomes' ):
    musicas_jg +=1
    duracoes_jg = duracoes_jg + duracao_5
elif ( musica_5[1] == 'Ze vaqueiro'):
    musicas_zv +=1
    duracoes_zv = duracoes_zv + duracao_5

if ( musica_6[1] == 'Joao gomes' ):
    musicas_jg +=1
    duracoes_jg = duracoes_jg + duracao_6
elif ( musica_6[1] == 'Ze vaqueiro'):
    musicas_zv +=1
    duracoes_zv = duracoes_zv + duracao_6

#Saida 1
if ( musica_1[1] == musica_2[1] == musica_3[1] == musica_4[1] == musica_5[1] == musica_6[1]):
    print('Nao tivemos dados suficientes para chegar uma conclusao.')

#Comparacao das medias
if musicas_zv>0:
    resultado_zv = duracoes_zv/musicas_zv
else:
    resultado_zv=0

if musicas_jg>0:
    resultado_jg = duracoes_jg/musicas_jg
else:
    resultado_jg=0

#Saidas
if resultado_zv!=0 and resultado_jg!=0:
    if resultado_zv==resultado_jg:
        print('Tivemos um empate tecnico.')
    elif resultado_jg>resultado_zv:
        print('De acordo com estes dados temos um forte indicativo de que as musicas de Joao gomes sao mais longas que as de Ze vaqueiro.')
    elif resultado_zv>resultado_jg:
        print('De acordo com estes dados temos um forte indicativo de que as musicas de Ze vaqueiro sao mais longas que as de Joao gomes.')
elif resultado_jg==0 and resultado_zv==0:
    print('Nao tivemos dados suficientes para chegar uma conclusao.')