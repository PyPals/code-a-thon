import random
import string
import csv

username = raw_input("Enter username\n")

data = ""
csvfile = open('/Users/apple/Desktop/ques11.txt', 'rb')
spamreader = csvfile.read()
data = data + spamreader
print 'DATA' + data
csvfile.close()

csvfile = open('/Users/apple/Desktop/ques11.txt', 'w')

no_of_chars = random.randrange(8, 32)

while True:
	passwd = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(no_of_chars)])
	if username in passwd:
		continue
	if passwd not in data:
		print passwd
		data = data + " " + passwd
		csvfile.write(data)
		break
csvfile.close()