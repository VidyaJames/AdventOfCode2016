f = open('day3-input.txt','r')
counter = 0
row = 0
rows= []
for i in f.readlines():
	sides = [int(s) for s in i.split() if s.isdigit()]
	sides[0] = int(sides[0])
	sides[1] = int(sides[1])
	sides[2] = int(sides[2])
	rows.append(sides)
	row = row + 1
	if row > 2:
		row = 0
		j = 0
		while j < 3:
			triangle = sorted([rows[0][j], rows[1][j], rows[2][j]])
			if triangle[2] < triangle[0] + triangle[1]:
				counter = counter + 1
			j = j + 1
		rows=[]
print "There are " + str(counter) + " valid triangles."
