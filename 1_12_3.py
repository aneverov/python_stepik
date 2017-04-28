a = float(input())
b = float(input())
c = input()

if c == '+':
	d = a + b
	print(d)
elif c == '-':
	d = a - b
	print(d)
elif c == '/':
	if b != 0:
		d = a / b
		print(d)
	else:
		print('Деление на 0!')
elif c == '*':
	d = a * b
	print(d)
elif c == 'mod':
	if b != 0:
		d = a % b
		print(d)
	else:
		print('Деление на 0!')
elif c == 'pow':
	d = a ** b
	print(d)
elif c == 'div':
	if b != 0:
		d = a // b
		print(d)
	else:
		print('Деление на 0!')