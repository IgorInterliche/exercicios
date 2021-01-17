import Util.vetores as util


def proc(vitens, vcab, vtamcol, stitulo):
    lin_sep = '-' * util.soma_lista(vtamcol)  # soma_lista a partir da biblioteca util.
    print()
    print('Listagem de Produtos ', stitulo)
    print(lin_sep)
    imprime(vcab, vtamcol)
    print(lin_sep)
    imprime(vitens, vtamcol)
    print(lin_sep)


def imprime(vdes, vcol):

    tot_col = len(vcol)    # Total de colunas
    tot_itens = len(vdes)  # total de itens a serem impressos em todas as colunas#
    col_atu = 0            # inicializa para a coluna 1 para entrar no loop do processamento...

    for pos in range(0, tot_itens):
        if type(vdes[pos]) == float or type(vdes[pos]) == int:
            campo = str(vdes[pos])  # precisa converter por causa dos campos numéricos...
        else:
            campo = vdes[pos]

        tot_esp = vcol[col_atu] - len(campo)  # Total espaços=tamanho do campo desejado - tamanho do campo atual
        campo = campo + (tot_esp * ' ')       # acrescenta os espaços ao final do campo para ficarem todos alinhados.
        if col_atu < tot_col - 1:             # inibe a impressão do proximo print na proxima linha.
            print(campo, end='')
            col_atu = col_atu + 1
        else:
            print(campo)
            col_atu = 0
