# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random

n = int(input('Введите размер массива: '))
a = [random.randint(0,10) for x in range(n)]
print(a)

x = int(input('Введите число X: '))

count = 0

for i in range(n):
	if a[i] == x:
		count += 1

print(f"Число {x} встречается {count} раз(а)")