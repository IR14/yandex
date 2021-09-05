import math

s = input()

n, i, j = list(map(int, s.split()))
  
diff = abs(j - i)

if diff < n / 2:
	print(diff - 1)
else:
    print(n - diff - 1)
