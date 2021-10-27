# Alterado para considerar qualquer numero de colunas, mas sem nenhuma formatação.
# iniciação das variáveis-----------
listagem = (('Monitor', 'duplo',  'sim', '0k', 1),
            ('Teclado', '', 'nao'),
            ('Mouse', 'duplo', 'nao'))

cabecalho = ('produto----', 'Tipo-----', 'status---', 'numero')

# impressão das linhas detalhe----
total_linhas = len(listagem)
for linha in range(0, total_linhas):
    tot_colunas = len(listagem[linha])
    for coluna in range(0, tot_colunas):
        campo = listagem[linha][coluna]
        print(campo, ' ', end='')
    print()
