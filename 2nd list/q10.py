musica = str(input())
seguidores_michael = int(input())
seguidores_raffa = int(input())
frase_1 = str(input())
frase_2 = str(input())
frase_3 = str(input())

seguidores_esperados = seguidores_michael+seguidores_raffa

print(f'Então Michael, eu trouxe os seguintes resultados da música...\nNome da Música: {musica.upper()}\nNúmero de Seguidores Esperados: {seguidores_esperados}')

if frase_1=='Gang Gang Bro!':
    seguidores_raffa = (1.25*seguidores_raffa)
elif frase_1=='Hihiiiii UuHuu, 777 Bro!':
    seguidores_michael= (1.15*seguidores_michael)
    seguidores_raffa= (1.2*seguidores_raffa)
elif frase_1=='Ayouwoki, ayouwoki, ayouwoki':
    seguidores_michael= (0.7*seguidores_michael)
    seguidores_raffa= (0.75*seguidores_raffa)

if frase_2=='Gang Gang Bro!':
    seguidores_raffa = (1.25*seguidores_raffa)
elif frase_2=='Hihiiiii UuHuu, 777 Bro!':
    seguidores_michael= (1.15*seguidores_michael)
    seguidores_raffa= (1.2*seguidores_raffa)
elif frase_2=='Ayouwoki, ayouwoki, ayouwoki':
    seguidores_michael= (0.7*seguidores_michael)
    seguidores_raffa= (0.75*seguidores_raffa)

if frase_3=='Gang Gang Bro!':
    seguidores_raffa = (1.25*seguidores_raffa)
elif frase_3=='Hihiiiii UuHuu, 777 Bro!':
    seguidores_michael= (1.15*seguidores_michael)
    seguidores_raffa= (1.2*seguidores_raffa)
elif frase_3=='Ayouwoki, ayouwoki, ayouwoki':
    seguidores_michael= (0.7*seguidores_michael)
    seguidores_raffa= (0.75*seguidores_raffa)


seguidores_atuais = int(seguidores_michael+seguidores_raffa)
porcentagem = float((100*seguidores_atuais)/seguidores_esperados)

print(f'Número de Seguidores Calculados: {seguidores_atuais}\nResultado: {porcentagem:.2f}%\n')

if porcentagem>=100:
    print('E felizmente... BROOO! faz sol! Camisa do Rusbé vai vender!')
elif porcentagem<100:
    print('Rockstar e fé em Deus bro! Que vocês irão pensar em frases melhores...')