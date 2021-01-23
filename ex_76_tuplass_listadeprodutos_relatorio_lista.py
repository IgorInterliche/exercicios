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
    _print_cabecalho(nome_colunas, tamanho_colunas, alinha_colunas, moeda_colunas)
    print(lin_sep)
    _print_report(itens_relatorio, tamanho_colunas, alinha_colunas, moeda_colunas)
    print(lin_sep)


def _is_field_float(field_value):
    return type(field_value) == float


def _is_field_int(field_value):
    return type(field_value) == int


def _print(field, field_size, field_alinhamento, field_moeda, new_line=True):
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


def _print_cabecalho(fields_value, fields_size, fields_alinhamento, fields_moeda):
    colunas_total = len(fields_value)
    for field in range(0, colunas_total):
        if field < colunas_total - 1:
            _print(fields_value[field],
                   fields_size[field],
                   fields_alinhamento[field],
                   fields_moeda[field],
                   False)

        else:
            _print(fields_value[field],
                   fields_size[field],
                   fields_alinhamento[field],
                   fields_moeda[field],
                   True)


def _print_report(fields_value, fields_size, fields_alinhamento, fields_moeda):
    linhas_total = len(fields_value)
    for linha in range(0, linhas_total):
        colunas_total = len(fields_value[linha])

        for field in range(0, colunas_total):
            if field < colunas_total - 1:
                _print(fields_value[linha][field],
                       fields_size[field],
                       fields_alinhamento[field],
                       fields_moeda[field],
                       False)

            else:
                _print(fields_value[linha][field],
                       fields_size[field],
                       fields_alinhamento[field],
                       fields_moeda[field],
                       True)
