# Raghavendra Reddy
import operator
f = open("reducedFile.txt","r")  # open file, read-only
sorterFile = open("reduceSorted.txt", "w") # open file, write
count = 0
ar = []
for line in f:  
    rowList = line.strip().split("\t") 
    if len(rowList) == 2:
        values = (float(rowList[1]),rowList[0]) #tuple creation with amount as first record
        ar.append(values) #append to list
ar.sort()
#loop and append to file
for line in ar:
  sorterFile.write("{0}\t{1}\n".format(line[1], line[0]))

print(ar)
f.close()
sorterFile.close()