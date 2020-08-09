import xml.etree.ElementTree as ET
import sys, getopt
from xml.dom import minidom
from random import randint

print("1-Almanca\n2-İngilizce")
long_code = input()
if long_code == "1":
   tree = ET.parse('almanca.xml')
else:
   tree = ET.parse('ingilizce.xml')

root = tree.getroot()
lst = root.findall('no')

var = 1
while var == 1:
   random = randint(1, len(list(root)))
   for item in lst:
      if (item.get('x') == str(random)):              
         print("\n\n**********************************************")
         print(item.find('word').text)
         print("----------------------------------------")
         input()
         print(item.find('meaning').text)
         print("----------------------------------------")         
         print(item.find('example').text)
         print("**********************************************\n\n\n\n")




