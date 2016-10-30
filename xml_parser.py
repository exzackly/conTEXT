#!/usr/bin/python3

import xml.etree.ElementTree as ET
import string
import re

def sanitizeString(input):
	input = re.sub("http[^\s]*", " [URL] ", input)
	input = re.sub("\.{3,}", " [ELLIPSIS] ", input)
	for mark in [",", "!", "?", ")", "(", ":", ";", "*", '"', "\n", "."]:
		input = input.replace(mark, " {0} ".format(mark))
	for replace, mark in [(" '", " ' "), ("' ", " ' ")]:
		input = input.replace(replace, " {0} ".format(mark))
	input = list(re.sub( ' +', ' ', input).strip())
	input.insert(0, " ")
	input += [" "]
	return ''.join(input)

def extract_messages(infile, outfile, myName):
  tree = ET.parse(infile)
  root = tree.getroot()

  D = root.findall(".//div[@class='thread']/div[@class='message']")
  P = root.findall(".//div[@class='thread']/p")

  fileHandle = open(outfile, "w")

  for i in range(0,len(D)):
    text = P[i].text
    for item in D[i].findall(".//div[@class='message_header']/span[@class='user']"):
      user = item.text
    if user != None and user == myName and text != None:
      fileHandle.write(str(sanitizeString(str(text.encode("utf-8"))[2:-1]) + "\n"))

  fileHandle.close()