# main program #
# iniciação das variáveis-----------
#
import ex_76_tuplass_listadeprodutos_relatorio_lista as relatorio

listagem = [('Carro', 110989.129, 'duplo', 'jose'),
            ('Controle sem fio', 399.9940, 'duplo', 'maria eduarda'),
            ('Caixas de som', 99.99, 'simples', 'josefina'),
            ('Carregador celular', 29.99, 'duplo', 'eliete')]

# colunas: item, tamanho, Alinhamento(D/E), Moeda(s/n)
info_colunas = [('Item', 19, False, False),
                ('Valor Final', 12, False, True),
                ('Capacidade', 10, True, True),
                ('Nome do Comprador', 25, True, False)]

relatorio.processar(listagem, info_colunas, 'Relatório B')

