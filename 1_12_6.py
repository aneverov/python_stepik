a = int(input())
b = ' программист'
c = str(a)
if a >= 0 and a <= 20:
	if a == 1:
		print(c + b)
	elif 2 <= a <= 4:
		print(c + b + 'а')
	elif a == 0 or 5 <= a <= 20:
		print(c + b + 'ов')

if a >= 21 and a <= 100:
	a = a % 10
	if a == 0 or 5 <= a <= 9:
		print(c + b + 'ов')
	elif 2 <= a <= 4:
		print(c + b + 'а')
	elif a == 1:
		print(c + b)
# 101 - 200
	
d = 100	
while d <= 900:
	
	if a >= (1 + d) and a <= (20 +d):
		a = a - d
		if a == 1:
			print(c + b)
		elif 2 <= a <= 4:
			print(c + b + 'а')
		elif a == 0 or 5 <= a <= 20:
			print(c + b + 'ов')
	if a >= (21 +d) and a <= (100 + d):
		a = a % 10
		if a == 0 or 5 <= a <= 9:
			print(c + b + 'ов')
		elif 2 <= a <= 4:
			print(c + b + 'а')
		elif a == 1:
			print(c + b)
	d = d + 100