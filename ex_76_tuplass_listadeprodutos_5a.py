# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio as rel

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

rel.proc(listagem, coluna, 'Relatório A')
#                #
# ______fim_______#
