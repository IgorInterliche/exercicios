# main program #
# iniciação das variáveis-----------
#
import Util.vetores as util
import ex_76_tuplass_listadeprodutos_funcoes as fun

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

lin_sep = '-' * util.soma_lista(coluna)  # soma_lista a partir da biblioteca util.

# ---------------------@
# _____execução___
#
print()
print('Listagem de Produtos a')
print(lin_sep)
fun.imp_vetor(cabecalho, coluna)
print(lin_sep)
fun.imp_vetor(listagem, coluna)
print(lin_sep)
#                #
# ______fim_______#
