
"""
Поиск минимума в списке.
"""
"""

a = [int(i) for i in input('Введите числа через пробел:').split()]
print(a)
b = len(a)
i = 0
k = 0
while i < b - 1:
	if a[i] <= a[i + 1] and a[i] <= a[i - 1]:
		k = a[i]
		print(k)
	if a[i + 1] == b - 1:
		break
	i += 1
print(k)
"""


a = [int(i) for i in input('Введите числа через пробел:').split()]
print(a)
k = a[0]
for x in a:
	if k > x:
		k = x
		print(k)
