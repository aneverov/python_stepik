fig = input()
if fig == 'прямоугольник':
	a = float(input())
	b = float(input())
	s = a * b
elif fig == 'треугольник':
	a = float(input())
	b = float(input())
	c = float(input())
	p =(a + b + c) / 2
	s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
elif fig == 'круг':
	r = float(input())
	s = 3.14 * (r ** 2)


print(s)
