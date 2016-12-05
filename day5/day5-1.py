import hashlib
counter = 0
base = "ffykfhsq"
code = ""
while len(code) < 8:
	done = 0
	while done == 0:
		text = base + str(counter)
		hashed = hashlib.md5(text).hexdigest()
		if hashed[0:5] == "00000":
			code = code + hashed[5]
			done = 1
		counter = counter + 1
print "the code is " + code + "."
