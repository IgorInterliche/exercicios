# Clean code, tell, don't ask...

import Util.vetores as ut


def processar(vetor_itens, vetor_cabecalho, vetor_tam_coluna, stitulo):
    lin_sep = "-" * ut.soma_lista(vetor_tam_coluna)
    print()
    print("Listagem de Produtos ", stitulo)
    print(lin_sep)
    print_report(vetor_cabecalho, vetor_tam_coluna)
    print(lin_sep)
    print_report(vetor_itens, vetor_tam_coluna)
    print(lin_sep)


def _is_value_float_or_int(position_value):
    return type(position_value) == float or type(position_value) == int


def _print_line(field, columns_size, end_of_line):
    if _is_value_float_or_int(field):
        field = str(field)

    spaces = columns_size - len(field)
    field = field + (spaces * " ")
    end_of_line = "\n" if end_of_line else ""
    print(field, end=end_of_line)


def print_report(fields, fields_size):
    fields_total = len(fields)
    colums_total = len(fields_size)
    actual_column = 0

    for position in range(0, fields_total):
        if actual_column < colums_total-1:
            _print_line(fields[position], fields_size[actual_column], False)
            actual_column = actual_column + 1
        else:
            _print_line(fields[position], fields_size[actual_column], True)
            actual_column = 0
