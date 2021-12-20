voltas = int(input())

tempo_maximo = voltas*72

tempo = 0

mensagem_erro = 0
mensagem_acerto =0
erro_consecutivo = 0

n_mensagens = 0


while n_mensagens < 10*voltas and tempo <= tempo_maximo and erro_consecutivo < 5 :
  nova_mensagem = input()
  if nova_mensagem == 'erro':
    n_mensagens += 1
    mensagem_erro += 1
    tempo += 9
    erro_consecutivo += 1
  elif nova_mensagem == 'acerto' :
    n_mensagens += 1
    tempo += 5
    mensagem_acerto += 1
    erro_consecutivo = 0
      
  if erro_consecutivo != 0 and erro_consecutivo % 2 == 0 :
    print('Voce precisa melhorar, Carlinhos')

  

if erro_consecutivo >= 5 :
  print('O treino de hoje nao esta rendendo Carlinhos, vamos tentar de novo amanha')

if tempo > tempo_maximo and n_mensagens < 10*voltas :
  print('Temos que trabalhar urgentemente na sua velocidade, voce precisa errar menos')
  print('Seu desempenho esta bom, mas poderia ter sido muito melhor')

if mensagem_acerto == 10*voltas and tempo < tempo_maximo :
  print('Que desempenho excelente, Carlinhos, melhor impossivel')

if mensagem_erro > 0 and tempo < tempo_maximo :
  print('Seu desempenho esta bom, mas poderia ter sido muito melhor')
