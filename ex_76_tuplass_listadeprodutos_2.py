#Alterado para considerar qualquer numero de colunas, mas sem nenhuma formatação.
#iniciação das variáveis-----------
listagem = ('Monitor', 989.99,'duplo','1', 'sim',
            'Teclado', 50.99,'simples','2', 'nao',
            'Mouse', 40.99,'duplo','3', 'nao',
            'Headset', 80.00,'simples','4', 'sim',
            'Controle sem fio', 399.99,'duplo','5', 'não',
            'Caixas de som', 99.99,'simples','6', 'sim',
            'Carregador celular', 29.99,'duplo', '7', 'nao')

des_col = ('  Descrição            ',
           ' Valor    ',
           ' Tipo      ',
           ' Item   ',
           ' Em estoque  ')
tam_col = (20,
           8,
           9,
           8,
           10)

col_atu = 0  #numero da coluna atual
col_tot = len(des_col) #total de colunas
#fim da iniciação das variaveis

#impressão do cabeçalho-----
print()
print('Listagem de Produtos')
print('-' * 66)
for pos in range(0, col_tot):
    print(des_col[pos], end='')
print()
print('-' * 66)
#fim do cabeçalho

#impressão das linhas detalhe----
for pos in range(0, len(listagem)):

    campo = str(listagem[pos])
    n_esp = tam_col[col_atu] - len(campo)
    campo = campo + (n_esp * ' ')

    if col_atu < col_tot-1:

        print(' ', campo, end='')
        col_atu = col_atu + 1
    else:
        print(campo)
        col_atu = 0



