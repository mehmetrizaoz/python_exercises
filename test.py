import xml.etree.ElementTree as ET
import sys, getopt
from xml.dom import minidom

tree = ET.parse('items.xml')
root = tree.getroot()
lst = root.findall('no')
wordId = sys.argv[1]

for item in lst:
   if (item.get('x') == wordId):
      print(item.find('word').text + ": " + item.find('meaning').text + "\n")
      print(item.find('example').text)
       
   
