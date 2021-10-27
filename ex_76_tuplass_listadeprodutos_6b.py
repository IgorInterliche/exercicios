import ex_76_tuplass_listadeprodutos_relatorio_lista as relatorio

listagem = [(1, 'Televisão portatil ', 989.129, 'duplo', 'jose'),
            (2, 'Controle sem fio', 399.9940, 'duplo', 'maria eduarda'),
            (3, 'Caixas de som', 99.99, 'simples', 'josefina'),
            (4, 'Carregador celular', 29.99, 'duplo', 'eliete')]

# colunas:       item, tamanho, Alinhamento(E/D), Moeda(S/N)
info_colunas = [('Cód.', 6, False, False),
                ('Item vendido', 20, True, False),
                ('Valor Final', 15, False, True),
                ('Capacidade', 10, True, True),
                ('Nome do Comprador', 25, True, False)]

relatorio.processar(listagem, info_colunas, 'Relatório 6B')
