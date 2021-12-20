#Input
nome_primeira = str(input())
visualizacoes_primeira = int(input())
nome_segunda =  str(input())
visualizacoes_segunda = int(input())
nome_terceira = str(input())
visualizacoes_terceira = int(input())

#Primeira música maior
if (visualizacoes_primeira>visualizacoes_segunda) and (visualizacoes_primeira>visualizacoes_terceira):
    if (visualizacoes_segunda>visualizacoes_terceira):
        print(f'{nome_primeira} {visualizacoes_primeira}\n{nome_segunda} {visualizacoes_segunda}\n{nome_terceira} {visualizacoes_terceira}')
    elif (visualizacoes_segunda<visualizacoes_terceira):
        print(f'{nome_primeira} {visualizacoes_primeira}\n{nome_terceira} {visualizacoes_terceira}\n{nome_segunda} {visualizacoes_segunda}')
    elif (visualizacoes_segunda==visualizacoes_terceira):
        print(f'{nome_primeira} {visualizacoes_primeira}\n{nome_segunda} {visualizacoes_segunda}\n{nome_terceira} {visualizacoes_terceira}')
#Segunda música maior
elif (visualizacoes_segunda>visualizacoes_primeira) and (visualizacoes_segunda>visualizacoes_terceira):
    if (visualizacoes_primeira>visualizacoes_terceira):
        print(f'{nome_segunda} {visualizacoes_segunda}\n{nome_primeira} {visualizacoes_primeira}\n{nome_terceira} {visualizacoes_terceira}')
    elif (visualizacoes_terceira>visualizacoes_primeira):
        print(f'{nome_segunda} {visualizacoes_segunda}\n{nome_terceira} {visualizacoes_terceira}\n{nome_primeira} {visualizacoes_primeira}')
    elif (visualizacoes_terceira==visualizacoes_primeira):
        print(f'{nome_segunda} {visualizacoes_segunda}\n{nome_primeira} {visualizacoes_primeira}\n{nome_terceira} {visualizacoes_terceira}')
#Terceira música maior
elif (visualizacoes_terceira>visualizacoes_primeira) and (visualizacoes_terceira>visualizacoes_segunda):
    if (visualizacoes_primeira>visualizacoes_segunda):
        print(f'{nome_terceira} {visualizacoes_terceira}\n{nome_primeira} {visualizacoes_primeira}\n{nome_segunda} {visualizacoes_segunda}')
    elif (visualizacoes_segunda>visualizacoes_primeira):
        print(f'{nome_terceira} {visualizacoes_terceira}\n{nome_segunda} {visualizacoes_segunda}\n{nome_primeira} {visualizacoes_primeira}')
    elif (visualizacoes_primeira==visualizacoes_segunda):
        print(f'{nome_terceira} {visualizacoes_terceira}\n{nome_primeira} {visualizacoes_primeira}\n{nome_segunda} {visualizacoes_segunda}')
#2 ou mais visualizacoes iguais
elif (visualizacoes_primeira==visualizacoes_segunda) and (visualizacoes_primeira>visualizacoes_terceira):
    print(f'{nome_primeira} {visualizacoes_primeira}\n{nome_segunda} {visualizacoes_segunda}\n{nome_terceira} {visualizacoes_terceira}')
elif (visualizacoes_primeira==visualizacoes_terceira) and (visualizacoes_primeira>visualizacoes_segunda):
    print(f'{nome_primeira} {visualizacoes_primeira}\n{nome_terceira} {visualizacoes_terceira}\n{nome_segunda} {visualizacoes_segunda}')
elif (visualizacoes_segunda==visualizacoes_terceira) and (visualizacoes_segunda>visualizacoes_primeira):
    print(f'{nome_segunda} {visualizacoes_segunda}\n {nome_terceira} {visualizacoes_terceira}\n{nome_primeira} {visualizacoes_primeira}')
elif (visualizacoes_primeira==visualizacoes_segunda==visualizacoes_terceira):
    print(f'{nome_primeira} {visualizacoes_primeira}\n{nome_segunda} {visualizacoes_segunda}\n{nome_terceira} {visualizacoes_terceira}')



