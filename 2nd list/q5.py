#Inputs
energia_c1 = int(input())
peso_c1 = int(input())
energia_c2 = int(input())
peso_c2 = int(input())
energia_c3 = int(input())
peso_c3 = int(input())

for i in range(0,3):
  peso1_c1 = int(input())
  peso1_c2 = int(input())
  peso1_c3 = int(input())
  energia_c1 = energia_c1 - float(peso1_c1/peso_c1)
  energia_c2 = energia_c2 - float(peso1_c2/peso_c2)
  energia_c3 = energia_c3 - float(peso1_c3/peso_c3)


if energia_c1 <=0:
    print('O competidor 1, desmaiou')
if energia_c2 <=0:
    print('O competidor 2, desmaiou')
if energia_c3 <=0:
    print('O competidor 3, desmaiou')

if energia_c1 > 0 and ( energia_c1<energia_c2 or energia_c2<=0 ) and ( energia_c1<energia_c3 or energia_c3<=0 ):
  print('O vencedor foi o competidor 1')
elif energia_c2 > 0 and ( energia_c2<energia_c1 or energia_c1<=0) and (energia_c2<energia_c3 or energia_c3<=0 ):
  print('O vencedor foi o competidor 2')
elif energia_c3 > 0 and ( energia_c3<energia_c1 or energia_c1<=0) and ( energia_c3<energia_c2 or energia_c2<=0):
  print('O vencedor foi o competidor 3')
elif energia_c1 <=0 and energia_c2<=0 and energia_c3<=0:
  print('Todos os competidores desmaiaram')
  
