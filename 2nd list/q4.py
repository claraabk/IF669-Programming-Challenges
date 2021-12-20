vida_eu = 100
vida_lp = 100
a = 1

while vida_eu > 0 and vida_lp > 0 :
    if (a%2) != 0 :
        a += 1
        ataque = int(input())
        defesa = int(input())
        if ataque > defesa:
            diferenca = ( ataque - defesa )
            if diferenca <= 20:
                vida_eu = vida_eu - diferenca
            elif diferenca > 20:
                vida_eu = vida_eu - 1.5*(diferenca)
        elif ataque <= defesa:
            diferenca2 = ( defesa - ataque )
            if diferenca2 > 20:
                vida_lp = vida_lp - diferenca2
    elif (a%2) == 0:
        a += 1
        ataque2 = int(input())
        defesa2 = int(input())
        if ataque2 > defesa2:
            diferenca = ( ataque2 - defesa2 )
            if diferenca <= 20:
                vida_lp = vida_lp - diferenca
            elif diferenca > 20:
                vida_lp = vida_lp - 1.5*(diferenca)
        elif ataque2 <= defesa2:
            diferenca2 = ( defesa2 - ataque2 )
            if diferenca2 > 20:
                vida_eu = vida_eu - diferenca2
else:
    if vida_lp <= 0:
        print('Apos longos anos de esforco voce finalmente conseguiu, e ouro pro Brasil!')
    elif vida_eu <=0:
        print('Infelizmente nao foi dessa vez, Logan Paul leva a vitoria.')
