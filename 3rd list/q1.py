lista = []

for numero in range(0,5) :
    competidor = input()
    competidor = competidor.split(' - ')
    lista = lista + competidor

print('Velocista - Posicao\n')

first = lista.index('1')
print(lista[int(first-1)] + ' - ' + lista[first])

second = lista.index('2')
print(lista[int(second-1)] + ' - ' + lista[second])

third = lista.index('3')
print(lista[int(third-1)] + ' - ' + lista[third])

fourth = lista.index('4')
print(lista[int(fourth-1)] + ' - ' + lista[fourth])

fifth = lista.index('5')
print(lista[int(fifth-1)] + ' - ' + lista[fifth])

