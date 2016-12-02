def turnRight(direction):
	if direction == "north":
		return "east"
	elif direction == "east":
		return "south"
	elif direction == "south":
		return "west"
	elif direction =="west":
		return "north"

def turnLeft(direction):
        if direction == "north":
                return "west"
        elif direction == "east":
                return "north"
        elif direction == "south":
                return "east"
        elif direction =="west":
                return "south"

direction ="north"
xCord = 0
yCord = 0

visited = []
counter = 0
visited.append((xCord,yCord))
firstIntersection = 0

for i in "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3".split(', '):
	if i[0] == 'R':
		direction=turnRight(direction)
	elif i[0] == 'L':
		direction=turnLeft(direction)
	stepCounter = 0
	while stepCounter < int(i[1:]):
		if direction=="north":
			yCord = yCord + 1
		elif direction=="east":
			xCord = xCord + 1
		elif direction=="south":
			yCord = yCord - 1
		elif direction=="west":
			xCord = xCord - 1
		for j in visited:
			if j == (xCord, yCord) and firstIntersection == 0:
				print "This is the first time you've crossed your own path. Your location is:"
				print "x = " + str(xCord)
				print "y = " + str(yCord)
				print "Which is " + str(abs(xCord) + abs(yCord)) + " blocks away from where you started."
				firstIntersection = 1
		stepCounter = stepCounter + 1
		visited.append((xCord,yCord))
		counter = counter + 1

print "\n\nYour final location is:"
print "x = " + str(xCord)
print "y = " + str(yCord)
print "Which is " + str(abs(xCord) + abs(yCord)) + " blocks away from where you started."
