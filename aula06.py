#metodos da classe string

n = input('Digite algo: ')

print('Iniciando a verificação das informações de', n)
print('Esse número é', (type(n)))
print('Esse número é numérico?', n.isnumeric())
print('Esse número é alfabético?', n.isalpha())
print('Esse número é um decimal?', n.isdecimal())
print('Esse número é minúsculo?', n.islower())
print('Esse número é maiúsculo?', n.isupper())
print('Ele é um dígito?', n.isdigit())
print('Verificação concluída.')


