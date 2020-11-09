#
valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

        if (valores % 2 == 0):
            valores = pares
            pares = pares + 1
        else:
            valores = impares
            impares = impares + 1

print('=-' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')