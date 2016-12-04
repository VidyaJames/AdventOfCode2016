f = open('day4-input.txt', 'r')

for i in f.readlines():
	base = i.split('[')
	codes = base[0][0:-4]
	sector = base[0][-3:]
	newCode = ""
	for j in codes:
		if j == "-":
			newCode = newCode + " "
		else:
			shift = int(sector) % 26
			if chr(ord(j) + shift) > 'z':
				shift = shift - 26
			j = chr(ord(j) + shift)
			newCode = newCode + j
	if newCode == "northpole object storage":
		print "The North Pole objects are stored at sector ID " + sector + "."
