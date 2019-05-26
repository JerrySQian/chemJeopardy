f = open("unit3.txt", "r")
l = f.readlines()
writeFile = open("unit3Formatted.txt", "w")

writeFile.write("[")

for i in range(0, len(l)):
	l[i] = l[i].strip("\n")

for i in range(0, 15):
	question = l[7 * i]
	a1 = l[7 * i + 1]
	a2 = l[7 * i + 2]
	a3 = l[7 * i + 3]
	a4 = l[7 * i + 4]
	correct = l[7 * i + 5]
	exp = l[7 * i + 6]

	writeFile.write("\t[%r, %r, %r, %r, %r, %r, %r],\n" % (question, a1, a2, a3, a4, correct, exp))


#target.write('%r \n%r \n%r \n') % (line1, line2, line3)

writeFile.write("]")

writeFile.close()
f.close()