f = open('day7-input.txt', 'r')

total = 0
for i in f.readlines():
	j = 0
	inHypernet = 0
	bad = 0
	good = 0
	while j < len(i) - 3:
		if i[j] == '[':
			inHypernet = 1
		elif i[j] == ']':
			inHypernet = 0
		if j > 0 and i[j] == i[j+1] and i[j-1] == i[j+2] and i[j] != i[j-1]:
			if inHypernet == 1:
				bad = 1
				break
			else:
				good = 1
		j += 1
	if good == 1 and bad == 0:
		total += 1
print "The number of strings that support TLS is " + str(total) + "."
