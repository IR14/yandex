from numpy import argmin

def outer():
	print(argmin((x * x + y * y, y * y + (d - x) * (d - x), x * x + (d - y) * (d - y))) + 1)

d = int(input())

x, y = list(map(int, input().split()))

if 0 <= x <= d:
	if 0 <= y <= d - x:
		print(0)
	else:
		outer()

else:
	outer()
