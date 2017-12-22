######################################################### lomutos partition and quick sort

def lomutosPartition(high,low,array):
  pivot = array[high]
  index = low - 1 
  for j in range(low,high):
    if array[j] <= pivot:
      index+=1
      temp = array[index]
      array[index] = array[j]
      array[j] = temp
  temp = array[high]
  array[high] = array[index+1]
  array[index+1] = temp

  return index+1

def lomutoQuickSort(high,low,array):
  if(low < high):
    partition = lomutosPartition(high,low,array)
    lomutoQuickSort(partition-1,low,array)
    lomutoQuickSort(high,partition+1,array)

def quickSortLomuto(arr):
  lomutoQuickSort(len(arr) - 1 ,0,arr)
  return arr
        
######################################################### hoares partition and quick sort

def hoaresPartition(high,low,array):
  pivot = array[low]
  lowIndex = low-1
  highIndex = high + 1 
  while True:
    while True:
      highIndex = highIndex - 1 
      if (array[highIndex] <= pivot):
        break
    while True:
      lowIndex = lowIndex + 1 
      if(array[lowIndex] >= pivot):
        break
    if ( lowIndex < highIndex ):
      temp = array[lowIndex]
      array[lowIndex] = array[highIndex]
      array[highIndex] = temp
    else:
      return highIndex
      
    
def hoareQuickSort(high,low,array):
  if(low < high):
    partition = hoaresPartition(high,low,array)
    hoareQuickSort(partition,low,array)
    hoareQuickSort(high,partition+1,array)

def quickSortHoare(arr):
  hoareQuickSort(len(arr) - 1 ,0,arr)
  return arr
  
####################################################################################################


  
arr = [15,4,68,24,75,16,42] 

print(quickSortHoare(arr))
print(quickSortLomuto(arr))



