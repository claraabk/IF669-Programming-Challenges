#Variáveis iniciais
new_value = 'a'
lista = []

#Continuação dos Inputs
while new_value != 'fim' :
    new_value = input()
    lista.append(new_value)

#P/ deixar a lista em ordem crescente 
for i in range(int(len(lista) -2)):
    
    for j in range(int(len(lista) -2)):
        
        if int(lista[j]) > int(lista[j+1]):
            lista[j], lista[j+1] = lista[j+1], lista[j]
            
        
#Saída
for _ in range (int(len(lista) -1)) :
    print(lista[_])