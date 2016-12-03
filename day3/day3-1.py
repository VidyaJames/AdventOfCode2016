f = open('day3-input.txt','r')
counter = 0
for i in f.readlines():
	sides = [int(s) for s in i.split() if s.isdigit()]
	sides[0] = int(sides[0])
	sides[1] = int(sides[1])
	sides[2] = int(sides[2])
	sides = sorted(sides)
	if sides[2] < sides[0] + sides[1]:
		counter = counter + 1
print "There are " + str(counter) + " valid triangles."
