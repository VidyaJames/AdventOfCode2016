import operator
f = open("day6-input.txt", 'r')

i = 0
dictList = []
while i < 8:
	dictList.append({})
	i += 1

for i in f.readlines():
	j = 0
	while j < len(i) - 1:
		if i[j] not in dictList[j]:
			dictList[j][i[j]] = 1
		else:
			dictList[j][i[j]] += 1
		j += 1
string = ""
for i in dictList:
	string += max(i.iteritems(), key=lambda x: x[1])[0]

print "the password is " + string + "."

