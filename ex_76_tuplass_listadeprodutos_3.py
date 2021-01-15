# Acrescentei funções para otimizar esse programa, deixando ele mais prático
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


def soma_lista(vlista):  # soma os itens de uma lista (vetor)
    car_lin = 0
    col_tot = len(vlista)
    for pos in range(0, col_tot):
        if type(vlista[pos]) == float or type(vlista[pos]) == int:
            car_lin = car_lin + vlista[pos]
        else:
            print('campo não númerico encontrado no vetor')
            return 0
    return car_lin


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

lin_sep = '-' * soma_lista(coluna)

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
