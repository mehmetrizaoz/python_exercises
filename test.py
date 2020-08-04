import xml.etree.ElementTree as ET
import sys, getopt
from xml.dom import minidom
from random import randint

tree = ET.parse('items.xml')
root = tree.getroot()
lst = root.findall('no')
random = randint(1, len(list(root)))

for item in lst:
   if (item.get('x') == str(random)):
      print(item.find('word').text)
      input()
      print(item.find('meaning').text)
      print(item.find('example').text)




