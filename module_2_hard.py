from random import randint

n = randint(3,20)
res = ''
for i in range(1, n):
    for k in range(i+1, n):
        if n % (i + k) == 0:
            res += f'{i}{k}'
print(f'{n} - {res}')