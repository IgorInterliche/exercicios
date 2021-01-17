# main program #
# iniciação das variáveis-----------
#
import Util.vetores as util
import ex_76_tuplass_listadeprodutos_funcoes as fun

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

lin_sep = '-' * util.soma_lista(coluna)  # soma_lista a partir da biblioteca util.

# ---------------------@
# _____execução___
#
print()
print('Listagem de Produtos b')
print(lin_sep)
fun.imp_vetor(cabecalho, coluna)
print(lin_sep)
fun.imp_vetor(listagem, coluna)
print(lin_sep)
#                #
# ______fim_______#
