# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio_lista as relatorio

listagem = [('Televisão', 989.123, 'duplo', 'jose'),
            ('Controle sem fio', 399.99, 'duplo', 'maria eduarda'),
            ('Caixas de som', 99.99, 'simples', 'josefina'),
            ('Carregador celular', 29.99, 'duplo', 'eliete')]

cabecalho = [('Item', 19, False, False),
             ('Valor Final', 12, False, False),
             ('Capacidade', 10, True, False),
             ('Nome do Comprador', 40, True, False)]


relatorio.processar(listagem, cabecalho, 'Relatório B')

