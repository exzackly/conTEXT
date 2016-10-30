import xml.etree.ElementTree as ET
import string
import re

def sanitizeString(input):
	#tokenize URLs and ellipses
	input = re.sub("http[^\s]*", " [URL] ", input)
	input = re.sub("\.{3,}", " [ELLIPSIS] ", input)
	#pad punctuation with spaces
	for mark in [",", "!", "?", ")", "(", ":", ";", "*", '"', "\n", "."]:
		input = input.replace(mark, " {0} ".format(mark))
	for replace, mark in [(" '", " ' "), ("' ", " ' ")]:
		input = input.replace(replace, " {0} ".format(mark))
	#condense runs of spaces
	input = list(re.sub( ' +', ' ', input).strip())
	#pad result with leading and trailing spaces
	input.insert(0, " ")
	input += [" "]
	return ''.join(input).lower()

def extract_messages(infile, outfile, myName):
	tree = ET.parse(infile)
	root = tree.getroot()

	#grab messages and corresponding senders
	D = root.findall(".//div[@class='thread']/div[@class='message']")
	P = root.findall(".//div[@class='thread']/p")

	#open outfile for writing
	fileHandle = open(outfile, "w")

	#iterate over messages, writing each message
	#sent by myName to output file
	for i in range(0,len(D)):
		text = P[i].text
		for item in D[i].findall(".//div[@class='message_header']/span[@class='user']"):
			user = item.text
		if user != None and user == myName and text != None:
			fileHandle.write(str(sanitizeString(str(text.encode("utf-8"))[2:-1]) + "\n"))

	#close output file
	fileHandle.close()