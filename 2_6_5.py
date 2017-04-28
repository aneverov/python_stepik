

"""
Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, 
которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.

Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" 
(без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""
lst = [int(i) for i in input().split()]
x = int(input())
b = []
i = 0
a = len(lst)
if x not in lst:
	print('Отсутствует')
while i < a:
	if lst[i] == x:
		b.append(lst.index(x))
		lst[i] += 1
	i += 1
for i in range(len(b)):
	print(b[i], end=' ')

"""
lst = [int(i) for i in input().split()]
x = int(input())
b = []
i = 0
if x not in lst:
	print('Отсутствует')
for i in lst:
	if lst[i] == x:
		b.append(lst.index(x))
		#lst[i] += 1
	print(b)
"""
		
	
