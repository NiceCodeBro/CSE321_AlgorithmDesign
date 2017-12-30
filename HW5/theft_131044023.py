# problemi satır satır ele aldım. her satırı sondan başa doğru ekleye ekleye ilk rowda ne kadar cost olabileceğini hesapladım
# Öncelikle problemi 3 parçaya ayırdım
# 1. parça en üst rowda işlem yapılma durumu; bu durumda sadece sağa ve sağ alta gidilebilirdi, sanki sona gelmiş de oradan başa gidiyormuş gibi topladım
# 2. parça en son rowda olma durumu ; bu durumda 1. durum gibi sadece sağa ve sağ üste gitme durumunu kontrol ettim
# 3. parçada ise ortada olma durumunu kontrol ettim; bu sefer hem orta hem sağ alt hem de sağ üstte gidebilme durumlarını kontrol ettim.
# en sonda ise olabilecek tüm maxlar 0. column da toplanmış oldu, buradan max'ı bularak return ettim.
# iç içe for loop olduğu için worst case O(m*n)


def theft(amountOfMoneyInLand):

  for j in range(0,len(amountOfMoneyInLand[0])):
    for i in range(len(amountOfMoneyInLand)-1,0,-1):
      if(j == 0):#for first row
        amountOfMoneyInLand[j][i-1] = amountOfMoneyInLand[j][i-1] +  max(amountOfMoneyInLand[j][i],amountOfMoneyInLand[j+1][i])
      elif(j == len(amountOfMoneyInLand[0])-1): #for last  row
        amountOfMoneyInLand[j][i-1] = amountOfMoneyInLand[j][i-1] +  max(amountOfMoneyInLand[j][i],amountOfMoneyInLand[j-1][i])
      else: #other rows
        amountOfMoneyInLand[j][i-1] = amountOfMoneyInLand[j][i-1] +  max(amountOfMoneyInLand[j][i],amountOfMoneyInLand[j-1][i],amountOfMoneyInLand[j+1][i])
  
  
  #print(amountOfMoneyInLand)
  maximum = amountOfMoneyInLand[0][0]
  
  for i in range(0,len(amountOfMoneyInLand[0])):
    if(amountOfMoneyInLand[i][0] > maximum):
      maximum = amountOfMoneyInLand[i][0]
  
  return maximum
  
amountOfMoneyInLand =  [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]] 
res = theft(amountOfMoneyInLand)
print(res)