# Exercício proposta para considerar 3 colunas,
# agora passando também mais 2 vetores:
# 1) descrição dos cabeçalhos;
# 2) tamanho dos campos;

listagem = ('Monitor  ', 989.99, 'Eletronico',
            'Teclado  ', 50.99, 'utilitario',
            'Mouse    ', 40.99, 'utiitario',
            'Headset  ', 80.00, 'eletronico',
            'Controle sem fio', 399.99, 'utilitario',
            'Caixas de som', 99.99, 'utilitario',
            'Carregador para celular', 29.99, 'utilitario',
            'Testador de carga',100.00, 'utilitario')

print()
print('Listagem de Preços')
print('-' * 55)

col = 1

for pos in range(0, len(listagem)):
    if col == 1:
        print(listagem[pos], ' ', end='')
        col = 2
    elif col == 2:
        print(listagem[pos], ' ', end='')
        col = 3
    elif col ==3:
        print(listagem[pos])
        col = 1


