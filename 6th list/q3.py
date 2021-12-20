#Função : Definir o dano da arma e diminuir da vida
def dano_ferramenta(arma_dano,limite_vida,vida_inimigo,ferramenta):

    #Condicao : Vida do inimigo é maior que 40%
    if vida_inimigo > limite_vida :
        vida_inimigo -= arma_dano[ferramenta]

    #Condicao : Vida do inimigo é menor que 40%
    else:
        #Condicoes : Diminuindo o valor do dano de acordo com a arma
        if 100 <= arma_dano[ferramenta] < 200 :
            vida_inimigo -= 0.5*arma_dano[ferramenta]

        elif 200 <= arma_dano[ferramenta] < 300 :
            vida_inimigo -= 0.25*arma_dano[ferramenta]

        elif arma_dano[ferramenta] >= 300 :
            vida_inimigo -= 0.15*arma_dano[ferramenta]

    return vida_inimigo

#Dicionario arma - valor do dano
arma_dano = {
    'Batrangue':270,
    'Bat-Minas':255,
    'Tasers':185,
    'Soqueiras':150,
    'Granada Sonica': 300,
    'Gel Explosivo':400,
    'Faca Tatica': 345
}

#Input - Qt de batalhas
qt_batalhas = int(input())

#Variáveis iniciais p/ contabilizar mortos fugas e sucessos
mortos = 0
fugas = 0
sucessos = 0

#Loop p/ cada batalha
for i in range(qt_batalhas):
    #Input : Ferramenta e vida inicial
    qt_ferramentas = int(input())
    vida_inicial = int(input())
    #Vida inimigo : P/ alterar na funcao e limite vida : 40% da vida inicial
    vida_inimigo, limite_vida = vida_inicial, 0.4 * vida_inicial

    #Loop p/ aplicar a funcao em casa ferramenta
    for j in range(qt_ferramentas):
        ferramenta = input()

        # Checando se a ferramente pertence ao dicionário
        ferramenta_in_dict = arma_dano.get(ferramenta)

        # Ferramenta_in_dict = True
        if ferramenta_in_dict :
            vida_inimigo = dano_ferramenta(arma_dano,limite_vida,vida_inimigo,ferramenta)

        #Ferramenta nao pertence
        else:
            print(f'{ferramenta}? Infelizmente esta ferramenta não está disponível.')

    #Contabilizando qt total de mortos, fugas e sucessos
    if vida_inimigo > 0.15*vida_inicial :
        fugas += 1

    elif 0.15*vida_inicial >= vida_inimigo  > 0 :
        sucessos += 1

    elif vida_inimigo <= 0 :
        mortos += 1

#Print inicial
print(f'Mortos: {mortos}\n'
      f'Fugas: {fugas}\n'
      f'Incapacitados: {sucessos}')

#Condicoes de fracassos e sucessos
if sucessos > fugas + mortos and fugas + mortos > 0 :
    print('Batman conseguiu capturar a maioria dos criminosos, nosso herói está no caminho certo.')

elif sucessos > fugas + mortos and fugas + mortos == 0 :
    print('Batman conseguiu capturar todos os criminosos e garantiu uma noite segura em Gotham City.')

elif fugas + mortos > sucessos and sucessos > 0 :
    print('Muitas missões fracassadas.. Pelo visto, o nosso herói precisa treinar mais.')

elif fugas + mortos > sucessos and sucessos == 0 :
    print('Muitas missões fracassadas... Tem certeza de que o seu programa passou as ferramentas corretas?')

elif fugas + mortos == sucessos :
    print('Uma noite caótica em Gotham City, talvez o nosso herói precise mudar as ferramentas...')