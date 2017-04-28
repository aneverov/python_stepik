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
while a != 'end':
	b.append([int(i) for i in a.split()])
	i += 1
	a = input()
if len(b) != 1:
	for i in range(len(b)):
		for j in range(len(b[0])):
			if i == 0 and j == 0:
				c = int(b[len(b) - 1][j]) + int(b[i + 1][j]) + int(b[i][len(b[0]) - 1]) + int(b[i][j + 1])
			elif i == 0 and j == 1:
				c = int(b[len(b) - 1][j]) + int(b[i + 1][j]) + int(b[i][j - 1]) + int(b[i][j + 1])
			elif i == 0 and j == 2:
				c = int(b[len(b) - 1][j]) + int(b[i + 1][j]) + int(b[i][j - 1]) + int(b[i][0])
			elif i == 1 and j == 2: 		
				c = int(b[i - 1][j]) + int(b[i + 1][j]) + int(b[i][j - 1]) + int(b[i][0])
			elif i == 2 and j == 0: 
				c = int(b[i - 1][j]) + int(b[0][j]) + int(b[i][j - 1]) + int(b[i][j + 1]) 
			elif i == 2 and j == 1: 
				c = int(b[i - 1][j]) + int(b[0][j]) + int(b[i][j - 1]) + int(b[i][j + 1]) 
			elif i == 2 and j == 2: 
				c = int(b[i - 1][j]) + int(b[0][j]) + int(b[i][j - 1]) + int(b[i][0]) 
			else:
				c = int(b[i - 1][j]) + int(b[i + 1][j]) + int(b[i][j - 1]) + int(b[i][j + 1])
			print(c, end=' ')
		print()
else:
	print(int(b[0][0]) * 4)