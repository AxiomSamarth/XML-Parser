import xml.etree.ElementTree as ET
import os
from find_child import *
from find_child_content import *

def one_line(contents):
	line = []

	for content in contents:
		for i in content:
			line.append(i)

	line = (',').join(line)
	return line

files = ['country_data', 'catalog', 'resume','new_xml','food']

for file in files:
	tree = ET.parse('xmlFiles/' + file +'.xml')
	root = tree.getroot()
	nodes = []

	for child in root:
	    find_child(child,nodes)

	contents = []

	for child in root:
	    li = []
	    find_child_contents(child,li) 
	    contents.append(li)	    

	#print contents

	file = open('csvFiles/' + file + '.csv','w')

	file.write((',').join(nodes) + "\n")


	for content in contents:
		#print content, type(content)
		line = ""
		if len(content) > 1:
			line = (',').join(content) + "\n"
			file.write(line)
		else:
			line = one_line(contents)
			file.write(line)
			break

	file.close()	
     
for file in files:
	os.system("subl csvFiles/" + file + ".csv" )     