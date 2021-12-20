genero = str(input())
nacionalidade = str(input())
decada = str(input())

if (genero=='Rock'):
  if (nacionalidade=='Nao') and (decada=='70'):
    print('A musica que voce esta procurando eh: Bohemian Rapsody')
  elif (nacionalidade=='Sim') and (decada=='80'):
    print('A musica que voce esta procurando eh: Indios')
  elif (nacionalidade=='Sim') and (decada=='70'):
    print('A musica que voce esta procurando eh: O Pirata')
  else: 
    print('Musica nao encontrada')
elif (genero=='Samba'):
  if (nacionalidade=='Sim') and (decada=='80'):
    print('A musica que voce esta procurando eh: Conselho')
  elif (nacionalidade=='Sim') and (decada=='70'):
    print('A musica que voce esta procurando eh: Apesar de Voce')
  elif (nacionalidade=='Sim') and (decada=='60'):
    print('A musica que voce esta procurando eh: Mas que Nada')
  else:
    print('Musica nao encontrada')
elif (genero=='Pop'):
  if (nacionalidade=='Nao') and (decada=='90'):
    print('A musica que voce esta procurando eh: Candle in the Wind 1997')
  elif (nacionalidade=='Nao') and (decada=='80'):
    print('A musica que voce esta procurando eh: Take On Me')
  elif (nacionalidade=='Sim') and (decada=='90'):
    print('A musica que voce esta procurando eh: Anna Julia')
  else:
    print('Musica nao encontrada')
else:
  print('Musica nao encontrada')
  
