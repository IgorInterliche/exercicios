#exemplo de uso do comando if, elif e else


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é o maior')
    print('O segundo número é o menor')
elif n2 > n1:
    print('O segundo número é o maior')
    print('O primeiro número é o menor')
elif n1==n2:
    print('O segundo número é igual ao primeiro')
else:
    print('nenhuma das condições foram satisfeitas...')


