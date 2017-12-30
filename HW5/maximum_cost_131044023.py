#öncelikle ilk elemanı ayrı olarak kontrol ettim, eğer elementIndex sona gelmişse son eleman için ayrı bir kontrol ettim
#onun dışındaki case ler için 3 erli 3 erli kontrol ettim, eğer ortadaki elemanın yerine 1 yazılması ilk haline gore costu arttırıyorsa 1 yazdım aksi takdirde 
#eski şekilde bıraktım.

def helper_find_maximum_cost(Y,elementIndex):
  if(len(Y) == 0 or len(Y) == 1):
    return

  if(elementIndex == 0):
    sum1 =  abs(1 - Y[1])  + abs(Y[2] - Y[1])
    sum2 = abs(Y[0] - Y[1]) + abs (Y[1] - Y[2] )
    if(sum1>sum2):
      Y[0] = 1
    return helper_find_maximum_cost(Y,elementIndex+1)
    
  if(elementIndex == len(Y)-1):
    sum2 = abs(Y[elementIndex-2] - Y[elementIndex-1]) + abs(Y[elementIndex-1] - Y[elementIndex]) 
    sum1 = abs(Y[elementIndex-2] - Y[elementIndex-1]) + abs(1 -  Y[elementIndex-1])
 
    if(sum1>sum2):
      Y[elementIndex] = 1
    return 
  
  if(elementIndex <= len(Y)-2 ):
    sum1 = abs(Y[elementIndex-1] - Y[elementIndex]) + abs(Y[elementIndex] - Y[elementIndex+1])
    sum2 = abs(Y[elementIndex-1] - 1) + abs(1 - Y[elementIndex+1])
    if(sum2>sum1):
      Y[elementIndex] = 1
      helper_find_maximum_cost(Y,elementIndex+2)
    else:
      helper_find_maximum_cost(Y,elementIndex+1)
      


def find_maximum_cost(Y):
  helper_find_maximum_cost(Y,0)
  sum = 0
  for i in range (0,len(Y)-1):
    sum = sum + abs(Y[i] - Y[i+1])
  return sum



Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y) 
print(cost)