openFile = open("output.txt","r")  # open file, read-only
sorterFile = open("sortedFile.txt", "w") # open file, write
lines = openFile.readlines()
lines.sort()

for line in lines:
 sorterFile.write(line)

openFile.close()
sorterFile.close()