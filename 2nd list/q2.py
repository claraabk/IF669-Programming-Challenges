#Inputs
surfista1 = str(input())
surfista2 = str(input())
surfista3 = str(input())

nacionalidade1 = str(input())
nacionalidade2 = str(input())
nacionalidade3 = str(input())

qt_fases = int(input())

#Variáveis p/ contabilizar as pontuacoes
pontuacao1=0
pontuacao2=0
pontuacao3=0

#Variável p quebrar o while
a = 1

while ( a <= qt_fases ):
    pont1 = float(input())
    pont2 = float(input())
    pont3 = float(input())
    pontuacao1 += pont1
    pontuacao2 += pont2
    pontuacao3 += pont3
    a +=1

#Comparacoes das pontuacoes
if ( pontuacao1 > pontuacao2) and ( pontuacao1 > pontuacao3):
    if nacionalidade1=='Brasil':
        print(f'O vencedor da medalha de ouro de surf e {surfista1}! E do Brasil!')
    else:
        print(f'O vencedor da medalha de ouro de surf e {surfista1}!')
elif ( pontuacao2 > pontuacao1 ) and ( pontuacao2 > pontuacao3):
    if nacionalidade2=='Brasil':
        print(f'O vencedor da medalha de ouro de surf e {surfista2}! E do Brasil!')
    else:
        print(f'O vencedor da medalha de ouro de surf e {surfista2}!')
elif ( pontuacao3 > pontuacao1 ) and ( pontuacao3 > pontuacao2 ):
    if nacionalidade3=='Brasil' :
        print(f'O vencedor da medalha de ouro de surf e {surfista3}! E do Brasil!')
    else:
        print(f'O vencedor da medalha de ouro de surf e {surfista3}!')
elif ( pontuacao1==pontuacao2 ) and ( pontuacao1 > pontuacao3 ):
    if nacionalidade1 == 'Brasil':
        print(f'O vencedor da medalha de ouro de surf e {surfista1}! E do Brasil!')
    else:
        print(f'O vencedor da medalha de ouro de surf e {surfista1}!')
elif ( pontuacao1 == pontuacao3 ) and ( pontuacao1 > pontuacao2 ):
    if nacionalidade1 == 'Brasil':
        print(f'O vencedor da medalha de ouro de surf e {surfista1}! E do Brasil!')
    else:
        print(f'O vencedor da medalha de ouro de surf e {surfista1}!')
elif ( pontuacao2==pontuacao3) and ( pontuacao2 > pontuacao1 ):
    if nacionalidade2=='Brasil':
        print(f'O vencedor da medalha de ouro de surf e {surfista2}! E do Brasil!')
    else:
        print(f'O vencedor da medalha de ouro de surf e {surfista2}!')
elif ( pontuacao1==pontuacao2) and (pontuacao2==pontuacao3):
  if nacionalidade1=='Brasil':
    print(f'O vencedor da medalha de ouro de surf e {surfista1}! E do Brasil!')
  else:
    print(f'O vencedor da medalha de ouro de surf e {surfista1}!')
    
    