
def hanoiProblem(SRC,DST,AUX,n,sumofweights):

  
  if n == 1:
    print('disk 1: %s to %s' %(SRC,DST))
    
    if (SRC == 'SRC' and DST == 'DST') or (SRC == 'DST' and DST == 'SRC'):
      sumofweights[n-1]+=2
    else:
      sumofweights[n-1]+=1
  else:
    hanoiProblem(SRC,AUX,DST,n-1,sumofweights)
    print('disk %s: %s to %s' %(n,SRC,DST))
    if (SRC == 'SRC' and DST == 'DST') or (SRC == 'DST' and DST == 'SRC'):
      sumofweights[n-1]+=2*n
    else:
        sumofweights[n-1]+=n
    
    hanoiProblem(AUX,DST,SRC,n-1,sumofweights)
  

def hanoi(SRC,DST,AUX,n):
  sumofweights=[]
  for i in range(n):
      sumofweights.append(0)
    
  hanoiProblem('SRC','DST','AUX',n,sumofweights)
  print(sumofweights)
  


hanoi('SRC','DST','AUX',3)