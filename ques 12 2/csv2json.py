import json
import csv

def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))

json_file = '/Users/apple/Desktop/ques12b.json'
csvfile = open('/Users/apple/Desktop/ques12b.csv')
csv_rows = []
reader = csv.DictReader(csvfile)
title = reader.fieldnames
for row in reader:
    csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
write_json(csv_rows, json_file, format)


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
