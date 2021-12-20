#Input número de baterias
qt_baterias = int(input())

#Soma dos tempos
tempo1 = 0
tempo2 = 0
tempo3 = 0
tempo4 = 0
tempo5 = 0

#Novos inputs dependendo da qt de bateria
for i in range(0,qt_baterias):
    atleta1 = float(input())
    atleta2 = float(input())
    atleta3 = float(input())
    atleta4 = float(input())
    atleta5 = float(input())
    if atleta1 <9.58:
        print(f'O atleta 1 bateu o recorde mundial com o tempo: {atleta1}')
    if atleta2<9.58:
        print(f'O atleta 2 bateu o recorde mundial com o tempo: {atleta2}')
    if atleta3<9.58:
        print(f'O atleta 3 bateu o recorde mundial com o tempo: {atleta3}')
    if atleta4<9.58:
        print(f'O atleta 4 bateu o recorde mundial com o tempo: {atleta4}')
    if atleta5<9.58:
        print(f'O atleta 5 bateu o recorde mundial com o tempo: {atleta5}')
 
    tempo1 += atleta1
    tempo2 += atleta2
    tempo3 += atleta3
    tempo4 += atleta4
    tempo5 += atleta5

if tempo1<tempo2 and tempo1<tempo3 and tempo1<tempo4 and tempo1<tempo5:
    print('Vencedor com o menor tempo somando todas as baterias foi: Atleta 1')
elif tempo2<tempo1 and tempo2<tempo3 and tempo2<tempo4 and tempo2<tempo5:
    print('Vencedor com o menor tempo somando todas as baterias foi: Atleta 2')
elif tempo3<tempo1 and tempo3<tempo2 and tempo3<tempo4 and tempo3<tempo5:
    print('Vencedor com o menor tempo somando todas as baterias foi: Atleta 3')
elif tempo4<tempo1 and tempo4<tempo2 and tempo4<tempo3 and tempo4<tempo5:
    print('Vencedor com o menor tempo somando todas as baterias foi: Atleta 4')
elif tempo5<tempo1 and tempo5<tempo2 and tempo5<tempo3 and tempo5<tempo4:
    print('Vencedor com o menor tempo somando todas as baterias foi: Atleta 5')

