import re
f = open('day7-input.txt', 'r')

total = 0
for i in f.readlines():
	j = 0
	inHypernet = 0
	while j < len(i) - 2:
		testString = ""
		if i[j] == '[':
			inHypernet = 1
		elif i[j] == ']':
			inHypernet = 0
		if inHypernet == 0 and i[j] == i[j+2] and i[j] != i[j+1] and i[j+1] != '[' and i[j+1] != ']':
			testString += i[j+1] + i[j] + i[j+1]
			regex = '\[[^\]]*' + testString + '[^\]]*\]'
			result = re.search(regex, i)
			if result:
				total += 1
				break
		j += 1
print "The number of strings that support TLS is " + str(total) + "."
