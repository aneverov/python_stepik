a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c and b <= a and b <= c:
	print(a, '\n', b, '\n', c,'\n')
elif a >= b and a >= c and c <= a and c <= b:
	print(a, '\n', c, '\n', b,'\n')
elif b >= a and b >= c and c <= a and c <= b:
	print(b, '\n', c, '\n', a,'\n')
elif b >= a and b >= c and a <= c and a <= b:
	print(b, '\n', a, '\n', c,'\n')
elif c >= a and c >= b and a <= c and a <= b:
	print(c, '\n', a, '\n', b,'\n')
elif c >= a and c >= b and b <= a and b <= c:
	print(c, '\n', b, '\n', a,'\n')
