s = input()

x, y, _ = list(map(int, s.split()))

if x <= 12:
	if y > 12:
		print(1)

	elif y == x:
		print(1)

	else:
		print(0)

else:
	print(1)
