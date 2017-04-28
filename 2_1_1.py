a = int(input())
s = 0
i = a
if i == 0:
	print(i)
else:
	while i != 0:
		s += i  # сумма
		i = int(input())
		if i == 0:
			print(s)
	