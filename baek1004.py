import math as m

case = int(input())
count = 0

for _ in range(case):
	x1, y1, x2, y2 = map(int, input().split())
	circle = int(input())
	for _ in range(circle):
		cx, cy, r = map(int, input().split())
		d1 = m.sqrt(m.pow((x1 - cx), 2) + m.pow((y1 - cy), 2))
		d2 = m.sqrt(m.pow((x2 - cx), 2) + m.pow((y2 - cy), 2))
		if (r > d1) and (r > d2):
			continue
		elif (r > d1) or (r > d2):
			count += 1
	print(count)
	count = 0

