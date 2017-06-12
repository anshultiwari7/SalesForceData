import re
import requests
import bs4
from collections import OrderedDict

apostedby =[]
atitle = []
avotepoints = []
astatus = []
acomments = []
# acommentdetail = OrderedDict()
# dictlist = [OrderedDict() for x in range(5000)]
# acommentdetail = []
acommentedby = []
acommentcontent = []
total = 0


def idea_details(url):
      html = requests.get(url)
      soup=bs4.BeautifulSoup(html.text,'html.parser')
      comment = soup.findAll('div',attrs={'class':'cmp-comments-body'})
      # print comment
      counter = 0
      for temp in comment:
      	counter = counter + 1
      	commentedby = temp.find('a').string
      	# print commentedby
      	# commentcontent = temp.find('div',attrs={'class':'htmlDetailElementDiv'})
      	# print commentcontent.string
      	commentcontent = temp.find('tr').find('td').find('div')
      	acommentedby.append(commentedby)
      	acommentcontent.append(commentcontent.string)
      	# acommentdetail[commentedby] = commentcontent.string
      # acommentdetail
      acomments.append(counter)

def idea_search(url):
      html = requests.get(url)
      soup=bs4.BeautifulSoup(html.text,'html.parser')
      
      title = soup.findAll('p', attrs={'class':'item-title'} )
      for temp in title:
      	# print temp.find('span').string
      	global total 
      	total = total + 1
      	atitle.append(temp.find('span').string)
      	# print temp.find('a')['href']
      	idea_details(temp.find('a')['href']+"")

      votepoints = soup.findAll('span', attrs={'class':'vote-points-value'})
      for temp in votepoints:
      	# print temp.string
      	tempstr = re.findall('\d+',temp.string)
      	# print "Hello"+str(tempstr)+"check"
      	digfull = ""
      	for dig in tempstr:
      		digfull = digfull + dig
      	# print digfull
      	avotepoints.append(digfull)

      status = soup.findAll('span', attrs={'class':'comty-status-badge'})
      for temp in status:
      	# print temp.string
      	astatus.append(temp.string.rstrip())

      postedby = soup.findAll('div', attrs={'class':'user-snap'})
      for temp in postedby:
      	# print temp.find('span').string
      	apostedby.append(temp.find('span').string)


mainurl = "https://success.salesforce.com/ideaSearch"


def print_details():
	i = 0
	j=0
	global avotepoints
	# global acommentedby
	global acomments
	global acommentedby
	global atitle
	global astatus
	global acommentcontent
	global apostedby
	global total
	while i!=total:
		print "{"
		if atitle[i]!=None:
			print "\"Title\" : \"" + str(atitle[i].encode('utf-8')) + "\","
		else:
			print "\"Title\" : \"" + str(atitle[i]) + "\","

		if apostedby[i]!=None:
			print "\"Posted by\" : \"" + str(apostedby[i].encode('utf-8')) + "\","
		else:
			print "\"Posted by\" : \"" + str(apostedby[i]) + "\","

		if astatus[i]!=None:
			print "\"Status\" : \"" + str(astatus[i].encode('utf-8')) + "\","
		else:		
			print "\"Status\" : \"" + str(astatus[i]) + "\","
		
		if avotepoints[i]!=None:
			print "\"Vote Points\" : \"" + str(avotepoints[i].encode('utf-8')) + "\","
		else:
			print "\"Vote Points\" : \"" + str(avotepoints[i]) + "\","

		print "\"Total Comments\" : \"" + str(acomments[i]) + "\","
		
		print "\"Comments\" : ["

		limit = acomments[i]+j
		while j!=limit:
			if acommentedby[j] != None and acommentcontent[j] != None :
				print "\t\t\t { \"" + str(acommentedby[j].encode('utf-8')) + "\" : \"" + str(acommentcontent[j].encode('utf-8')) + "\" }, " 
			elif acommentedby[j] != None and acommentcontent[j]==None:
				print "\t\t\t { \"" + str(acommentedby[j].encode('utf-8')) + "\" : \"" + str(acommentcontent[j]) + "\" }, "
			elif acommentcontent[j] ==None and acommentcontent[j]!=None:
				print "\t\t\t { \"" + str(acommentedby[j]) + "\" : \"" + str(acommentcontent[j].encode('utf-8')) + "\" }, "
			# print acommentcontent[j]
			j=j+1
		print "\t\t\t] \n},\n\n\n"


		i = i + 1
	# limit = 0
	acommentcontent = []
	acomments = []
	# apostedby = []
	acommentedby = []
	apostedby = []
	astatus = []
	atitle = []
	avotepoints = []
	total = 0


for pageno in range(1,501):
	if pageno == 1:
		urlstr = mainurl
	else:
		urlstr = mainurl + "?pageNo=" + str(pageno)
	
	idea_search(urlstr)
	print_details()