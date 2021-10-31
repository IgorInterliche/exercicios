# Clean code, tell, don't ask...
#import Util.vetores as vetores


def processar(vetor_itens, vetor_cabecalho, vetor_tam_coluna, stitulo):
    lin_sep = "-" * vetores.soma_lista(vetor_tam_coluna)
    print()
    print("Listagem de Produtos ", stitulo)
    print(lin_sep)
    print_report(vetor_cabecalho, vetor_tam_coluna)
    print(lin_sep)
    print_report(vetor_itens, vetor_tam_coluna)
    print(lin_sep)


def _is_field_float_or_int(field_value):
    return type(field_value) == float or type(field_value) == int


def _print_line(field, field_size, new_line=True):
    if _is_field_float_or_int(field):
        field = str(field)

    spaces = field_size - len(field)
    field = field + (spaces * " ")
    new_line = "\n" if new_line else ""
    print(field, end=new_line)


def print_report(fields_value, fields_size):
    fields_total = len(fields_value)
    colums_total = len(fields_size)
    actual_column = 0

    for position in range(0, fields_total):
        if actual_column < colums_total-1:
            _print_line(fields_value[position], fields_size[actual_column], False)
            actual_column = actual_column + 1
        else:
            _print_line(fields_value[position], fields_size[actual_column])
            actual_column = 0
