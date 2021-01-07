#Alterado para considerar qualquer numero de colunas, mas sem nenhuma formatação.

# em vez de duas...
listagem = ('Monitor', 989.99,'duplo','1', 'sim', 1,
            'Teclado', 50.99,'simples','2', 'nao', 2,
          'Mouse', 40.99,'duplo','3', 'nao', 3,
          'Headset', 80.00,'simples','4', 'sim', 4,
          'Controle sem fio', 399.99,'duplo','5', 'não',5,
          'Caixas de som', 99.99,'simples','6', 'sim', 6,
        'Carregador celular', 29.99,'duplo', '7', 'nao',7 )

print('-' * 97)
print(f'{"Listagem de Preços":^40}')
print('-' * 97)

#acrescentado dois contadores para reposicionar a coluna.
col_atu = 0  #numero da coluna atual
col_tot = 5  #total de colunas

for pos in range(0, len(listagem)):

    if col_atu < col_tot:
        print(f'{listagem[pos]:<19}', end='')
        col_atu = col_atu + 1

    else:
        print(f' {listagem[pos]}')
        col_atu = 0



