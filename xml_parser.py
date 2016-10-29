#!/usr/bin/python3

import xml.etree.ElementTree as ET
import string
import re

tree = ET.parse('messages.htm')
root = tree.getroot()

myName = "Brendon Boldt"

'''
myMessages = []
for elem in root.iter('thread'):
  if elem.attrib.get('class') == 'message':
    for span in elem.iter('span'):
      if span.attrib.get('class') == 'user' and span.text == myName:
        print(span.text)
        for val in elem.iter('p'):
          myMessages.append(val.text)
'''

def sanitizeString(input):
	input = re.sub("http[^\s-]*", " [URL] ", input)
	for mark in [",", "!", "?", ")", "("]:
		input = input.replace(mark, " {0} ".format(mark))
	input = re.sub(" '", " ' ", input)
	input = re.sub("' ", " ' ", input)
	input = re.sub(' "', ' " ', input)
	input = re.sub('" ', ' " ', input)
	input = input.replace("\n", " \n ")
	input = list(re.sub( ' +', ' ', input).strip())
	input.insert(0, " ")
	input += [" "]
	return ''.join(input)

D = root.findall(".//div[@class='thread']/div[@class='message']")
P = root.findall(".//div[@class='thread']/p")

fileHandle = open("output.txt", "w")

for i in range(0,len(D)):

	text = P[i].text
	for item in D[i].findall(".//div[@class='message_header']/span[@class='user']"):
		user = item.text
	if user != None and user == myName and text != None:
		fileHandle.write(str(sanitizeString(str(text.encode("utf-8"))[2:-1]) + "\n"))

fileHandle.close()
'''
for thread in :
	print(thread.text)
	if a == 30:
		break
	a += 1
	for message in thread.findall("*"): 
		print(message.attrib)
		#message[0] = user
		#message[1] = timestamp
		for item in message:
			print(item.text)
			'''
  
'''
 for thread in root.findall(".//div[@class='thread']/p"):
    if message.attrib.get(

print(len(myMessages))
print(myMessages[0])
'''

