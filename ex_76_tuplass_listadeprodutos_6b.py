import ex_76_tuplass_listadeprodutos_relatorio_lista as relatorio

listagem = [(1, 'Televisão', 99989.129, 'duplo', 'jose'),
            (2, 'Controle sem fio', 399.9940, 'duplo', 'maria eduarda'),
            (3, 'Caixas de som', 99.99, 'simples', 'josefina'),
            (4, 'Carregador celular', 29.99, 'duplo', 'eliete')]

# colunas:       item, tamanho, Alinhamento(E/D), Moeda(S/N)
info_colunas = [('Código', 6, False, False),
                ('Item', 18, True, False),
                ('Valor Final', 15, False, True),
                ('Capacidade', 10, False, True),
                ('Nome do Comprador', 25, True, False)]

relatorio.processar(listagem, info_colunas, 'Relatório 6B')
