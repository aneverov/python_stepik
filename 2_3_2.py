a = int(input())
b = int(input())
s = 0
d = 0
for i in range(a, b + 1):
	if i % 3 == 0:
		s = s + i
		d = d + 1
print(s / d, end='\t')