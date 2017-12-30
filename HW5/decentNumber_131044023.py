#N değerinin 3 e ve 5 e göre modlarının adedi toplamı N değerine eşit olduğu an bizim istediğimiz sonucu alacağımız an olacaktır.
# Bu yüzden bu kural dikkate alınarak döngü içinde değerler toplanarak çözüme gidildi.
#worst case O(N/2)

def decentNumber(N):
  
  result = ""
  for i in range (N):
    count1 = i;
    count2 = N - i;
    
    if(count1 % 3 == 0 and count2 % 5 == 0):
      for j in range(0,count1):
        result += str('5')
      for j in range(0,count2):
        result += str('3')
      break
    elif(count1 % 5 == 0 and count2 % 3 == 0):
      for j in range(0,count2):
        result += str('5')
      for j in range(0,count1):
        result += str('3')
      break
    
  if(result == ""):
    return -1
        
    
  return result

print(decentNumber(1))  
print(decentNumber(2))  
print(decentNumber(3))  
print(decentNumber(4))  
print(decentNumber(5))  
print(decentNumber(6))  
print(decentNumber(7))  
print(decentNumber(8))  
print(decentNumber(9))  
print(decentNumber(10))  
print(decentNumber(11))  
print(decentNumber(12))  
print(decentNumber(13))  
print(decentNumber(14))  
print(decentNumber(15))  
print(decentNumber(16))  
print(decentNumber(17))  
    

  


