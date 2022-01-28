# Raghavendra Reddy
sortedFile = open("sortedFile.txt","r")
reducerFile = open("reducedFile.txt", "w")

thisKey = ""
thisValue = 0.0

for line in sortedFile:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      reducerFile.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
reducerFile.write(thisKey + '\t' + str(thisValue)+'\n')

sortedFile.close()
reducerFile.close()