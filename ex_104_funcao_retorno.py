def is_int(field_value):
    return type(field_value) == int


while True:

    wnum = str(input('digite um numero: '))
    if is_int(wnum):
        num = int(wnum)
        print("voce acabou de digitar o numero {num}")
