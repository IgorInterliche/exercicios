# Exercício proposta para considerar 3 colunas

listagem = ('Monitor', 989.99, 'Eletronico',
          'Teclado', 50.99, 'utilitario',
          'Mouse', 40.99, 'utiitario',
          'Headset', 80.00, 'eletronico',
          'Controle sem fio', 399.99, 'utilitario',
          'Caixas de som', 99.99, 'utilitario',
        'Carregador para celular', 29.99, 'utilitario',
            'Testador de carga',100.00, 'utilitario')


print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)

col = 0
num_col = 4

for pos in range(0, len(listagem)):
    if col == 0:
        print(f'{listagem[pos]:.<30}', end='')
        col = 1
    elif col == 1:
        print(f'R${listagem[pos]:>7.2f}', end='')
        col = 2
    elif col ==2:
        print(f'  {listagem[pos]}')
        col = 0


