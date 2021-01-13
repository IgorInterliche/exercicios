#Acrescentei funções para otimizar esse programa, deixando ele mais prático.
def imp_vetor( vDes= (), vCol = ()):
    #imprime vetor em linhas...
    tot_col = len(vCol)
    tot_des = len(vDes)
    col_atu = 0
    for pos in range(0, tot_des):
        campo = str(vDes[pos])   #precisa converter por causa dos campos numéricos...
        tot_esp = vCol[col_atu] - len(campo)  #tamanho do campo desejado - tamanho do campo atual
        campo = campo + (tot_esp * ' ')
        if col_atu < tot_col - 1:
            print(campo, end='')
            col_atu = col_atu + 1
        else:
            print(campo)
            col_atu = 0
    print(' ')

def soma_lista(vLista):
    #soma os itens de uma lista (vetor)
    car_lin = 0
    col_tot = len(vLista)
    for pos in range(0, col_tot):
        car_lin = car_lin + vLista[pos]
    return car_lin

#iniciação das variáveis-----------
listagem = ('Monitor', 989.99,'duplo','1', 'sim', 23, 'jose',
            'Teclado', 50.99,'simples','2', 'nao', 26, 'pedro',
            'Mouse', 40.99,'duplo','3', 'nao', 30, 'maria',
            'Headset', 80.00,'simples','4', 'sim', 10, 'janaina',
            'Controle sem fio', 399.99,'duplo','5', 'não', 10, 'maria eduarda',
            'Caixas de som', 99.99,'simples','6', 'sim', 40, 'josefina',
            'Carregador celular', 29.99,'duplo', '7', 'nao', 50, 'eliete')

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

lin_sep = '-' * soma_lista(coluna)

#---------------------@
#
#_____execução___
#
print()
print('Listagem de Produtos')
print(lin_sep)
imp_vetor(cabecalho, coluna)
print(lin_sep)
imp_vetor(listagem, coluna)
print(lin_sep)
#
#______fim_______
#


