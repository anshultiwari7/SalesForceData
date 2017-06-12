import json
import pprint
import csv

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


statustemp = {}
traffic = json.load(open('salesf.json'))

for temp in traffic:
	for key, value in temp.iteritems():
		if key == "Status":
			tempval = value
			if tempval in statustemp.keys():
				statustemp[value]= statustemp[value]+1
			else:
				statustemp[value]=1

				
datastrings=[("Status Description,Count").split(",")]

for key, value in statustemp.iteritems():
	datastrings.append((str(key)+","+str(value)).split(","))

path = "output.csv"

csv_writer(datastrings, path)