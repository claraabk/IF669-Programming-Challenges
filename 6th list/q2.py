#Funcao : Pesquisa de vilao
def pesquisa_vilao(vilao_procurado,dic_pronto) :

    output = ''

    #Variável p/ checar se o vilao existe
    a = dic_pronto.get(vilao_procurado)

    # a = True
    if a:
        #Printando cada atributo do vilao
        output += f'Os atributos do {vilao_procurado} foram:\n'
        output += f'ataque: {dic_pronto[vilao_procurado][ataque]}\n'
        output += f'defesa: {dic_pronto[vilao_procurado][defesa]}\n'
        output += f'vida: {dic_pronto[vilao_procurado][vida]}'

    # a = False / vilao nao existe
    else:
        output += 'Peter, foca nos viloes que tao ai agora! se liga, boy'

    return output

#Função : Pesquisar atributo
def pesquisa_atributo(vilao_procurado,atributo,dic_pronto) :

    output = ''

    #Variável p/ checar se o vilao existe
    a = dic_pronto.get(vilao_procurado)

    # a = True
    if a:
        # Condicao : o atributo nao existe
        if atributo != 'ataque' and atributo != 'defesa' and atributo != 'vida':
            output += 'Ta viajando, peter? nao existe esse atributo'

        # O atributo existe 
        else:
            output += f'O(a) {atributo} do {vilao_procurado} e: {dic_pronto[vilao_procurado][atributo]}\n'

            # Atributo = vida
            if atributo == 'vida':
                #Condicao : valor vida <= 5 ou >= 15
                if int(dic_pronto[vilao_procurado][vida]) <= 5:
                    output += f'{vilao_procurado} esta enfraquecido! va para cima dele, peter!!'
                    
                elif int(dic_pronto[vilao_procurado][vida]) >= 15:
                    output += f'Nao foque em {vilao_procurado} ainda! ele esta muito bem'

            #Atributo = defesa
            elif atributo == 'defesa':
                #Condicao : valor defesa <= 5 ou >= 15
                if int(dic_pronto[vilao_procurado][defesa]) >= 15:
                    output += f'cara, voce nao vai conseguir machuca-lo, {vilao_procurado} e uma muralha!'

                elif int(dic_pronto[vilao_procurado][defesa]) <= 5:
                    output += f'Va agora! {vilao_procurado} nao se defende bem'

            #Atributo = ataque
            elif atributo == 'ataque':
              #Condicao : valor ataque >= 15
                if int(dic_pronto[vilao_procurado][ataque]) >= 15:
                    output += f'{vilao_procurado} vai destruir a cidade, chama o Dr. estranho!'

    # O vilao nao exsite
    else :
        output += 'Peter, foca nos viloes que tao ai agora! se liga, boy'

    return output

#Funcao : Comparar atributo
def comparar_atributo(vilao1,vilao2,atributo,dic_pronto):

    output = ''

    #Comparacao inicial 
    output += 'Aqui esta a comparacao, peter!\n'
    output += f'{vilao1}: {dic_pronto[vilao1][atributo]} X {vilao2}: {dic_pronto[vilao2][atributo]}\n'

    #Comparando o maior e menor
    if dic_pronto[vilao1][atributo] > dic_pronto[vilao2][atributo]:
        output += f'O vilao com menos {atributo} e o {vilao2}, pra cima dele!'

    else:
        output += f'O vilao com menos {atributo} e o {vilao1}, pra cima dele!'


    return output

#Input : qt de viloes
qt_viloes = int(input())
#Dicionario p/ guardar vilao e seus atributos
dic_pronto = {}

#Input de cada atributo dos viloes
for i in range(qt_viloes):
    vilao = input()
    ataque,defesa,vida = input().split(' - ')

    ataque, valor_ataque = ataque.split(', ')
    defesa, valor_defesa = defesa.split(', ')
    vida, valor_vida = vida.split(', ')

    dic_pronto[vilao] = {
        'ataque': int(valor_ataque),
        'defesa': int(valor_defesa),
        'vida': int(valor_vida)
    }

#Input : qt de acoes
qt_acoes = int(input())

#Chamando cada funcao dependendo da acao
for i in range(qt_acoes) :
    acao = input()

    if acao == 'pesquisar vilao' :
        vilao_procurado = input()

        print(pesquisa_vilao(vilao_procurado,dic_pronto))

    elif acao == 'pesquisar atributo' :
        vilao_procurado = input()
        atributo = input()

        print(pesquisa_atributo(vilao_procurado,atributo,dic_pronto))

    elif acao == 'comparar atributo' :
        vilao1 = input()
        vilao2 = input()
        atributo = input()

        print(comparar_atributo(vilao1,vilao2,atributo,dic_pronto))