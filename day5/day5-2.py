import hashlib
counter = 0
base = "ffykfhsq"
code = ['_','_','_','_','_','_','_','_']
while '_' in code:
	text = base + str(counter)
	hashed = hashlib.md5(text).hexdigest()
	if hashed[0:5] == "00000":
		if hashed[5] in '01234567' and code[int(hashed[5])] == '_':
			code[int(hashed[5])] = hashed[6]
	counter = counter + 1
print "the code is " + "".join(code) + "."
