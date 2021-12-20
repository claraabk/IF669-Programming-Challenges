#Inputs
voltas = int(input())

nota_1 = int(input())
nota_2 = int(input())
nota_3 = int(input())
nota_4 = int(input())
nota_5 = int(input())

#Pontuação volta 1
melhor_nota = nota_1 + nota_2 + nota_3 + nota_4 + nota_5

#Variável p/ contar o número de voltas 
a = 1

#1 saída
print(f'A pontuacao na volta 1 foi de {melhor_nota} pontos!')

for i in range(0,(voltas-1)):
  nota1 = int(input())
  nota2 = int(input())
  nota3 = int(input())
  nota4 = int(input())
  nota5 = int(input())
  a +=1
  print(f'A pontuacao na volta {a} foi de {nota1 + nota2 + nota3 + nota4 + nota5} pontos!')

  if ( nota1 + nota2 + nota3 + nota_4 + nota5 ) >= melhor_nota:
    melhor_nota = nota1 + nota2 + nota3 + nota4 + nota5

print(f'A pontuacao final de Rayssa foi de {melhor_nota} pontos!')