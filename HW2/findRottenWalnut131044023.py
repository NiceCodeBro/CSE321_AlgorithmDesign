import math

def compareScales (leftScaleList, rightScaleList):     
  result = sum(leftScaleList) - sum(rightScaleList)     
  
  if result < 0:         
    return 1     
  elif result > 0:         
    return -1     
  else:         
    return 0
    

  
def indexOfWalnuts(walnuts):
  if len(walnuts) % 2 == 1:
    if walnuts[math.floor(len(walnuts)/2)] == 0.5:
      return math.floor(len(walnuts)/2) ;
    elif compareScales(walnuts[0:math.floor(len(walnuts)/2)], walnuts[math.floor(len(walnuts)/2)+1:]) == 1 : 
      return indexOfWalnuts(walnuts[0:math.floor(len(walnuts)/2)])
    elif compareScales(walnuts[0:math.floor(len(walnuts)/2)], walnuts[math.floor(len(walnuts)/2)+1:]) == -1 :
      return  math.floor((len(walnuts)/2)+1) + indexOfWalnuts(walnuts[math.floor(len(walnuts)/2)+1:])
  else:
    if compareScales(walnuts[0:math.floor(len(walnuts)/2)], walnuts[math.floor(len(walnuts)/2):]) == 1 :
      return indexOfWalnuts(walnuts[0:math.floor(len(walnuts)/2)])
    elif compareScales(walnuts[0:math.floor(len(walnuts)/2)], walnuts[math.floor(len(walnuts)/2):]) == -1 :
      return  math.floor(len(walnuts)/2) + indexOfWalnuts(walnuts[math.floor(len(walnuts)/2):])
  return 0
    
    
def wrapperRottenWalnut(walnuts):
  if len(walnuts) == 0:
    print ('List is empty')
  else:
    index =  indexOfWalnuts(walnuts)
    if index == 0 and walnuts[index] != 0.5:
      print('No rotten walnuts')
    else:
      print ('Rotten walnut at %sth index' %index)
      
  
sumofweights=[1, 1, 1, 0.5]

wrapperRottenWalnut(sumofweights)
