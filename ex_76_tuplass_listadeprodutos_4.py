# Acrescentei funções, uma interna e outra na biblioteca utl.

import Util.vetores

def imp_vetor(vdes, vcol):
    # imprime vetor em linhas...
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
    print(' ')


# main program #
#
# iniciação das variáveis-----------
#
listagem = ('Monitor', 989.99, 'duplo', '1', 'sim', 23, 'jose',
            'Teclado', 50.99, 'simples', '2', 'nao', 26, 'pedro',
            'Mouse', 40.99, 'duplo', '3', 'nao', 30, 'maria',
            'Headset', 80.00, 'simples', '4', 'sim', 10, 'janaina',
            'Controle sem fio', 399.99, 'duplo', '5', 'não', 1, 'maria eduarda',
            'Caixas de som', 99.99, 'simples', '6', 'sim', 40, 'josefina',
            'Carregador celular', 29.99, 'duplo', '7', 'nao', 50, 'eliete')

cabecalho = ('Descrição do Produto',
             'Valor',
             'Tipo',
             'Item',
             'Em estoque',
             'Lote',
             'Nome vendedor')

coluna = (23,
          8,
          9,
          6,
          12,
          5,
          20)

lin_sep = '-' * Util.vetores.soma_lista(coluna)  # soma_lista a partir da biblioteca util.

# ---------------------@
# _____execução___
#
print()
print('Listagem de Produtos')
print(lin_sep)
imp_vetor(cabecalho, coluna)
print(lin_sep)
imp_vetor(listagem, coluna)
print(lin_sep)
#                #
# ______fim_______#
