sFile = open("pSource.txt", "r")
tFile = open("tSource.txt", "r")

sArray = sFile.readlines()
tArray = tFile.readlines()

fArray = set(tArray) - set(sArray)

print sorted(fArray)

fFile=open("fFile.txt", "w")
for i in sorted(fArray):
    fFile.write(i)

sFile.close()
tFile.close()
