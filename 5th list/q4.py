#Alfabeto minúsculo e maiúsculo p/ fazer alteração caso tenha letra maiúscula
alfabeto_maisuculo = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabeto_minusculo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Função recursiva p/ inverter a palavra
def inversao_palavra(lista_string) :

    #Transformando a lista em string
    string = ''.join(lista_string)

    #Caso base: Retornar a string só se for vazia
    if string == '' :
        return string

    #Retirando o 1 elemento da string e concatenando no final da string
    else :
        return inversao_palavra(string[1:]) + string[0]

#Input : Palavra a ser invertida
string = input()

#Formando uma lista a partir da palavra
lista_string = list(string)

#Substituindo as letras maiúsculas pelas minúsculas
for i in range(len(lista_string)) :

    #Condição : Caso a letra faça parte da lista alfabeto_maiusculo
    if lista_string[i] in alfabeto_maisuculo :

        #Encontrando o index da letra no alfabeto
        substituicao = alfabeto_maisuculo.index(lista_string[i])
        #Substituindo pela letra de mesmo index do alfabeto minúsculo
        lista_string[i] = alfabeto_minusculo[substituicao]

#Printando a palavra invertida
print(inversao_palavra(lista_string))

#Condição : Se for uma destas palavras, printar mistério desvendado
if inversao_palavra(lista_string) == 'amigo' or inversao_palavra(lista_string) == 'ogima' or inversao_palavra(lista_string) == 'mellon' or inversao_palavra(lista_string) == 'nollem' :
    print('Desvendamos o misterio e a porta se abriu!')

#Printar que mistério não foi desvendado
else:
    print('Acho que ainda nao acertamos, Gandalf, o que faremos agora?')

