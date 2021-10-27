# Alterado para considerar qualquer numero de colunas, mas sem nenhuma formatação.
# iniciação das variáveis-----------

listagem = (('Monitor', 'duplo',  'sim', 'outro item'),
            ('Teclado', 'simples', 'nao'),
            ('Mouse', 'duplo', 'nao'))

total_de_itens = len(listagem)
col_atu = 0
col_tot = 3

for lin in range(0, total_de_itens):
    campo = listagem[lin]

    if col_atu < col_tot-1:
        print(campo, ' ', end='')
        col_atu = col_atu + 1
    else:
        print(campo)
        col_atu = 0
