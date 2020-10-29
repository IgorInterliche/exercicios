n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é o maior')
    print('O segundo número é o menor')
elif n2 > n1:
    print('O segundo número é o maior')
    print('O primeiro número é o menor')
else:
    print('Os dois números são iguais, portanto, não existe valor maior ou menor')

