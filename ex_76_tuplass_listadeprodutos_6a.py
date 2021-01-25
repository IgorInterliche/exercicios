# main program #
# acrescentado as listas
#
import ex_76_tuplass_listadeprodutos_relatorio_lista as relatorio

listagem = [('Monitor', 999.7899999, 'duplo', '1', 'sim', 23, 'jose'),
            ('Teclado', 50.99, 'simples', '2', 'nao', 26, 'pedro'),
            ('Mouse', 40.99, 'duplo', '3', 'nao', 30, 'maria'),
            ('Headset', 80.00, '', '4', 'sim', '', 'janaina'),
            ('Controle sem fio', 399.99, 'duplo', '5', 'não', 1, 'maria eduarda'),
            ('Caixas de som', 99.99, 'simples', '6', 'sim', 40, 'josefina'),
            ('Carregador celular', 29.99, 'duplo', '7', 'nao', 50, 'Eliete')]

#            item,  tamanho, alinhamento, moeda
info_colunas = [('Descrição', 20, True, False),
           ('Valor', 10, False, False),
           ('Tipo', 7, False, False),
           ('Item', 6, True, False),
           ('Em estoque', 11, True, False),
           ('Lote', 5, True, False, False),
           ('Nome vendedor', 23, True, False)]

# Teste do loop no vetor duplo... controlando as linnhas e itens:

# for a in range(0, len(colunas)):
#    for b in range(0, len(colunas[a])):
#        print(colunas[a][b])


relatorio.processar(listagem, info_colunas, "Relatório A")
#                 #
# ______fim_______#
