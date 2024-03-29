#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

from random import randint

amount_coin = int(input('Введите количество монет: '))

random.seed(42)
m = 0
k = 0
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'все монеты{coins}')
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
print(f'всего монет {m, k}')

if m > k:
    ans = k
else:
    ans = m

print(f"Минимальное количество монет, которые нужно перевернуть  {ans}")