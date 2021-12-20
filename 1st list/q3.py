objeto_1 = str(input())
objeto_2 = str(input())
objeto_3 = str(input())
objeto_4 = str(input())

a=0

if (objeto_1=='Alicate'):
   a+=1
elif (objeto_1=='Chave de Fenda'):
    a+=1
elif (objeto_1=='Lanterna'):
    a+=1
elif (objeto_1=='Martelo'):
    a+=1

if (objeto_2=='Alicate'):
    a+=1
elif (objeto_2=='Chave de Fenda'):
    a+=1
elif (objeto_2=='Lanterna'):
    a+=1
elif (objeto_2=='Martelo'):
    a+=1

if (objeto_3=='Alicate'):
    a+=1
elif (objeto_3=='Chave de Fenda'):
    a+=1
elif (objeto_3=='Lanterna'):
    a+=1
elif (objeto_3=='Martelo'):
    a+=1

if (objeto_4=='Alicate'):
    a+=1
elif(objeto_4=='Chave de Fenda'):
    a+=1
elif (objeto_4=='Lanterna'):
    a+=1
elif (objeto_4=='Martelo'):
    a+=1

if (a==4):
    print('Tuê, encontrei tudo! Tá tudo Jóia, ficou bem BOOMZIM!!!')
elif (a==0):
    print('Tuêzin! Se a seca chegar, não vai se desanimar...')
else:
    print('Andam dizendo que o Tuê é um baiano...')
