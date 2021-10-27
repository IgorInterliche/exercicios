def printi():

    print("Igor S/A")

times = ('Corintians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Vasco', 'Botafogo', 'Atlético-PR',
         'Bahia', 'São Paulo', 'Fluminense', 'Chapecoense',
         'Ponte Preta',)

printi()
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {times[-4]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição')
printi()
