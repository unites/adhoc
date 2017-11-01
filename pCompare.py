#!/usr/bin/env python

import sys

sFile = open("pSource.txt", "r")
tFile = open("tSource.txt", "r")

sArray = sFile.readlines()
tArray = tFile.readlines()

fArray = set(tArray) - set(sArray)
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

print sorted(fArray)

fFile=open("fFile.txt", "w")
for i in sorted(fArray, reverse=True):
    fFile.write(i)

sFile.close()
tFile.close()

