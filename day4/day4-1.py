import operator
import collections
f = open('day4-input.txt', 'r')

sum = 0
for i in f.readlines():
	real = 1
	base = i.split('[')
	codes = base[0][0:-3]
	sector = base[0][-3:]
	checkSum = base[1][0:-2]
	codes = "".join(sorted(codes.replace("-", "")))
	common = collections.Counter(codes).most_common() 
	common = sorted(common, key=lambda x:(-x[1], x[0]))[0:5]
	j = 0
	while j < 5:
		if common[j][0] != checkSum[j]:
			real = 0
		j = j + 1
	if real == 1:
		sum = sum + int(sector)
print "The sum of the keys is " + str(sum) + "."
