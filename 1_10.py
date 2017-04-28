
A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
	print('Это нормально')
elif A > H:
	print('Недосып')
else:
	print('Пересып')