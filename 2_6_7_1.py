"""
Выведите таблицу размером n×n, заполненную числами от 1 до n*2 по спирали, выходящей из левого верхнего 
угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
a = int(input())
i = 1
b = []
c = []
d = [[0 for j in range(a)] for i in range(a)]
e = []
f = []
g = []
h = []
k = []
l = []
while i < a ** 2:
	for i in range(a):
		for j in range(a):
			b.insert(i, i)
			i += 1
		a -= 1
		j += 1
		print(b)
#print(d)
#d.remove(d[0])
#print(d)
#d.insert(0, b)
#print(d)
"""
while i < a ** 2:
		
	break

		for j in range(a - 1):
			c.insert(j, i)
			i += 1
		print(c)	
		for j in range(a - 1):
			d.insert(j, i)
			i += 1
		print(d)	
		for j in range(a - 2):
			e.insert(j, i)
			i += 1
		print(e)
		for j in range(a - 2):
			f.insert(j, i)
			i += 1
		print(f)
		for j in range(a - 3):
			g.insert(j, i)
			i += 1
		print(g)
		for j in range(a - 3):
			h.insert(j, i)
			i += 1
		print(h)
		for j in range(a - 4):
			k.insert(j, i)
			i += 1
		print(k)
		for j in range(a - 4):
			l.insert(j, i)
			i += 1
		print(l)
		break
	
"""
	

