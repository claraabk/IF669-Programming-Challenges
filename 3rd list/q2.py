lista = []
count = 0

try:
    while True:
        name = input()
        if ( name not in lista ) and  ( name=='Damon Salvatore' or name=='Stefan Salvatore' or name=='Caroline Forbes' or name=='Elena Gilbert' or name=='Bonnie Bennett' or name=='Kai Parker' or name=='Katherine Pierce'):
            lista.append(name)
            count += 1
except:
    if count == 0:
        print('Nenhum sobrenatural foi encontrado :/')
    else:
        print('Os sobrenaturais encontrados foram:\n')
        for nome in range(len(lista)):
            print(lista[nome])
        print('\nAgora Klaus, Rebekah, Elijah, Kol e toda a família original sabem bem em quem podem confiar e quem devem matar.')
