valor = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valor)} elementos.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')

if 5 in valor:
    print('Você digitou o elemento 5')
else:
    print('Você NÃO digitou o elemento 5')