#Função p/ checar se é anagrama
def check_anagrama (chave, senha) :
  
    #Dicionário vazio
    dict_chave = {}
    #P/ cada letra da chave 
    for letra in range(len(chave)) :
        #Caso a letra ainda não esteja no dicionário, adicionar ela com o valor do count
        if chave[letra] not in dict_chave :
            dict_chave[chave[letra]] = chave.count(chave[letra])

    #Fazendo a mesma coisa da chave p/ a senha
    dict_senha = {}
    for letra in range(len(senha)) :
        if senha[letra] not in dict_senha :
            dict_senha[senha[letra]] = senha.count(senha[letra])

    #Condição: Se os dois dicionários forem iguais, retorne True
    if dict_chave == dict_senha :
        liberado = True
    #Else: False    
    else:
        liberado = False

    return liberado

#Input chave e senha
chave = input()
senha = input()

#Deixando todos em minúsculo
chave, senha = chave.lower(),senha.lower()

#Chamando a função
res = check_anagrama (chave, senha)

#Output dependendo do resultado
if res :
    print('Acesso liberado. Bem vindo Senhor Stark.')
else :
    print('Acesso negado.')