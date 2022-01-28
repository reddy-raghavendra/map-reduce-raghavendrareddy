openFile = open("reducedFile.txt","r")  # open file, read-only
sorterFile = open("reduceSorted.txt", "w") # open file, write
lines = openFile.readlines()
lines.amount.sort()

for line in lines:
 sorterFile.write(line)

openFile.close()
sorterFile.close()