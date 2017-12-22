
def  min_subarray_finder(inpArr,probablities):

  tempList = []
  minSum = 999999999
  myList = []
  minSumList = []
  for i in range(0,len(inpArr)):
    tempList.append(inpArr[i])
    probablities.append(list(tempList))
    min_subarray_finder(inpArr[i+1:],probablities)





def mmain(inputt):
  probablities = []
  
  longestString = []
  longestStringLong = 0
  
  for i in inputt:
    probablities = []
    min_subarray_finder(i,probablities)
    temp = ""
    for j in probablities:
      count = 0
      for k in inputt:
        if i!=k and temp.join(j) in k:
          count = count + 1
      if(count==len(inputt)-1 and len(temp.join(j)) > longestStringLong):
        longestString = temp.join(j)
        longestStringLong = len(longestString)
  
  
  print(longestString)
  
    




inpStrings = ["absorptivity", "circularity","electricity", "importunity", "humanity"]
mmain(inpStrings)