# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio_tupla as relatorio

listagem = ('Televisão', 99989.129,  'jose',
            'Controle sem fio', 399.99, 'maria eduarda',
            'Caixas de som', 99.99, 'josefina',
            'Carregador celular', 29.99, 'eliete')



cabecalho = ('Item Final',
             'Valor Final',
             'Nome do Comprador')

coluna = (20,
          12,
          20)


relatorio.processar(listagem, cabecalho, coluna, 'Relatório 5b')
