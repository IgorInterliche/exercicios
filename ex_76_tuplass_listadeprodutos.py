import Util.tipos as tipo


listagem = ('Monitor', 989.99,
          'Teclado', 50.99,
          'Mouse', 40.99,
          'Headset', 80.00,
          'Controle sem fio', 399.99,
          'Caixas de som', 99.99,
        'Carregador para celular', 29.99)

print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if tipo.is_par(pos):
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
