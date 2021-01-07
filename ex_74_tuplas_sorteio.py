
from random import randint

n = (randint(1, 11), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1,10))
print(f'Os valores sorteados são {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
