
#Adding a Task
# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
#
#
# additional_task = raw_input("Add a task")
#
# print "Ok, I'm writing this to the tasks list"
#
# target = open(filename, 'a')
# target.write(additional_task)


#Remove a task
import sys
import shutil

delete_this = raw_input("Enter the line number you wish to delete")
print 'Input file:'+ sys.argv[1]
print 'Output file:'+ sys.argv[2]

shutil.copy(sys.argv[1],sys.argv[2])# copied content to the new file

inputFile = open(sys.argv[1], "r+")
outputFile = open(sys.argv[2], "w")


outputFile.writelines(inputFile.readlines()[delete_this])
inputFile.close()
outputFile.close()
print 'created sm file with scattering matrix'
