import json
import pprint
import collections
import csv

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

traffic = json.load(open('salesf.json'),object_pairs_hook=collections.OrderedDict)
maxcomments = int(0)
for temp in traffic:
	for key, value in temp.iteritems():
		if key == "Total_Comments":			
			if maxcomments <= int(value):
				maxcomments = int(value)
print maxcomments

# statustemp = {}
# traffic = json.load(open('salesf.json'))

# for temp in traffic:
# 	for key, value in temp.iteritems():
# 		if key == "Status":
# 			tempval = value
# 			if tempval in statustemp.keys():
# 				statustemp[value]= statustemp[value]+1
# 			else:
# 				statustemp[value]=1
				
datastrings=[("Title,Posted By,Status,Vote Points,Total Comments,Comment 1,Comment 2,Comment 3,Commnent 4,Comment 5,Comment 6,Commnent 7,Comment 8,Comment 9,Commnent 10,Comment 11,Comment 12,Commnent 13,Comment 14,Comment 15,Comment 16").split(",")]
sno = int(0)
mainstr = ""
for temp in traffic:
	for key, value in temp.iteritems():
		# print key, value
		if key != "Comments":
			mainstr = mainstr + value + ","
		else:

			tempvalue = value
			for tempcomment in tempvalue:
				for key, value in tempcomment.iteritems():
					mainstr = mainstr + value + ","
	mainstr = mainstr[:-1]
	print mainstr + "\n\n"
	
	datastrings.append(mainstr.encode('utf-8').split(","))
	mainstr = ""
path = "saleforcedata.csv"


csv_writer(datastrings, path)