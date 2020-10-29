#Esse programa serve para formatar uma tabuada



from time import sleep

tabuada = int(input('Digite um número inteiro para mostrar a sua tabuada: '))
for c in range(1, 11):
    sleep(0.5)
    print('{} x {} = {}'.format(tabuada, c, tabuada * c))
