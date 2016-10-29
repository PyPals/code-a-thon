import json

json_file = open('/Users/apple/Desktop/ques12b.json')
data = json.load(json_file)

d15 = {}
d16 = {}
diff_dict = {}
key_list = []

for x in data:
	pos = x['POS']
	key_list.append(pos)
	try:
		dct = d15[pos]
	except:
		dct = None
	if dct is None:
		d15[pos] = x['Pax Count']
	else:
		d15[pos] = str(int(x['Pax Count']) + int(dct))
	if x['Date'][-4:] == '2015':
		d15[pos] = dct
	else:
		d16[pos] = dct

print d15
print d16

for key in key_list:
	try:
		diff_dict[key] = int(d15[key]) - int(d16[key])
	except:
		diff_dict[key] = None
print diff_dict
