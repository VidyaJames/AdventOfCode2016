import hashlib
counter = 0
base = "ffykfhsq"
code = ['_','_','_','_','_','_','_','_']
while '_' in code:
	text = base + str(counter)
	hashed = hashlib.md5(text).hexdigest()
	if hashed[0:5] == "00000":
		if hashed[5].isdigit():
			place = int(hashed[5])
			if place >= 0 and place <= 7 and code[place] == '_':
				code[place] = hashed[6]
	counter = counter + 1
print "the code is " + "".join(code) + "."
