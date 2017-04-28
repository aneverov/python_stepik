"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, 
заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме 
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний 
элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""

a = input()
b = []
c = 0
i = 0
j = 0
finallist = []
while a != 'end':
	b.append([int(i) for i in a.split()])
	i += 1
	a = input()
print(b)
# Создание расширенного списка
for j in range(len(b)):
	b[j].insert(0, 0)
	b[j].insert(len(b) + 1, 0)
b.insert(0, [0] * (len(b) + 2))
b.insert(len(b) + 1, [0] * (len(b) + 2))
print(b)

c = int(b[i - 1][j]) + int(b[i + 1][j]) + int(b[i][j - 1]) + int(b[i][j + 1])
print(c)
print(int(b[i - 1][j]))
print(int(b[i + 1][j]))
print(int(b[i][j - 1]))
print(int(b[i][j + 1]))
"""
for i in range(len(b)):
	for j in range(len(b)):
		c = int(b[i - 1][j]) + int(b[i + 1][j]) + int(b[i][j - 1]) + int(b[i][j + 1])
		finallist.append(c)
print(finallist)


#print(c)
"""
