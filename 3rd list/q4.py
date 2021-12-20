#Input c/ testemunhas
names = input()

#Formando a lista das testemunhas
list_names = names.split(' ')

qt = int(input())

#Realização das trocas

for number in range(qt):
    troca = int(input())

    if list_names[troca] != list_names[int(((len(list_names))-1)-troca )] :
      print(f'A testemunha {list_names[troca]} trocou de ordem com a testemunha {list_names[int(((len(list_names))-1)-troca )]}')
      list_names[troca], list_names[int(((len(list_names))-1)-troca )] = list_names[int(((len(list_names))-1)-troca )], list_names[troca] 
            
    elif list_names[troca] == list_names[int(((len(list_names))-1)-troca )] or troca == int(((len(list_names))-1)-troca ) :
      print('Nenhuma troca foi feita')

print(*list_names)
