"""import math
n = int(input())
m = []
a = [int(i) + 1 for i in range(n)]
for i in a:
	if i <= len(a):
		m.append([a[i - 1] * [math.fabs(i)]])
print(m)"""

n = int(input())
m = []
for i in range(n + 1):
	m += (i * [i])
for i in range(n):
	print(m[i], end=' ')


"""
a=[]
n=int(input())
for i in range(n+1):
    a+=(i*[i])
for i in range(n):
    print(a[i], end=' ')"""