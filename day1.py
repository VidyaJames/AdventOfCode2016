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

instructionList = raw_input("enter instructions: ").split(', ')
direction ="north"
xCord = 0
yCord = 0

visited = []
counter = 0
visited.append((xCord,yCord))
firstIntersection = 0

for i in instructionList:
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
				print "\n\nThis is the first time you've crossed your own path. Your location is:"
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
