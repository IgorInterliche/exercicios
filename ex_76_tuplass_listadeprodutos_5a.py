# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio_tupla as relatorio

listagem = ('Monitor', 999.789, 'duplo', '1', 'sim', 23, 'jose',
            'Teclado', 50.99, 'simples', '2', 'nao', 26, 'pedro',
            'Mouse', 40.99, 'duplo', '3', 'nao', 30, 'maria',
            'Headset', 80.00, '', '4', 'sim', '', 'janaina',
            'Controle sem fio', 399.99, 'duplo', '5', 'não', 1, 'maria eduarda',
            'Caixas de som', 99.99, 'simples', '6', 'sim', 40, 'josefina',
            'Carregador celular', 29.99, 'duplo', '7', 'nao', 50, 'Eliete')

# item, tamanho, alinhamento, moeda
colunas = [('Descrição do Produto', 23, True, False),
           ('Valor', 9, False, False),
           ('Tipo', 7, False, False),
           ('Item', 4, True, False),
           ('Em estoque', 11, True, False),
           ('Lote', 5, True, False, False),
           ('Nome vendedor', 20, True, False)]

relatorio.processar(listagem, colunas, "Relatório A")
#                 #
# ______fim_______#
