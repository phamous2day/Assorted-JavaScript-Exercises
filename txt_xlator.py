
from sys import argv
script = argv
import json
file = open('abbv.json', 'r')
abbreviations = json.loads(file.read())

txt= raw_input("What is the text?").upper()



print "Text translates to: ", abbreviations[txt]




file.close()
