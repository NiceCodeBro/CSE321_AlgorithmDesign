# Gelen arrayin uzunluğunun 1 olup olmamasına göre base case belirledim.
# gelen arrayi ortasından sağa ve sola doğru gezip sağdan ve soldan minimum sub arrayi buluyorum
# sonrasında iki arrayi birleştiriyorum, elime geçen 3 arrayi karşılaştırıp minimumu belirliyorum
# mevcut Array'i her seferinde 2 recursiv koldan çağırıp iki kolun sonucunu çekiyorum
# öncesinde hesaplanan midArray ile bu iki koldan gelen sonucu karşılaştırıp en küçüğünü döndürüyorum

def min_subarray_finder(inpArr):
  if(len(inpArr) > 1):
    mid = len(inpArr)//2

    midArray = []
    sumRightArray = []
    sumLeftArray = []
    sumLeft = 9999999
    for i in range(mid-1,-1,-1):
      if( sum(inpArr[i:mid]) < sumLeft):
        sumLeftArray = inpArr[i:mid]
        sumLeft = sum(sumLeftArray)
    sumRight = 9999999
    for i in range(mid,len(inpArr)):
      if(sum(inpArr[mid:i+1]) < sumRight):
        sumRightArray = inpArr[mid:i+1]
        sumRight = sum(sumRightArray)
      
    midArray.extend(sumLeftArray)
    midArray.extend(sumRightArray)
    
    if(sum(sumRightArray) < sum(sumLeftArray) and sum(sumRightArray) < sum(midArray)):
      midArray = sumRightArray
    elif(sum(sumLeftArray) < sum(sumRightArray) and sum(sumLeftArray) < sum(midArray)):
      midArray = sumLeftArray

    leftArray = min_subarray_finder(inpArr[0:mid])
    rightArray = min_subarray_finder(inpArr[mid:len(inpArr)])
    
    if(sum(sumLeftArray) < sum(sumRightArray) and sum(sumLeftArray) < sum(midArray)):
      return sumLeftArray
    elif(sum(sumRightArray) < sum(sumLeftArray) and sum(sumRightArray) < sum(midArray)):
      return sumRightArray
    elif(sum(midArray) < sum(sumLeftArray) and sum(midArray) < sum(sumRightArray)):
      return midArray
      
        
  else:
    return inpArr

inpArr =  [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print (msa)





