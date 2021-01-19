# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio as relatorio

listagem = ('Monitor', 989.99, 'duplo', 'jose',
            'Controle sem fio', 399.99, 'duplo', 'maria eduarda',
            'Caixas de som', 99.99, 'simples', 'josefina',
            'Carregador celular', 29.99, 'duplo', 'eliete')
cabecalho = ('Descrição do Produto',
             'Valor',
             'Tipo',
             'Nome vendedor')
coluna = (23,
          8,
          9,
          20)


relatorio.processar(listagem, cabecalho, coluna, 'Relatório B')

