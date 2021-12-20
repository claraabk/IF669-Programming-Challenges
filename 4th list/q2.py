#Função p/ calcular o valor da vida
def funcao_vida(mascara) :
    mascara,vida = mascara.split()
    if mascara == 'Aku-Aku' :
        vida = 2*int(vida)
    elif mascara == 'Velo' :
        vida = 1.25*int(vida)
    elif mascara == 'Apo-Apo' :
        vida = 1.5*int(vida)

    return [mascara,vida]

#Função p/ calcular o valor do dano
def funcao_dano(vilao,frutas_totais) :
    vilao, dano  = vilao.split()
    if frutas_totais <= 20 :
        dano = int(dano)**2
    elif frutas_totais > 20 and frutas_totais <= 30 :
        dano = 2*int(dano)

    return [vilao,dano]

#Variáveis iniciais
qt_viloes = int(input())
vitorias = 0
percas = 0

#Condição p/ ver se vai ter vilao
if qt_viloes > 0 :
    #Caso tenha vilao
    for i in range(qt_viloes) :
        mascara = input()
        vilao = input()
        frutas_totais = 0
        
        #Input das frutas
        while True :
            frutas = input()
            frutas_totais += int(frutas)
            if frutas == '0' :
                break

        #Puxando os valores da vida e do dano
        valor_mascara = int(((funcao_vida(mascara))[1]))
        valor_dano = int(((funcao_dano(vilao,frutas_totais))[1]))

        #Testando pra ver se vai ter combate (dependendo das frutas)
        if frutas_totais > 10 :
          
            #Caso crash ganhe
            if valor_mascara > valor_dano :
                vitorias += 1
                print(f'O nosso herói conseguiu mais uma vez! Pisou no {((funcao_dano(vilao,frutas_totais))[0])}.')

            #Caso crash perca
            else :
                percas += 1
                print('Aku-Aku estamos precisando de você!')
        
        #Crash perdendo por conta da qt de frutas
        else :
            print(f'Infelizmente o Crash só conseguiu pegar {frutas_totais} frutas, então, não é hoje que ele vai derrotar o {((funcao_dano(vilao, frutas_totais))[0])} =(')

    #Comparando qt de vitorias e de percas 
    if vitorias > percas :
        print('O Crash conseguiu livrar as Ilhas Wumpa das mãos dos vilões!!!')
    else:
        print('Não é possível, o Crash não conseguiu vencer?')

#Caso não tenha nenhum vilão
else:
    print('Nenhum vilão teve coragem de encarar o Crash hoje!')