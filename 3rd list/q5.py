#Primeira entrada

lista=[]
lista_assasinatos = []
lista_furtos = []

crime = input().split(': ')

if crime[1] != 'Doug Judy':
      lista.append(crime[0])
      lista.append(crime[1])

#Próximas entradas
while crime[1] != 'Doug Judy' :
    crime = input().split(': ')
    if crime[1] != 'Doug Judy':
      lista.append(crime[0])
      lista.append(crime[1])


#Operações
n_operacoes = int(input())

for i in range(n_operacoes):
    tipo_operacao = int(input())

    if tipo_operacao == 1 :
        name = input()
        print(f'Na ficha de {name} constam {lista.count(name)} infrações este mês.')

    elif tipo_operacao == 2 :
        crime = input()
        print(f'Neste mês foram cometidos {lista.count(crime)} {crime}')

    elif tipo_operacao == 3 :
        for number in range(int(len(lista) - 1 )):

            if lista[number] == 'Assassinato' :

                if lista[int(number+1)] not in lista_assasinatos:
                    lista_assasinatos.append(lista[int(number+1)])

            elif lista[number] == 'Furto' or lista[number] == 'Roubo':

                if lista[int(number+1)] not in lista_furtos :
                    lista_furtos.append(lista[int(number+1)])

        print('Boletim de Ocorrências:')
        print('Assassinos: '+', '.join(lista_assasinatos))
        print('Ladroes: '+', '.join(lista_furtos))