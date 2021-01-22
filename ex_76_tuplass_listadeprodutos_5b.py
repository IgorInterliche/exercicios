# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio as relatorio

listagem = ('Televisão', 989.123, 'duplo', 'jose',
            'Controle sem fio', 399.99, 'duplo', 'maria eduarda',
            'Caixas de som', 99.99, 'simples', 'josefina',
            'Carregador celular', 29.99, 'duplo', 'eliete')

cabecalho = ('Item Final',
             'Valor Final',
             'Capacidade',
             'Nome do Comprador')

coluna = (23,
          12,
          12,
          20)


relatorio.processar(listagem, cabecalho, coluna, 'Relatório B')

