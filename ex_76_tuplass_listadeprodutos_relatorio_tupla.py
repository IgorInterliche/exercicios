# "Clean code", "tell_don't_ask"
import Util.tipos as tipo


def processar(itens_relatorio, informacoes_colunas, stitulo):

    total_colunas = len(informacoes_colunas)
    nome_colunas = []
    tamanho_colunas = []
    alinha_colunas = []
    moeda_colunas = []
    comprimento_do_relatorio = 0
    for i in range(0, total_colunas):
        comprimento_do_relatorio = comprimento_do_relatorio + informacoes_colunas[i][1]
        nome_colunas.append(informacoes_colunas[i][0])
        tamanho_colunas.append(informacoes_colunas[i][1])
        alinha_colunas.append(informacoes_colunas[i][2])
        moeda_colunas.append((informacoes_colunas[i][3]))

    lin_sep = "-" * comprimento_do_relatorio

    # * vetores.soma_lista(vetor_tam_coluna)
    print()
    print("Listagem de Produtos ", stitulo)
    print(lin_sep)
    print_report(nome_colunas, tamanho_colunas, alinha_colunas, moeda_colunas)
    print(lin_sep)
    print_report(itens_relatorio, tamanho_colunas, alinha_colunas, moeda_colunas)
    print(lin_sep)


def _is_field_float(field_value):
    return type(field_value) == float


def _is_field_int(field_value):
    return type(field_value) == int


def _print_line(field, field_size, field_alinhamento, field_moeda, new_line=True):
    if _is_field_float(field):
        field = tipo.float_em_str_moeda_real(field, field_moeda)
    elif _is_field_int(field):
        field = str(field)

    spaces_num = field_size - len(field) + 1
    spaces = spaces_num * ' '
    if field_alinhamento:
        field = field + spaces
    else:
        field = spaces + field + ' '

    new_line = "\n" if new_line else ""
    print(field, end=new_line)


def print_report(fields_value, fields_size, fields_alinhamento, fields_moeda):
    fields_total = len(fields_value)
    colums_total = len(fields_size)
    actual_column = 0

    for position in range(0, fields_total):
        if actual_column < colums_total-1:
            _print_line(fields_value[position],
                        fields_size[actual_column],
                        fields_alinhamento[actual_column],
                        fields_moeda[actual_column],
                        False)
            actual_column = actual_column + 1
        else:
            _print_line(fields_value[position],
                        fields_size[actual_column],
                        fields_alinhamento[actual_column],
                        fields_moeda[actual_column])
            actual_column = 0
