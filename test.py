import xml.etree.ElementTree as ET
import sys, getopt
from xml.dom import minidom
from random import randint

print("Select Language: \n1-Almanca\n2-İngilizce\n")
long_code = input()
if long_code == "1":
   tree = ET.parse('almanca.xml')
else:
   tree = ET.parse('ingilizce.xml')

root = tree.getroot()
lst = root.findall('no')
print("\n\n\n")

var = 1
while var == 1:
   random = randint(1, len(list(root)))
   for item in lst:
      if (item.get('x') == str(random)):              
         print("\n\n**********************************************")
         print(item.find('word').text)
         print("----------------------------------------")
         answer = input()
         if(answer == "OK"):
            print("mmmmmm")
         print(item.find('meaning').text)
         print("----------------------------------------")         
         print(item.find('example').text)
         print("**********************************************\n\n\n\n")




