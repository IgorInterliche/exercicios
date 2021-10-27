# "Clean code", "tell_don't_ask"
import Util.tipos as tipo


def processar(itens_relatorio, info_colunas, stitulo):
    nome_colunas = []
    tamanho_colunas = []
    alinha_colunas = []
    moeda_colunas = []
    tamanho_da_linha = 0
    total_colunas = len(info_colunas)
    for i in range(0, total_colunas):
        tamanho_da_linha = tamanho_da_linha + info_colunas[i][1]
        nome_colunas.append(info_colunas[i][0])
        tamanho_colunas.append(info_colunas[i][1])
        alinha_colunas.append(info_colunas[i][2])
        moeda_colunas.append((info_colunas[i][3]))

    lin_sep = "-" * tamanho_da_linha
    print()
    print("Listagem de Produtos ", stitulo)
    print(lin_sep)
    _print_cabecalho(nome_colunas, tamanho_colunas, alinha_colunas, moeda_colunas)
    print(lin_sep)
    _print_report(itens_relatorio, tamanho_colunas, alinha_colunas, moeda_colunas)
    print(lin_sep)


def _format_field(value, size, alinhamento, moeda):
    if tipo.is_float(value):
        value = tipo.float_em_str_moeda_real(value, moeda)
    elif tipo.is_int(value):
        value = str(value)

    spaces_num = size - len(value) + 1
    spaces = spaces_num * ' '
    if alinhamento:
        value = value + spaces
    else:
        value = spaces + value + ' '

    return value


def _print_field(field, new_line=True):
    new_line = "\n" if new_line else ""
    print(field, end=new_line)


def _print_cabecalho(fields_value, fields_size, fields_alinhamento, fields_moeda):
    colunas_total = len(fields_value)
    for col_num in range(0, colunas_total):
        field_formated = _format_field(fields_value[col_num],
                                       fields_size[col_num],
                                       fields_alinhamento[col_num],
                                       fields_moeda[col_num])
        _print_field(field_formated, False)
    print()


def _print_report(fields_value, fields_size, fields_alinhamento, fields_moeda):
    lin_total = len(fields_value)
    for lin_num in range(0, lin_total):
        col_total = len(fields_value[lin_num])
        for col_num in range(0, col_total):
            field_formated = _format_field(fields_value[lin_num][col_num],
                                           fields_size[col_num],
                                           fields_alinhamento[col_num],
                                           fields_moeda[col_num])
            _print_field(field_formated, False)
        print()
