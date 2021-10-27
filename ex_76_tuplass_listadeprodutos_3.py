# Acrescentei funções para otimizar esse programa, deixando ele mais prático
def imp_vetor(vdes, vcol):
    # imprime vetor em linhas..........
    lin_total = len(vdes)
    col_total = len(vcol)
    for lin in range(0, lin_total):
        for col in range(0, col_total):
            print(alinha_campo(vdes[lin][col], vcol[col]), end='')
        print()


def alinha_campo(campo_original, campo_tamanho):
    espaco = campo_tamanho - len(campo_original)
    espaco = ' ' * espaco
    return campo_original + espaco


def soma_itens_lista(vlista):  # soma os itens de uma lista (vetor)
    car_lin = 0
    col_tot = len(vlista)
    for pos in range(0, col_tot):
        if type(vlista[pos]) == int:
            car_lin = car_lin + vlista[pos]
        else:
            print('campo não númerico encontrado no vetor')
            return 0
    return car_lin


# main program #
listagem = [('Monitor', '989.99', 'duplo', '1', 'sim', 'jose', ),
            ('Teclado', '50.99', 'simples', '2', 'nao', 'pedro', ),
            ('Mouse', '40.99', 'duplo', '3', 'nao', 'maria', ),
            ('Headset', '80.00', 'simples', '4', 'sim', 'janaina',),
            ('(Controle sem fio', '399.99', 'duplo', '5', 'não', 'maria eduarda', ),
            ('Caixas de som', '99.99', 'simples', '6', 'sim', 'josefina', ),
            ('Carregador celular', '29.99', 'duplo', '7', 'nao', 'eliete')]

cabecalho = [('Descrição do Produto',
              'Valor',
              'Tipo',
              'Em estoque',
              'Lote',
              'Nome vendedor')]

coluna = (23,
          8,
          9,
          6,
          5,
          20)

lin_sep = '-' * soma_itens_lista(coluna)
# ---------------------------------------@
# __execução__
#
print()
print('Listagem de Produtos')
print(lin_sep)
imp_vetor(cabecalho, coluna)
print(lin_sep)
imp_vetor(listagem, coluna)
print(lin_sep)
#                #
# ______fim______#
