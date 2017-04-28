a = int(input())

b = a // 1000
c = a % 1000

d = b // 100
e = (b % 100) // 10
f = b % 10

m = d + e + f

j = c // 100
k = (c % 100) // 10
l = c % 10

n = j + k + l

if m == n:
	print('Счастливый')
else:
	print('Обычный')
